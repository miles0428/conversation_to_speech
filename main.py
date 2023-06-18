from g_c import conversation  as c
from g_c import caption_to_docx as ctd
from g_c import multiple_sentence as ms
import os

#get the conversations
conversations = c.get_all_conversation("test.txt")
#get the utterances
conversations = c.get_all_utterances(conversations)

#generate ten 1 minute audio files
for i in range(10):
    os.mkdir(f"test_{i}")
    conversations = ms.conversations_to_speech(conversations, f"test_{i}/output_{i}.mp3", 60)
    ctd.caption_to_docx(f"test_{i}/output_{i}.srt", f"test_{i}/output_{i}.docx")
    print(f"test_{i} done")
