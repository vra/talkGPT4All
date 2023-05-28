import argparse

from .chat import GPT4AllChatBot


def main():
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
