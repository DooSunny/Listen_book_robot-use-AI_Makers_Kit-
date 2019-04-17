import stt_tts
import MicrophoneStream as MS
from time import sleep

def stt_roop():
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")
        
        print("text : %s"% text)
        if("끝" in text): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("안녕" in text):
            stt_tts.getText2VoiceStream("그래그래. 인사 그만해두돼.", output_file)
            MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)