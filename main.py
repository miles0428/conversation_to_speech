"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import google.cloud.texttospeech as tts
from google.oauth2 import service_account
import pydub
from pydub import AudioSegment

# AudioSegment.converter = r"ffmpeg-2023-06-15-git-41229ef705-essentials_build/bin/ffmpeg.exe"
# AudioSegment.ffprobe = r"ffmpeg-2023-06-15-git-41229ef705-essentials_build/bin/ffprobe.exe"


# Instantiates a client

credentials = service_account.Credentials.from_service_account_file('key.json')

client = tts.TextToSpeechClient(credentials=credentials)

text = "刹车不是最好的方案，他强行掉头搞不好就是没看到后面来车，继续掉会直接碾过来 … 逃脱才是最佳方案。"
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
temp.export("temp.mp3", format="mp3")


