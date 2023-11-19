import argparse
import subprocess

from gpt4all import GPT4All
import speech_recognition as sr
from TTS.api import TTS
from playsound import playsound


class GlowTTS:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False)

    def process(self, text, audio_save_path):
        return self.tts.tts(text=text, file_path=audio_save_path)


class GPT4AllChatBot:
    """Voice chat bot based on Whisper and GPT4All"""

    def __init__(self, gpt_model_name, whisper_model_type, tts_rate=165):
        self.gpt_model = GPT4All(gpt_model_name)

        self.whisper_model_type = whisper_model_type

        self.voice_recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        self.tts_engine = GlowTTS()

    def run(self):
        """Run the listen-think-response loop"""
        input_words = self._voice_to_text()
        print("===> question:", input_words)
        answer = self.run_gpt(input_words)
        print("==> answer:", answer)
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

        messages = [{"role": "user", "content": question}]
        response = self.gpt_model.chat_completion(
            messages,
            default_prompt_footer=False,
            default_prompt_header=False,
            verbose=False,
        )
        try:
            answer = response["choices"][0]["message"]["content"]
        except:
            answer = "ERROR: Wrong Response"
        return answer

    def _text_to_voice(self, answer):
        """Convert text to voice using TTS tools"""
        audio = self.tts_engine.process(answer, "tmp.wav")
        playsound("tmp.wav")
        # self.tts_engine.say(answer)
        # self.tts_engine.runAndWait()


if __name__ == "__main__":
    tts_engine = GlowTTS()
    answer = "Hello"
    audio = tts_engine.process(answer)
    playsound(audio)
    raise ValueError

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gpt-model-name",
        type=str,
        default="ggml-gpt4all-j-v1.3-groovy",
        help="""GPT4All model name, All available names:
            [
            ggml-gpt4all-j-v1.3-groovy
            ggml-gpt4all-j-v1.2-jazzy
            ggml-gpt4all-j-v1.1-breezy
            ggml-gpt4all-j
            ggml-gpt4all-l13b-snoozy
            ggml-vicuna-7b-1.1-q4_2
            ggml-vicuna-13b-1.1-q4_2
            ggml-wizardLM-7B.q4_2
            ggml-stable-vicuna-13B.q4_2
            ]
            """,
    )
    parser.add_argument(
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
