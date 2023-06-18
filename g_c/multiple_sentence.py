from . import one_sentence 
from . import conversation
import os
from pydub import AudioSegment

def merge_mp3(output_file_name : str, file_names : list) -> None:
    '''
    merge multiple mp3 files into one mp3 file

    Args:
        output_file_name : the name of the output file
        file_names : a list containing the names of the mp3 files to be merged

    Return:
        None
    '''
    combined = AudioSegment.empty()
    for file_name in file_names:
        combined += AudioSegment.from_mp3(file_name)
    combined.export(output_file_name, format="mp3")


def merge_caption(output_file_name : str, captions : list, duration_times : list) -> None:
    '''
    merge multiple caption into one caption

    Args:
        output_file_name : the name of the output file
        captions : a list containing the captions to be merged
        duration_times : a list containing the duration time of each caption

    Return:
        None
    '''
    with open(output_file_name, "w", encoding='utf-8') as f:
        start_time = 0
        for i in range(len(captions)):
            f.write(one_sentence.generate_srt_style_text(captions[i], start_time, start_time+duration_times[i], i+1))
            start_time += duration_times[i]


def conversations_to_speech(conversations : list, output_file_name : str, duration_limit : int  = None) -> list:
    '''
    convert a list of conversations to a mp3 file and a caption file in srt format\n
    with the duration limit of the output file\n
    will return the conversations have not been converted

    Args:
        conversations : a list containing the conversations to be converted
        output_file_name : the name of the output file ending with .mp3
        duration_limit : the duration limit of the output file in seconds

    Return:
        conversations : a list containing the conversations have not been converted
    '''
    if duration_limit is None:
        #generate the audio files and captions
        file_names = [f'tmp_{i}.mp3' for i in range(len(conversations))]
        captions = [i for i in conversations]
        #generate the audio files
        for i in range(len(conversations)):
            one_sentence.text_to_speech(conversations[i], file_names[i])
        #get the duration of each audio file
        duration_times = [one_sentence.get_duration(file_name) for file_name in file_names]
        
        #merge the audio files and captions
        merge_mp3(output_file_name, file_names)
        merge_caption(output_file_name[:-4]+".srt", captions, duration_times)

        #remove the temp files  
        for file_name in file_names:
            os.remove(file_name)
        return []
    
    else:
        total_duration = 0
        file_names = []
        captions = []
        duration_times = []
        while total_duration < duration_limit*1000 and len(conversations) > 0:
            #generate the audio files and captions
            conversation = conversations[0]
            conversations = conversations[1:]
            captions.append(conversation)
            file_name = f'tmp_{len(file_names)}.mp3'
            file_names.append(file_name)
            #generate the audio files
            one_sentence.text_to_speech(conversation, file_name)
            #get the duration audio file
            duration_time = one_sentence.get_duration(file_name)
            duration_times.append(duration_time)
            total_duration += duration_time
        #merge the audio files and captions
        merge_mp3(output_file_name, file_names)
        merge_caption(output_file_name[:-4]+".srt", captions, duration_times)
        #remove the temp files
        for file_name in file_names:
            os.remove(file_name)
        return conversations


if __name__ == "__main__":
    #test conversations_to_speech
    conversations = conversation.get_all_conversation("train.txt")
    utterances = conversation.get_all_utterances(conversations)
    conversations = conversations_to_speech(utterances, "output_a.mp3", 10)
    conversations = conversations_to_speech(conversations[:10], "output_b.mp3")
    

