import argparse
import sys
import warnings

from .chat import VoiceChatBot, GPT4AllChatBot


def main():
    parser = argparse.ArgumentParser(
        description="talkGPT4All - A modular voice chatbot supporting API-based LLM, modern-asr and modern-tts."
    )

    # LLM arguments
    parser.add_argument(
        "--llm-type",
        type=str,
        default="kimi",
        choices=["kimi", "moonshot", "deepseek"],
        help="LLM backend type. Default: kimi",
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        default=None,
        help="LLM model name. Defaults depend on --llm-type: "
             "kimi -> moonshot-v1-8k, "
             "deepseek -> deepseek-chat",
    )

    # ASR arguments
    parser.add_argument(
        "--asr-type",
        type=str,
        default="sensevoice",
        choices=["whisper", "funasr", "sensevoice"],
        help="ASR backend type. Default: sensevoice",
    )
    parser.add_argument(
        "--asr-model",
        type=str,
        default=None,
        help="ASR model name. Defaults depend on --asr-type: "
             "whisper -> whisper-base, "
             "funasr/sensevoice -> sensevoice-small",
    )

    # TTS arguments
    parser.add_argument(
        "--tts-type",
        type=str,
        default="qwen3-tts-0.6b",
        choices=["glowtts", "chattts", "cosyvoice", "qwen3-tts-0.6b", "qwen3-tts-1.7b"],
        help="TTS backend type. Default: qwen3-tts-0.6b",
    )
    parser.add_argument(
        "--tts-model",
        type=str,
        default=None,
        help="TTS model name / path. Defaults depend on --tts-type: "
             "glowtts -> melotts-zh, "
             "cosyvoice -> cosyvoice-300m, "
             "qwen3-tts-0.6b -> qwen3-tts-0.6b",
    )

    # Backward compatibility arguments
    parser.add_argument(
        "--gpt-model-name",
        type=str,
        default=None,
        help="[Deprecated, GPT4All has been removed] GPT4All model name",
    )
    parser.add_argument(
        "--whisper-model-type",
        type=str,
        default=None,
        help="[Deprecated, use --asr-model] Whisper model type",
    )
    parser.add_argument(
        "--voice-rate",
        type=int,
        default=165,
        help="[Deprecated] voice rate, no longer used",
    )

    args = parser.parse_args()

    # Resolve backward compatibility
    llm_model = args.llm_model
    asr_model = args.asr_model or args.whisper_model_type
    tts_model = args.tts_model

    # Set defaults based on backend type
    if llm_model is None:
        if args.llm_type in ("kimi", "moonshot"):
            llm_model = "moonshot-v1-8k"
        elif args.llm_type == "deepseek":
            llm_model = "deepseek-chat"

    if asr_model is None:
        if args.asr_type == "whisper":
            asr_model = "whisper-base"
        elif args.asr_type in ("funasr", "sensevoice"):
            asr_model = "sensevoice-small"

    if tts_model is None:
        if args.tts_type == "glowtts":
            tts_model = "melotts-zh"
        elif args.tts_type == "cosyvoice":
            tts_model = "cosyvoice-300m"
        elif args.tts_type == "chattts":
            tts_model = "chattts"
        elif args.tts_type == "qwen3-tts-0.6b":
            tts_model = "qwen3-tts-0.6b"

    if args.gpt_model_name:
        warnings.warn(
            "--gpt-model-name is deprecated and GPT4All backend has been removed. "
            "Use --llm-type and --llm-model with an API-based LLM instead.",
            DeprecationWarning,
        )
    if args.whisper_model_type:
        warnings.warn(
            "--whisper-model-type is deprecated, use --asr-model instead",
            DeprecationWarning,
        )

    chat_bot = VoiceChatBot(
        llm_type=args.llm_type,
        llm_model=llm_model,
        asr_type=args.asr_type,
        asr_model=asr_model,
        tts_type=args.tts_type,
        tts_model=tts_model,
    )
    while True:
        try:
            chat_bot.run()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
    sys.exit(0)


if __name__ == "__main__":
    main()
