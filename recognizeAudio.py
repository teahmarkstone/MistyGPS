import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk
# from main import * 


def writeToAudioFile(filename):
    wav_data = misty.getAudioFile(filename)
    decode_string = base64.b64decode(wav_data)
    wav_file = open('temp.wav', 'wb')
    wav_file.write(decode_string)



def recognize_speech_google():
    r = sr.Recognizer()
    with sr.AudioFile('temp.wav') as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
        return text

def recognize_speech_azure(audio_file):
    sub = "382d62b5f9ca4e738cfada7379d8b5f6"
    reg = "eastus"
    # print(reg)
    speech_config = speechsdk.SpeechConfig(subscription=sub, region=reg)
    speech_config.speech_recognition_language="en-US"
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    
    return None