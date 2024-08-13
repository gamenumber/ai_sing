from google.cloud import texttospeech

# 클라이언트 생성
client = texttospeech.TextToSpeechClient()

# 텍스트 입력
input_text = texttospeech.SynthesisInput(text="안녕하세요, 만나서 반갑습니다!")

# 음성 설정
voice = texttospeech.VoiceSelectionParams(
    language_code="ko-KR",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# 오디오 설정
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# 음성 합성 요청
response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)

# 음성 파일 저장
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
