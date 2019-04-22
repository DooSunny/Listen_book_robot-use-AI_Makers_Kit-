import stt_tts
import MicrophoneStream as MS
from time import sleep
import while_stt

def main():
	output_file = "testtts.wav"
	text=""
	while True :
		text=stt_tts.Call()

		if("안녕" in text):
			stt_tts.getText2VoiceStream("안녕. 반가워.",output_file)

		# "읽는다" 하였을때 호출어없이 sst만 동작
		
		#1 #구름빵
		elif("구름빵" in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.cloud_bread()

		#2 #칭찬 먹으러 가요?
		elif("칭찬먹으러"in text and(("읽을"in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.eat_compliment()
		
		#3 #줄줄이꿴호랑이
		elif("호랑이" in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.bingle_tiger()

		#4 #빨간 끈으로 머리를 묶은 사자 
		elif("사자 " in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.red_tie_lion()
		
		#6 #학교 가는 길
		elif(("학교" in text) and (("읽을"in text) or ("읽어" in text))) :
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.school_way()

		#7 #재미있게 먹는 법
		elif(("재미있게" in text) and (("읽을" in text ) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.funny_eating()

		#8 #두더지 버스
		elif(("두더지" in text) and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.mole_bus()

		#9 #우리 아빠가 최고야
		elif(("우리아빠" in text) and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.my_father_is_best()
		
		#10 #누가 내 머리에 똥쌌어?
		elif(("내머리에똥" in text) and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.",output_file)
			MS.play_file(output_file)
			while_stt.poof_in_myhead()

		else:
			stt_tts.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)

if __name__ == '__main__':
	main()