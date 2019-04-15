import stt_tts
import MicrophoneStream as MS

def main():
	output_file = "testtts.wav"
	text=""
	while True :
		test_return = stt_tts.test()

		if(int(test_return) == 200):
			text = stt_tts.getVoice2Text()
			text=text.replace(" ","")
			print("text : %s"%text)

		text = text.encode("utf-8")
		# print("type : %s" %type(text))

		if("안녕" in text):
			stt_tts.getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)
		elif("이름" in text):
			stt_tts.getText2VoiceStream("제 이름은 기가지니입니다.", output_file)
		else:
			stt_tts.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)
		text=""

if __name__ == '__main__':
	main()