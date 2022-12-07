# speech recognition for misty using Microsoft Azure Cognitive Services
# inp: .wav audio file
# outp: str text
import os
import azure.cognitiveservices.speech as speechsdk

def recognize_speech(audio_file):
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

