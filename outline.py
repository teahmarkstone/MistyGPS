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

def startSequence():
    misty.speak("Hi, I'm Misty. I'm here to help you get to wherever you need to go on Tufts' campus. Just state the name of the place you want to go after you hear the beep and I'll give you accurate directions.")
    #could also not do beep and instead say when you see the blue light speak?
    misty.playAudio()
    recognizePlace()

def recognizePlace():
    text = recognize_speech_google()
    time.sleep(5) 
    location = 'Tufts ' + namedEntityRecognition(text)
    checkDestination(location)
    
def checkDestination(location):
    misty.speak(f"Okay, I will get you directions to {location}. Does that sound okay? Please say yes or no.")
    #does this return a str?
    user_response = recognize_speech_google()
    if user_response == "No":
        misty.speak("I'm sorry. Maybe, I heard you wrong. Can you once again state the name of the place that you want to go?")
        recognizePlace()
    elif user_response == "Yes":
        misty.speak(f"Awesome, I'll get you directions to {location}")
        get_directions(location)
        #repeat end sequence function
        endSequence()

    else:
        misty.speak("I'm sorry. I didn't quite get that. Can you once again state the name of the place you want to go?")
        recognizePlace()
    
def endSequence():
    misty.speak("I'm happy that I was able to help you today. Is there any other place that you need directions to? Please state yes or no.")
    user_response = recognize_speech_google()
    if user_response == "No":
        misty.speak("Well alright, I'm happy that I was able to help. Goodbye and good luck on your journey!")
    if user_response == "Yes":
        misty.speak("Awesome, I'm excited to help. Please state the name of the next place that you want to go to.")
        recognizePlace()








    

    











    




