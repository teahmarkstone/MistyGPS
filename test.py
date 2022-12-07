from speech_recognition import recognize_speech

EX1 = "wav_files/TakeMeToTuftsUniversity.wav"
EX2 = "wav_files/LewisHall.wav"
EX3 = "wav_files/Madeline.wav"

text = recognize_speech(EX3)
print(text)