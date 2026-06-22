"""Main voice chat bot for talkGPT4All."""

from .llm import (
    LLMBackend,
    KimiBackend,
    DeepSeekBackend,
)
from .asr import (
    ASRBackend,
    ModernASRBackend,
)
from .tts import (
    TTSBackend,
    ModernTTSBackend,
)


class VoiceChatBot:
    """Voice chat bot with pluggable LLM, ASR and TTS backends."""

    def __init__(
        self,
        llm_type: str = "kimi",
        llm_model: str = "moonshot-v1-8k",
        asr_type: str = "sensevoice",
        asr_model: str = "sensevoice-small",
        tts_type: str = "qwen3-tts-0.6b",
        tts_model: str = "qwen3-tts-0.6b",
    ):
        print(
            f"==> LLM: {llm_type} ({llm_model}), "
            f"ASR: {asr_type} ({asr_model}), "
            f"TTS: {tts_type} ({tts_model})"
        )
        self.llm: LLMBackend = self._create_llm(llm_type, llm_model)
        self.asr: ASRBackend = self._create_asr(asr_type, asr_model)
        self.tts: TTSBackend = self._create_tts(tts_type, tts_model)

    @staticmethod
    def _create_llm(llm_type: str, llm_model: str) -> LLMBackend:
        llm_type = llm_type.lower().strip()
        if llm_type in ("kimi", "moonshot"):
            return KimiBackend(model=llm_model)
        elif llm_type == "deepseek":
            return DeepSeekBackend(model=llm_model)
        else:
            raise ValueError(
                f"Unknown LLM type: {llm_type}. "
                f"Supported: kimi, moonshot, deepseek"
            )

    @staticmethod
    def _create_asr(asr_type: str, asr_model: str) -> ASRBackend:
        asr_type = asr_type.lower().strip()
        if asr_type == "whisper":
            model_id = asr_model or "whisper-base"
        elif asr_type in ("funasr", "sensevoice"):
            model_id = asr_model or "sensevoice-small"
        else:
            # Treat as direct modern-asr model ID
            model_id = asr_type
        return ModernASRBackend(model_id=model_id)

    @staticmethod
    def _create_tts(tts_type: str, tts_model: str) -> TTSBackend:
        tts_type = tts_type.lower().strip()
        if tts_type == "glowtts":
            model_id = tts_model or "melotts-zh"
        elif tts_type == "chattts":
            model_id = "chattts"
        elif tts_type == "qwen3-tts-0.6b":
            model_id = "qwen3-tts-0.6b"
        elif tts_type == "cosyvoice":
            model_id = tts_model or "cosyvoice-300m"
        else:
            # Treat as direct modern-tts model ID
            model_id = tts_type
        return ModernTTSBackend(model_id=model_id)

    def run(self):
        """Run one listen-think-response loop."""
        input_words = self.asr.transcribe()
        if not input_words or not input_words.strip():
            print("No speech detected, skipping...")
            return
        print(f"==> You said: {input_words}")
        answer = self.llm.generate(input_words)
        print(f"==> Bot: {answer}")
        self.tts.speak(answer)


# Keep the old class name for backward compatibility
class GPT4AllChatBot(VoiceChatBot):
    """Deprecated: use VoiceChatBot instead."""

    def __init__(self, gpt_model_name, whisper_model_type, tts_rate=165):
        # tts_rate is ignored in the new architecture
        import warnings
        warnings.warn(
            "GPT4AllChatBot is deprecated. GPT4All backend has been removed. "
            "Use VoiceChatBot with an API-based LLM instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(
            llm_type="kimi",
            llm_model="moonshot-v1-8k",
            asr_type="whisper",
            asr_model=whisper_model_type,
            tts_type="glowtts",
        )
