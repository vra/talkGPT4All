# talkGPT4All
A voice chatbot based on GPT4All and talkGPT.

[Video demo](https://www.zhihu.com/zvideo/1625779747656515584).

Please check more details in this [blog post (in Chinese)](https://zhuanlan.zhihu.com/p/618826760).

If you are looking for the older version of talkGPT4All, please checkout to [dev/v1.0.0](https://github.com/vra/talkGPT4All/tree/dev/v1.0.0) branch.

## Installation
### Install Python Requirements
clone the code:
```bash
git clone https://github.com/vra/talkGPT4All.git <ROOT>
```

construct python virtual environment:
```bash
cd <ROOT>
python -m venv talkgpt4all
source talkgpt4all/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### Download Whispe model
```bash
wget https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt -o $HOME/.cache/whisper/base.pt
```

### Download GPT4All checkpoint
+ Direct link: <https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin>
+ Torrent: <https://tinyurl.com/gpt4all-lora-quantized>

put the downloaded model to folder `<ROOT>/models`.


### Download GPT4All binary executable

+ Mac M1: <https://raw.githubusercontent.com/nomic-ai/gpt4all/main/chat/gpt4all-lora-quantized-OSX-m1>
+ Mac Intel : <https://raw.githubusercontent.com/nomic-ai/gpt4all/main/chat/gpt4all-lora-quantized-OSX-Intel>
+ Linux : <https://raw.githubusercontent.com/nomic-ai/gpt4all/main/chat/gpt4all-lora-quantized-linux-x86>
+ Windows : <https://raw.githubusercontent.com/nomic-ai/gpt4all/main/chat/gpt4all-lora-quantized-win64.exe>

put the downloaded executable to `<ROOT>/bin`.

### Prepare Text to Voice program
We use [pyttsx3](https://github.com/nateshmbhat/pyttsx3) to convert text to voice. You can install it by running this:
```bash
pip install pyttsx3
```
Please note that on Linux ，You need to install dependencies:
```bash
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

## Usage
pattern: `python chat.py --platform <platform>`

Mac M1:
```bash
python chat.py --platform mac-m1
```

Mac Intel:
```bash
python chat.py --platform mac-intel
```

Linux:
```bash
python chat.py --platform linux
```

Windows:
```bash
python chat.py --platform windows
```

You can choose whisper model type using `--whisper-model-type <type>`, all available choices:
```python
{
"tiny.en"
"tiny"
"base.en"
"base"
"small.en"
"small"
"medium.en"
"medium"
"large-v1"
"large-v2"
"large"
}
```

You can tune the voice rate using `--voice-rate <rate>`, default rate is 165. the larger the speak faster.

e.g.,
```bash
python chat.py --platform mac-m1 --whisper-model-type large --voice-rate 150
```

## RoadMap
+ Test code on Linux，Mac Intel and WSL2.
+ Add support for contextual information during chating.
+ Add support for Chinese input and output.
+ Add source building for llama.cpp, with more flexible interface.
+ More LLMs

contributions are welcomed!

