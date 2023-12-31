# Conversation to Speech

This is a tool to transfer conversation to speech in Mandarin-TW.
And this tool is powered by Google TTS API.

## Install

You can simplied install this tool by using git clone in your CLI.

```bash
git clone https://github.com/miles0428/conversation_to_speech.git
```

You also need to install some package in the requirement.txt

```bash

python -m pip install requirement.txt

```

## Credential Key

You will also need a credential key file for Google TTS API.  
Make sure that your key file in your project directory.  
you can see the [before you begin](https://cloud.google.com/text-to-speech/docs/create-audio-text-command-line) document at Google Cloud for detail.

## Test Dataset

We use [Diamante中文开放域闲聊数据集](https://www.luge.ai/#/luge/dataDetail?id=52) to test our code.

## Example

You can see example code in example.py

## Reference

[Lu, Hua, et al. "Towards Boosting the Open-Domain Chatbot with Human Feedback." arXiv preprint arXiv:2208.14165 (2022).](https://arxiv.org/pdf/2208.14165.pdf)
