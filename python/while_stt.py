import stt_tts
import MicrophoneStream as MS
from time import sleep

def cloud_bread():#구름빵
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if("끝" in text): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("내리고" in text):
            stt_tts.getText2VoiceStream("우와.", output_file)
            MS.play_file(output_file)

        elif("생길것" in text):
            stt_tts.getText2VoiceStream("기대된다.", output_file)
            MS.play_file(output_file)

        elif("작은구름" in text):
            stt_tts.getText2VoiceStream("뭐야뭐야?.", output_file)
            MS.play_file(output_file)

        elif("조심조심" in text):
            stt_tts.getText2VoiceStream("조심조심.", output_file)
            MS.play_file(output_file)

        elif("동그랗게" in text):
            stt_tts.getText2VoiceStream("음 맛있는냄새~.", output_file)
            MS.play_file(output_file)

        elif("기다릴수가" in text):
            stt_tts.getText2VoiceStream("히잉 맛있을텐데.", output_file)
            MS.play_file(output_file)

        elif("배고플텐데" in text):
            stt_tts.getText2VoiceStream("그러게요.", output_file)
            MS.play_file(output_file)

        elif("잘익은" in text):
            stt_tts.getText2VoiceStream("우와 맛있겠다아.", output_file)
            MS.play_file(output_file)

        elif("아빠한테" in text):
            stt_tts.getText2VoiceStream("좋은 생각이야.", output_file)
            MS.play_file(output_file)

        elif("맛있었습니다" in text):
            stt_tts.getText2VoiceStream("맛있겠다. 나도 구름빵 먹고 싶어.", output_file)
            MS.play_file(output_file)

        elif("안녕" in text):
            stt_tts.getText2VoiceStream("그래그래. 인사 그만해두돼~~", output_file)
            MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)