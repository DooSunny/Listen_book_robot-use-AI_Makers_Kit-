import stt_tts
import MicrophoneStream as MS
from time import sleep

def cloud_bread():#구름빵
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("내리고" in text):
            stt_tts.getText2VoiceStream("밖에 비온다. 주륵주륵.", output_file)
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

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)


def bingle_tiger():#줄줄이꿴호랑이
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("얻어다" in text):
            stt_tts.getText2VoiceStream("괭이로 무엇을 하려고 하는거지?", output_file)
            MS.play_file(output_file)
        
        elif("주렁주렁" in text):
            stt_tts.getText2VoiceStream("참깨로는 무엇을 할까?", output_file)
            MS.play_file(output_file)

        elif("실컷잠" in text):
            stt_tts.getText2VoiceStream("아이의 계획이 무엇일지 너무 궁금해!", output_file)
            MS.play_file(output_file)

        elif("냄새가" in text):
            stt_tts.getText2VoiceStream("우와 게으르지만 영리한 아이였네~!", output_file)
            MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)


def red_tie_lion():#빨간 끈으로 머리를 묶은 사자 
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("정말예" in text):
            stt_tts.getText2VoiceStream("우와 정말 예쁜 끈이네~", output_file)
            MS.play_file(output_file)

        elif("사자는무척" in text):
            stt_tts.getText2VoiceStream("사자가 되게 속상하겠다..", output_file)
            MS.play_file(output_file)

        elif("으앙" in text):
            stt_tts.getText2VoiceStream("사자야 울지마,,", output_file)
            MS.play_file(output_file)

        elif("묶을수" in text):
            stt_tts.getText2VoiceStream("거미야 고마워~", output_file)
            MS.play_file(output_file)

        elif("오래오래앉아" in text):
            stt_tts.getText2VoiceStream("그래그래. 인사 그만해두돼~~", output_file)
            MS.play_file(output_file)

        elif("안녕" in text):
            stt_tts.getText2VoiceStream("빨간끈으로 머리를 묶으니 사자가 더 예뻐 보여~", output_file)
            MS.play_file(output_file)


    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def always_love_you(): #언제까지나 너를 사랑해
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("" in text):

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def school_way(): #학교 가는 길
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("" in text):

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def funny_eating(): #재미있게 먹는 법
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("" in text):

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def mole_bus(): #두더지 버스
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

		elif("모르는마을"in text):
			stt_tts.getText2VoiceStream("땅속에 마을이 있다고?", output_file)
			MS.play_file(output_file)
		
        elif("짖는모양" in text):
			stt_tts.getText2VoiceStream("우와.", output_file)
			MS.play_file(output_file)

		elif("뛰어든것"in text):
			stt_tts.getText2VoiceStream("왜 그러니??", output_file)
			MS.play_file(output_file)

		elif("엄청빠르거든"in text):
			stt_tts.getText2VoiceStream("큰일이야", output_file)
			MS.play_file(output_file)

		elif("보이지않아"in text):
			stt_tts.getText2VoiceStream("어떡하면 좋아.", output_file)
			MS.play_file(output_file)

		elif("대답했어요"in text):
			stt_tts.getText2VoiceStream("다행이다 짝짝짝", output_file)
			MS.play_file(output_file)
		
		elif("받을수있어" in text):
			stt_tts.getText2VoiceStream("나도 죽순 받고싶어!", output_file)
			MS.play_file(output_file)
		
		elif("맛있게먹" in text):
			stt_tts.getText2VoiceStream("평화로운 두더지 버스 이야기네~.", output_file)
			MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def my_father_is_best(): #우리 아빠가 최고야
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("문제없이" in text):
			stt_tts.getText2VoiceStream("멋있는 아빠야!", output_file)
			MS.play_file(output_file)
		
		elif("곰인형" in text):
			stt_tts.getText2VoiceStream("나처럼?", output_file)
			MS.play_file(output_file)

		elif("앞으로도" in text):
			stt_tts.getText2VoiceStream("나도 사랑해", output_file)
			MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

def poof_in_myhead(): #누가 내 머리에 똥쌌어?
    output_file = "testtts.wav"
    text=""
    while True:
        text = stt_tts.getVoice2Text()
        text=text.replace(" ","")

        if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
            break

        elif("소시지같기도" in text):
			stt_tts.getText2VoiceStream("뭘까아?", output_file)
			MS.play_file(output_file)
		
		elif("누구야" in text):
			stt_tts.getText2VoiceStream("누구야", output_file)
			MS.play_file(output_file)

		elif("비둘기에게" in text):
			stt_tts.getText2VoiceStream("비둘기야?", output_file)
			MS.play_file(output_file)

		elif("말에게"in text):
			stt_tts.getText2VoiceStream("말이 범인일까?", output_file)
			MS.play_file(output_file)

		elif("소에게"in text):
			stt_tts.getText2VoiceStream("소가 범인일까?", output_file)
			MS.play_file(output_file)

		elif("내머리에똥" in text):
			stt_tts.getText2VoiceStream("누가 두더지 머리위에 똥을 싼거야!", output_file)
			MS.play_file(output_file)

		elif("개가한짓" in text):
			stt_tts.getText2VoiceStream("강아지 나빠.", output_file)
			MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

