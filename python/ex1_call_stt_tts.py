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
			stt_tts.getText2VoiceStream("안녕. 반가워.", output_file)

		# "읽는다" 하였을때 호출어없이 sst만 동작
		elif("구름빵" in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.", output_file)
			MS.play_file(output_file)
			while_stt.cloud_bread()

		elif("호랑이" in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.", output_file)
			MS.play_file(output_file)
			while_stt.bingle_tiger()

		elif("사자 " in text and (("읽을" in text) or ("읽어" in text))):
			stt_tts.getText2VoiceStream("듣기모드를 실행할게.", output_file)
			MS.play_file(output_file)
			while_stt.red_tie_lion()

		else:
			stt_tts.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)

if __name__ == '__main__':
	main()