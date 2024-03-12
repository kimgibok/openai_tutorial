from openai import OpenAI
from dotenv import load_dotenv
import os
from PIL import Image
import requests

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=openai_api_key)
MODEL = "dall-e-3"

client = OpenAI()


response = client.images.generate(
  model=MODEL,
  prompt="오로라 그려줘",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

# 저장파일이름 설정
filename = "image.jpg"

# 이미지 데이터 요청
response = requests.get(image_url)

# 이미지 파일 저장
with open(filename, "wb") as f:
    f.write(response.content)

# 이미지 열기
Image.open(filename)