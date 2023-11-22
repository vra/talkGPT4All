import argparse
import os
import subprocess
import tempfile

from gpt4all import GPT4All
from playsound import playsound
import speech_recognition as sr
from TTS.api import TTS


class GlowTTS:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False)

    def process(self, text, audio_save_path):
        return self.tts.tts_to_file(text=text, file_path=audio_save_path)


class GPT4AllChatBot:
    """Voice chat bot based on Whisper and GPT4All"""

    def __init__(self, gpt_model_name, whisper_model_type, tts_rate=165):
        print(f"==> GPT4All model: {gpt_model_name}, Whisper model: {whisper_model_type}")
        self.gpt_model = GPT4All(gpt_model_name, allow_download=True)

        self.whisper_model_type = whisper_model_type

        self.voice_recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        self.tts_engine = GlowTTS()

    def run(self):
        """Run the listen-think-response loop"""
        input_words = self._voice_to_text()
        answer = self.run_gpt(input_words)
        self._text_to_voice(answer)

    def _voice_to_text(self):
        """Listen voice and convert voice to text using OpenAI Whisper"""
        print("Listening...")
        with self.mic as source:
            self.voice_recognizer.adjust_for_ambient_noise(source)
            audio = self.voice_recognizer.listen(source)
            transcript = self.voice_recognizer.recognize_whisper(
                audio, self.whisper_model_type
            )
            return transcript

    def run_gpt(self, question):
        """Run GPT4All model with input_data as input"""

        with self.gpt_model.chat_session():
            answer = self.gpt_model.generate(prompt=question)
        print("==> answer:", answer)
        return answer

    def _text_to_voice(self, answer):
        """Convert text to voice using TTS tools"""
        tmp_file = tempfile.NamedTemporaryFile(
            prefix="talkgpt4all-", suffix=".wav", delete=False
        )
        tmp_dir = os.path.dirname(tmp_file.name)
        try:
            try:
                audio = self.tts_engine.process(answer, tmp_file.name)
            except RuntimeError:
                print(
                    "Errors occur when converting anwser to audio. please try another question."
                )
                return

            playsound(tmp_file.name)
        finally:
            tmp_file.close()
            os.remove(tmp_file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--gpt-model-name",
        type=str,
        default="mistral-7b-openorca.Q4_0.gguf",
        help="""GPT4All model name, All available names:
            [
            mistral-7b-openorca.Q4_0.gguf
            mistral-7b-instruct-v0.1.Q4_0.gguf
            gpt4all-falcon-q4_0.gguf
            orca-2-7b.Q4_0.gguf
            orca-2-13b.Q4_0.gguf
            wizardlm-13b-v1.2.Q4_0.gguf
            nous-hermes-llama2-13b.Q4_0.gguf
            gpt4all-13b-snoozy-q4_0.gguf
            mpt-7b-chat-merges-q4_0.gguf
            orca-mini-3b-gguf2-q4_0.gguf
            replit-code-v1_5-3b-q4_0.gguf
            starcoder-q4_0.gguf
            rift-coder-v0-7b-q4_0.gguf
            all-MiniLM-L6-v2-f16.gguf
            em_german_mistral_v01.Q4_0.gguf
            ]
            """,
    )
    parser.add_argument(
        "-w",
        "--whisper-model-type",
        type=str,
        default="base",
        help="whisper model type, default is base",
    )
    parser.add_argument(
        "--voice-rate",
        type=int,
        default=165,
        help="voice rate, default is 165, the larger the speak faster",
    )
    args = parser.parse_args()

    chat_bot = GPT4AllChatBot(
        args.gpt_model_name, args.whisper_model_type, args.voice_rate
    )
    while True:
        chat_bot.run()
