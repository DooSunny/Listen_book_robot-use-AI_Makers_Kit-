import stt_tts
import MicrophoneStream as MS
from time import sleep

#1
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
            stt_tts.getText2VoiceStream("음. 맛있는냄새~.", output_file)
            MS.play_file(output_file)

        elif("기다릴수가" in text):
            stt_tts.getText2VoiceStream("히잉. 맛있을텐데.", output_file)
            MS.play_file(output_file)

        elif("배고플텐데" in text):
            stt_tts.getText2VoiceStream("그러게요.", output_file)
            MS.play_file(output_file)

        elif("잘익은" in text):
            stt_tts.getText2VoiceStream("우와. 맛있겠다아.", output_file)
            MS.play_file(output_file)

        elif("아빠한테" in text):
            stt_tts.getText2VoiceStream("좋은 생각이야.", output_file)
            MS.play_file(output_file)

        elif("맛있었습니다" in text):
            stt_tts.getText2VoiceStream("맛있겠다. 나도 구름빵 먹고 싶어.", output_file)
            MS.play_file(output_file)

    stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)


#2
def eat_compliment(): #칭찬 먹으러 가요?
	output_file = "testtts.wav"
	text=""
	while True:
		text = stt_tts.getVoice2Text()
		text=text.replace(" ","")

		if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
			break

		elif("생일카드" in text):
			stt_tts.getText2VoiceStream("우와, 아빠께서 좋으시겠다.", output_file)
			MS.play_file(output_file)

		elif("등산으로" in text):
			stt_tts.getText2VoiceStream("가족 등산 부럽다..", output_file)
			MS.play_file(output_file)
				
		elif("출발하자" in text):
			stt_tts.getText2VoiceStream("세시간이나 걸리는 구나..", output_file)
			MS.play_file(output_file)

		elif("크게소리" in text):
			stt_tts.getText2VoiceStream("위험해", output_file)
			MS.play_file(output_file)

		elif("모두털썩" in text):
			stt_tts.getText2VoiceStream("지원아, 병관아 조금만 더 힘을 내", output_file)
			MS.play_file(output_file)

		elif("뒤따라오던아저씨" in text):
			stt_tts.getText2VoiceStream("힘내", output_file)
			MS.play_file(output_file)

		elif(("한줄" in text) and ("올라" in text)):
			stt_tts.getText2VoiceStream("조심, 조심", output_file)
			MS.play_file(output_file)

		elif(("기분" in text) and ("으쓱" in text)):
			stt_tts.getText2VoiceStream("지원이와 병관이, 대단해", output_file)
			MS.play_file(output_file)


	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)
    

#3
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


#4
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

#5
def always_love_you(): #언제까지나 너를 사랑해
	output_file = "testtts.wav"
	text=""
	while True:
		text = stt_tts.getVoice2Text()
		text=text.replace(" ","")

		if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
			break

		elif("" in text):
			pass

	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

#6
def school_way(): #학교 가는 길
	output_file = "testtts.wav"
	text=""
	while True:
		text = stt_tts.getVoice2Text()
		text=text.replace(" ","")

		if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
			break
		
		elif(("머리카락" in text) and ("눈동자" in text) and ("친구" in text)):
			stt_tts.getText2VoiceStream("누굴까아?", output_file)
			MS.play_file(output_file)
		
		elif("아주많을" in text):
			stt_tts.getText2VoiceStream("우와, 말을 탈 수 있다니 되게 부러워.", output_file)
			MS.play_file(output_file)

		elif(("힘들지않습니다"in text) and ("선생님" in text)):
			stt_tts.getText2VoiceStream("중국의 친구들은 다같이 등교를 하는구나.", output_file)
			MS.play_file(output_file)

		elif("시원한아이스크림"in text):
			stt_tts.getText2VoiceStream("터키아이스크림 나도 먹고싶다.", output_file)
			MS.play_file(output_file)

		elif("무엇일까요" in text):
			stt_tts.getText2VoiceStream("무엇일까???", output_file)
			MS.play_file(output_file)

		elif("페달을밟으며"in text):
			stt_tts.getText2VoiceStream("열심히 페달을 밟아서 일등하자.", output_file)
			MS.play_file(output_file)

		elif("언제나즐거워요"in text):
			stt_tts.getText2VoiceStream("프랑스의 등굣길은 낭만적이구나.", output_file)
			MS.play_file(output_file)

		elif("기린가족" in text):
			stt_tts.getText2VoiceStream("케냐의 친구들은 기린을 보면서 등교 하는구나.", output_file)
			MS.play_file(output_file)
 
		elif("내일또그리면"in text):
			stt_tts.getText2VoiceStream("우와 정말 아름다울것 같아", output_file)
			MS.play_file(output_file)

		elif("왕이된것처럼"in text):
			stt_tts.getText2VoiceStream("우와 코끼리를 타고 등교를 하다니 대단해.", output_file)
			MS.play_file(output_file)

		elif("무에타이선수"in text):
			stt_tts.getText2VoiceStream("무에타이라니 멋있어.", output_file)
			MS.play_file(output_file)

		elif("자꾸자꾸"in text):
			stt_tts.getText2VoiceStream("부모님을 돕는 착한 아이구나.", output_file)
			MS.play_file(output_file)

		elif("멀리던지기시합"in text):
			stt_tts.getText2VoiceStream("멋있다. 부메랑 던지기!", output_file)
			MS.play_file(output_file)

		elif("아름다워요"in text):
			stt_tts.getText2VoiceStream("키리바시의 등굣길은 굉장히 아름답겠구나", output_file)
			MS.play_file(output_file)

		elif("나쁜꿈"in text):
			stt_tts.getText2VoiceStream("동생을 위해 드림캐처를 걸어주다니. 착한 친구구나.", output_file)
			MS.play_file(output_file)
	
		elif("편해지거든요"in text):
			stt_tts.getText2VoiceStream("나도 비가 좋아!", output_file)
			MS.play_file(output_file)

		elif(("아름다운"in text)and("학교가는길"in text)):
			stt_tts.getText2VoiceStream("오로라가 등굣길을 비춰준다니 굉장히 아름다울 것 같아", output_file)
			MS.play_file(output_file)

		elif("뭉게구름" in text):
			stt_tts.getText2VoiceStream("너는 무엇이 되고싶니?", output_file)
			MS.play_file(output_file)

		elif("캠프는지금부터"in text):
			stt_tts.getText2VoiceStream("우와 지구촌 아이들의 학교 가는 길은 굉장히 다양하구나", output_file)
			MS.play_file(output_file)

	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

