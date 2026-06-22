# talkGPT4All

A modular voice chatbot supporting multiple LLM, ASR and TTS backends.

[Video demo](https://www.zhihu.com/zvideo/1625779747656515584).

Please check more details in this [blog post (in Chinese)](https://zhuanlan.zhihu.com/p/632592897).

If you are looking for the older version of talkGPT4All, please checkout to [dev/v1.0.0](https://github.com/vra/talkGPT4All/tree/dev/v1.0.0) branch.

## Supported Backends

### LLM (Large Language Model)
| Backend | Type | Default Model |
|---------|------|---------------|
| `gpt4all` | Local | `mistral-7b-openorca.Q4_0.gguf` |
| `kimi` / `moonshot` | API | `moonshot-v1-8k` |
| `deepseek` | API | `deepseek-chat` |

### ASR (Automatic Speech Recognition)
| Backend | Type | Default Model |
|---------|------|---------------|
| `whisper` | Local | `base` |
| `funasr` / `sensevoice` | Local | `iic/SenseVoiceSmall` |

### TTS (Text-to-Speech)
| Backend | Type | Default Model |
|---------|------|---------------|
| `glowtts` | Local | `tts_models/en/ljspeech/glow-tts` |
| `chattts` | Local | ChatTTS pre-trained |
| `cosyvoice` | Local | `pretrained_models/CosyVoice-300M-SFT` |

## Installation

### Basic installation (GPT4All + Whisper + GlowTTS)
```bash
pip install talkgpt4all
```

### With API LLM support (Kimi / DeepSeek)
```bash
pip install "talkgpt4all[openai]"
```

### With FunASR / SenseVoice support
```bash
pip install "talkgpt4all[funasr]"
```

### With ChatTTS support
```bash
pip install "talkgpt4all[chattts]"
```

### With CosyVoice support
```bash
pip install "talkgpt4all[cosyvoice]"
```

### Install everything
```bash
pip install "talkgpt4all[all]"
```

### Install from source code
```bash
git clone https://github.com/vra/talkGPT4All.git <ROOT>
cd <ROOT>
pip install -e ".[all]"
```

## API Key Setup

For API-based LLM backends, set the corresponding environment variable:

```bash
# Kimi (Moonshot)
export MOONSHOT_API_KEY="your-moonshot-api-key"

# DeepSeek
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

## Usage

### Quick start (default: GPT4All + Whisper + GlowTTS)
```bash
talkgpt4all
```

### Use Kimi + FunASR + ChatTTS
```bash
talkgpt4all \
  --llm-type kimi \
  --llm-model moonshot-v1-8k \
  --asr-type funasr \
  --asr-model iic/SenseVoiceSmall \
  --tts-type chattts
```

### Use DeepSeek + Whisper + CosyVoice
```bash
talkgpt4all \
  --llm-type deepseek \
  --llm-model deepseek-chat \
  --asr-type whisper \
  --asr-model base \
  --tts-type cosyvoice \
  --tts-model pretrained_models/CosyVoice-300M-SFT
```

### Use local GPT4All with custom model
```bash
talkgpt4all \
  --llm-type gpt4all \
  --llm-model mistral-7b-instruct-v0.1.Q4_0.gguf
```

## CLI Arguments

| Argument | Choices | Default | Description |
|----------|---------|---------|-------------|
| `--llm-type` | `gpt4all`, `kimi`, `moonshot`, `deepseek` | `gpt4all` | LLM backend type |
| `--llm-model` | model name | depends on type | LLM model name |
| `--asr-type` | `whisper`, `funasr`, `sensevoice` | `whisper` | ASR backend type |
| `--asr-model` | model name | depends on type | ASR model name |
| `--tts-type` | `glowtts`, `chattts`, `cosyvoice` | `glowtts` | TTS backend type |
| `--tts-model` | model name / path | depends on type | TTS model name or path |

**Backward compatibility:** `--gpt-model-name` and `--whisper-model-type` are still supported but deprecated.

## Extra dependencies for Linux users
We use [pyttsx3](https://github.com/nateshmbhat/pyttsx3) to convert text to voice. Please note that on Linux, you need to install dependencies:
```bash
sudo apt update && sudo apt install -y espeak ffmpeg libespeak1
```

## RoadMap
+ [x] Add source building for llama.cpp, with more flexible interface.
+ [x] More LLMs
+ [x] Add support for contextual information during chating.
+ [x] Modular backend architecture (LLM / ASR / TTS)
+ [x] Support for Kimi and DeepSeek API
+ [x] Support for FunASR / SenseVoice
+ [x] Support for ChatTTS and CosyVoice
+ [ ] Test code on Linux，Mac Intel and WSL2.
+ [x] Add support for Chinese input and output.
+ [ ] Add Documents and Changelog

Contributions are welcomed!
