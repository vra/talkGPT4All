import argparse
import subprocess

import pyttsx3
import speech_recognition as sr


class GPT4AllChatBot:
    """Voice chat bot based on Whisper and GPT4All"""

    def __init__(self, executable_path, model_path, whisper_model_type, tts_rate=165):
        self.executable_path = executable_path
        self.model_path = model_path

        self.whisper_model_type = whisper_model_type

        self.voice_recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        self.tts_engine = pyttsx3.init()  # object creation
        self.tts_engine.setProperty("rate", tts_rate)

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
            transcript = self.voice_recognizer.recognize_whisper(audio, self.whisper_model_type)
            return transcript

    def run_gpt(self, input_data):
        """Run GPT4All model with input_data as input"""

        binary_program = [
            self.executable_path,
            "-m",
            self.model_path,
            "-p",
            input_data.encode(),
        ]
        process = subprocess.Popen(
            binary_program, stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
        output_data = process.communicate()[0]
        string_data = output_data.decode("utf-8")
        return string_data

    def _text_to_voice(self, answer):
        """Convert text to voice using TTS tools"""
        self.tts_engine.say(answer)
        self.tts_engine.runAndWait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform",
        type=str,
        default="mac-m1",
        help="running platform, should be one of [mac-m1, mac-intel, linux, windows]",
    )
    parser.add_argument(
        "--whisper-model-type",
        type=str,
        default='base',
        help="whisper model type, default is base",
    )
    parser.add_argument(
        "--voice-rate",
        type=int,
        default=165,
        help="voice rate, default is 165, the larger the speak faster",
    )
    args = parser.parse_args()

    model_path = "models/gpt4all-lora-quantized.bin"
    executable_paths = {
        "mac-m1": "bin/gpt4all-lora-quantized-OSX-m1",
        "mac-intel": "bin/gpt4all-lora-quantized-OSX-intel",
        "linux": "bin/gpt4all-lora-quantized-linux-x86",
        "windows": "bin/gpt4all-lora-quantized-win64.exe",
    }
    executable_path = executable_paths.get(args.platform)
    if executable_path is None:
        raise NotImplementedError(f"the platform {args.platform} is not supported now!")

    chat_bot = GPT4AllChatBot(executable_path, model_path, args.whisper_model_type, args.voice_rate)
    while True:
        chat_bot.run()
