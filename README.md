# talkGPT4All
A voice chatbot based on GPT4All and talkGPT.

[Video demo](https://www.zhihu.com/zvideo/1625779747656515584).

Please check more details in this [blog post (in Chinese)](https://zhuanlan.zhihu.com/p/632592897).

If you are looking for the older version of talkGPT4All, please checkout to [dev/v1.0.0](https://github.com/vra/talkGPT4All/tree/dev/v1.0.0) branch.

## Installation

### Install using pip (Recommend)
talkgpt4all is on PyPI, you can install it using simple one command:
```bash
pip install talkgpt4all
```
### Install from source code
Clone the code:
```bash
git clone https://github.com/vra/talkGPT4All.git <ROOT>
```

Install the dependencies and talkGPT4All in a python virtual environment:
```bash
cd <ROOT>
python -m venv talkgpt4all
source talkgpt4all/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Extra dependencies for Linux users
We use [pyttsx3](https://github.com/nateshmbhat/pyttsx3) to convert text to voice. Please note that on Linux ，You need to install dependencies:
```bash
sudo apt update && sudo apt install -y espeak ffmpeg libespeak1
```

## Usage
Open a terminal and type `talkgpt4all` to begin:
```bash
talkgpt4all
```

### Use different LLMs
You can choose different LLMs  using `--gpt-model-type <type>`, all available choices:
```python
{
"ggml-gpt4all-j-v1.3-groovy"
"ggml-gpt4all-j-v1.2-jazzy"
"ggml-gpt4all-j-v1.1-breezy"
"ggml-gpt4all-j"
"ggml-gpt4all-l13b-snoozy"
"ggml-vicuna-7b-1.1-q4_2"
"ggml-vicuna-13b-1.1-q4_2"
"ggml-wizardLM-7B.q4_2"
}
```

### Use different Whisper models
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

### Tune voice rate
You can tune the voice rate using `--voice-rate <rate>`, default rate is 165. the larger the speak faster.

e.g.,
```bash
talkgpt4all --whisper-model-type large --voice-rate 150
```

## RoadMap
+ [x] Add source building for llama.cpp, with more flexible interface.
+ [x] More LLMs
+ [x] Add support for contextual information during chating.
+ [ ] Test code on Linux，Mac Intel and WSL2.
+ [ ] Add support for Chinese input and output.
+ [ ] Add Documents and Changelog

contributions are welcomed!
