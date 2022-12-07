from Python_SDK.mistyPy.Robot import Robot
from Python_SDK.mistyPy.Events import Events

from speech_recognition import recognize_speech


MISTY_02944 = "10.245.158.6"
MISTY_02955 = "10.245.145.99"
MISTY_02855 = "10.245.155.168"

def start_skill():
    misty.register_event(Events.TextToSpeechComplete, "initTTSComplete", keep_alive=False, callback_function=tts_intro_completed)

    print("registered")
    misty.display_image("e_defaultcontent.jpg")
    print("displayed")
    misty.move_head(0, 0, 0, 85)
    misty.set_default_volume(5)
    misty.speak("Hello I am Misty. Where would you like to go?", None, None, None, True, "tts-content")
    print("spoke")

def tts_intro_completed(event):
    print("In tts complete")
    misty.register_event(Events.VoiceRecord, "VoiceRecord", callback_function=voice_record_complete)

    # curr_message = misty.capture_speech_azure(overwriteExisting=False,
    #                                           silenceTimeout=None,
    #                                           maxSpeechLength=4000,
    #                                           requireKeyPhrase=False,
    #                                           captureFile=True,
    #                                           speechRecognitionLanguage= "en-us",
    #                                           azureSpeechKey= "382d62b5f9ca4e738cfada7379d8b5f6",
    #                                           azureSpeechRegion="eastus")
    
    curr_message = misty.capture_speech(overwriteExisting=True, silenceTimeout=None, requireKeyPhrase=False)
    print("audio record done")

def voice_record_complete(event):
    print("recognizing audio...")
    var = misty.play_audio(fileName="capture_Dialogue.wav")
    speech = recognize_speech("capture_Dialogue.wav")
    print("You said: ", speech)
    misty.speak(("You said " + speech), None, None, None, True, "tts-content")

    print("You said: ", speech)
    # if "message" in event:
    #     parsed_message = event["message"]
    #     print(parsed_message)
    #     misty_heard = parsed_message["speechRecognitionResult"]
    #     print(f"Misty heard: {misty_heard}")
    print("...done.")
        
if __name__ == "__main__":
    misty = Robot(MISTY_02855)
    print("robot made")
    start_skill()
