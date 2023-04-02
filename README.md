# talkGPT4All
A voice chatbot based on GPT4All and talkGPT.

[Video demo](https://www.zhihu.com/zvideo/1625779747656515584).

Please check more details in this [blog post (in Chinese)](https://zhuanlan.zhihu.com/p/618826760).

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
on Mac, no extra work needed, just use [say](https://ss64.com/osx/say.html).


on Linux ，please install [espeak](https://espeak.sourceforge.net/)，For example, on Ubuntu, run `sudo apt install espeak`.

On Windows , please install [wsay](https://github.com/p-groarke/wsay), you can download binary [at here](https://github.com/p-groarke/wsay/releases/tag/v1.5.0)，then put it into `<ROOT>/bin`.

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

## RoadMap
+ Test code on Linux，Mac Intel and WSL2.
+ Add support for contextual information during chating.
+ Add support for Chinese input and output.
+ Add source building for llama.cpp, with more flexible interface.
+ More LLMs

contributions are welcomed!