#7
def funny_eating(): #재미있게 먹는 법
	output_file = "testtts.wav"
	text=""
	while True:
		text = stt_tts.getVoice2Text()
		text=text.replace(" ","")

		if(("끝" in text) or ("그만" in text)): #잘들었어,재밌었어,다음에 또 읽어줘 
			break

		elif(("당근"in text and ("앞니"in text))):
			stt_tts.getText2VoiceStream("아삭아삭 어석어석", output_file)
			MS.play_file(output_file)

		elif("캠프는지금부터"in text):
			stt_tts.getText2VoiceStream("우와 지구촌 아이들의 학교 가는 길은 굉장히 다양하구나", output_file)
			MS.play_file(output_file)

		elif(("입을"in text)and("풀과채소"in text)):
			stt_tts.getText2VoiceStream("아작아작 우적우적", output_file)
			MS.play_file(output_file)

		elif("곰한마리"in text):
			stt_tts.getText2VoiceStream("우와 곰이다.", output_file)
			MS.play_file(output_file)

		elif(("새우"in text)and("먹어"in text)):
			stt_tts.getText2VoiceStream("어머나", output_file)
			MS.play_file(output_file)

		elif("숲에거인"in text):
			stt_tts.getText2VoiceStream("우와 거인이다", output_file)
			MS.play_file(output_file)

		elif(("한입에"in text)and("먹었어"in text)):
			stt_tts.getText2VoiceStream("아작아작 쩝쩝 어적어적 쩝쩝", output_file)
			MS.play_file(output_file)

		elif("잘먹었다"in text):
			stt_tts.getText2VoiceStream("모두들 배부르게 밥을 먹어서 기뻐", output_file)
			MS.play_file(output_file)

	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

#8
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
		
		elif("모양이에요" in text):
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
			stt_tts.getText2VoiceStream("다행이다. 짝짝짝", output_file)
			MS.play_file(output_file)
		
		elif("받을수있어" in text):
			stt_tts.getText2VoiceStream("나도 죽순 받고싶어!", output_file)
			MS.play_file(output_file)
		
		elif("맛있게먹" in text):
			stt_tts.getText2VoiceStream("평화로운 두더지 버스 이야기네~.", output_file)
			MS.play_file(output_file)

	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)

#9
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

#10
def poof_in_myhead(): #누가 내 머리에 똥쌌어?
	output_file = "testtts.wav"
	text=""
	while True:
		text = stt_tts.getVoice2Text()
		text=text.replace(" ","")

		if("그만" in text): #잘들었어,재밌었어,다음에 또 읽어줘 
			break

		elif("소시지같기도" in text):
			stt_tts.getText2VoiceStream("뭘까아?", output_file)
			MS.play_file(output_file)
		
		elif("아무도찾을수" in text):
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

		elif("기분좋게" in text):
			stt_tts.getText2VoiceStream("그래도 두더지 머리위에 똥을 싼 범인을 찾게되어서 다행이야.",output_file)
			MS.play_file(output_file)

	stt_tts.getText2VoiceStream("잘들었어. 다음에 또 읽어줘.", output_file)
