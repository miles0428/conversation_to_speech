from g_c import conversation  as c
from g_c import caption_to_docx as ctd
from g_c import multiple_sentence as ms
from g_c import one_sentence 
import os

#get the conversations
#the dataset is from [Diamante中文开放域闲聊数据集](https://www.luge.ai/#/luge/dataDetail?id=52),
#you should download the dataset and put it in the same directory as this file
conversations = c.get_all_conversation("test.txt")
#get the utterances
conversations = c.get_all_utterances(conversations)

os.mkdir("test")
#generate 2 1 minute audio files
for i in range(2):
    os.mkdir(f"test/test_{i}")
    conversations = ms.conversations_to_speech(conversations, f"test/test_{i}/output_{i}.mp3", 60)

    ctd.caption_to_docx(f"test/test_{i}/output_{i}.srt", f"test/test_{i}/output_{i}.docx")
    print(f"test_{i} done")
    if len(conversations) == 0:
        break

#generate one audio file with sigle sentence

one_sentence.text_to_speech("你好", "test/test_single.mp3")
