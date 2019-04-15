import stt_tts
import MicrophoneStream as MS

def main():
	output_file = "testtts.wav"
	text=""
	while True :
		test_return = stt_tts.test() 		#호출어 부르는함수는 호출되었을때 200 을 반환한다

		if(int(test_return) == 200): 		#호출어 부르는함수의 반한값이 200일경우 아래와 같은 함수를 실행한다
			text = stt_tts.getVoice2Text() 	#sst 함수를 실행하고 받아온 값을 text변수안에 넣는다
			text=text.replace(" ","") 		#받아온 text변수안에 공백을 완전히 제거 해준다
			print("text : %s"%text)

		text = text.encode("utf-8")
		# print("type : %s" %type(text))

		if("안녕" in text):
			stt_tts.getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)

		elif(("읽을" in text) or("읽어" in text)):
			stt_tts.getText2VoiceStream("오, 재밌겠네여 어서 읽어주세요. 듣기모드를 실행합니다", output_file)
			
			while True:
				text = stt_tts.getVoice2Text()
				text=text.replace(" ","")

		else:
			stt_tts.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)
		text=""

if __name__ == '__main__':
	main()