import argparse
import os
import subprocess

import speech_recognition as sr


LANGUAGES = {"en": "english", "zh-hans": "chinese"}


def run_gpt(executable_path, model_path, input_data):
    """Run GPT4All model with input_data as input"""

    binary_program = [
        executable_path,
        "-m",
        model_path,
        "-p",
        input_data.encode(),
    ]
    process = subprocess.Popen(
        binary_program, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    output_data = process.communicate()[0]
    string_data = output_data.decode("utf-8")
    return string_data


def voice_to_text():
    """Listen voice and convert voice to text using OpenAI Whisper"""
    print("Listening...")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        transcript = r.recognize_whisper(audio)
        return transcript


def text_to_voice(say_executable, answer, platform):
    """Convert text to voice using TTS tools"""
    cmd_str = say_executable + ' "' + answer.replace("\n", " ") + '"'

    # On Windows, subprocess.call raises errors. Need Fix in the future.
    if platform == "windows":
        subprocess.Popen(cmd_str)
    else:
        subprocess.call(cmd_str, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform",
        type=str,
        default="mac-m1",
        help="running platform, should be one of [mac-m1, mac-intel, linux, windows]",
    )
    args = parser.parse_args()

    model_path = "models/gpt4all-lora-quantized.bin"
    if args.platform == "mac-m1":
        gpt4all_executable = "bin/gpt4all-lora-quantized-OSX-m1"
        say_executable = "say"
    elif args.platform == "mac-intel":
        gpt4all_executable = "bin/gpt4all-lora-quantized-OSX-intel"
        say_executable = "say"
    elif args.platform == "linux":
        gpt4all_executable = "bin/gpt4all-lora-quantized-linux-x86"
        say_executable = "espeak"
    elif args.platform == "windows":
        gpt4all_executable = "bin/gpt4all-lora-quantized-win64.exe"
        say_executable = "bin/wsay.exe"
    else:
        raise NotImplementedError(
            "the platform {}is not supported now!".format(args.platform)
        )

    while True:
        input_words = voice_to_text()
        print('===> question:', input_words)
        answer = run_gpt(gpt4all_executable, model_path, input_words)
        print('==> answer:', answer)
        text_to_voice(say_executable, answer, args.platform)
