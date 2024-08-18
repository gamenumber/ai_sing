from gtts import gTTS
import os

def create_voice(text, filename="output.mp3", lang='ko', speed=False):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang=lang, slow=speed)
    
    # 음성을 파일로 저장
    tts.save(filename)
    
    print(f"음성이 '{filename}'로 저장되었습니다.")

# 사용 예시
lyrics = "안녕하세요, 저는 AI 가수입니다. 라라라~"
create_voice(lyrics)