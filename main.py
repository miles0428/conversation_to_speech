import google.cloud.texttospeech as tts
from google.oauth2 import service_account
import os
from pydub import AudioSegment

def text_to_speech(text : str, file_name : str, key :str = 'key.json' ) -> None:
    '''
    convert a chinese text to speech and save it to file_name in mp3 format
    use google cloud text to speech api
    
    Args:
        text : the text to be converted
        file_name : the name of the mp3 file to be saved
        key : the path of the key file

    Return:
        None
    '''
    credentials = service_account.Credentials.from_service_account_file(key)

    client = tts.TextToSpeechClient(credentials=credentials)
    # Set the text input to be synthesized
    synthesis_input = tts.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = tts.VoiceSelectionParams(
        language_code="cmn-TW",
        name='cmn-TW-Standard-A'
    )

    # Select the type of audio file you want returned
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("temp.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)

    #add a 1 sec silence to the end of the file
    temp = AudioSegment.from_mp3("temp.mp3")
    temp = temp + AudioSegment.silent(duration=1000)
    temp.export(file_name, format="mp3")
    #rm temp file
    os.remove("temp.mp3")

def get_duration(file_name : str) -> int:
    '''
    return the duration of the mp3 file in ms

    Args:
        file_name : the name of the mp3 file

    Return: 
        the duration of the mp3 file in ms
    '''
    temp = AudioSegment.from_mp3(file_name)
    duration = len(temp)
    return duration

def generate_srt_style_text(
        text : str,
        start_time : int,
        end_time : int,
        index : int
        ) -> str:
    '''
    generate a srt style text with the given text, start time, end time and index
    
    Args:
        text : the text to be converted
        start_time : the start time of the text in ms
        end_time : the end time of the text in ms
        index : the index of the text
    
    Return:
        a srt style text
    '''
    #convert ms to srt style time
    start_time = f'{start_time//1000:02}:{start_time%1000:03}'
    end_time = f'{end_time//1000:02}:{end_time%1000:03}'
    #generate srt style text
    result = f'{index}\n'
    result += f'{start_time} --> {end_time}\n'
    result += f'{text}\n\n'
    return result

if __name__ == "__main__":
    text = "刹车不是最好的方案，他强行掉头搞不好就是没看到后面来车，继续掉会直接碾过来 … 逃脱才是最佳方案。"
    file_name = "test.mp3"
    text_to_speech(text, file_name)
    print(f'the duration of {text} is {get_duration(file_name)} ms')
    os.remove(file_name)


    



