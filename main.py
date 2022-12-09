import base64
from geo import *
from recognizeAudio import *
from entityRecognizer import *
# from os import path
from mistyFunctions import * 


misty = Robot('10.245.145.216') # This is the IP of my misty. Replace with your IP


filename = 'capture_Dialogue.wav'
misty.changeLED(255, 255, 255)

# misty.speak('Hello my name is Misty')


misty.recordAudio()
time.sleep(5)

def writeToAudioFile(filename):
    wav_data = misty.getAudioFile(filename)
    decode_string = base64.b64decode(wav_data)
    wav_file = open('temp.wav', 'wb')
    wav_file.write(decode_string)


writeToAudioFile(filename)

text = recognize_speech_google()


location = 'Tufts ' + namedEntityRecognition(text)
directions = get_directions(location)
print(location)
print(directions)


