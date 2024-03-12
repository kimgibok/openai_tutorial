from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=openai_api_key)
MODEL = "gpt-3.5-turbo-1106"

client = OpenAI()

user_input = input("후기를 입력하세요:")

response = client.chat.completions.create(
  model=MODEL,
  response_format={ "type": "json_object" },   # json object로 응답하라는 코드가 추가됨
  messages=[
    {"role": "system", "content": "후기를 매우 만족, 만족, 보통, 불만족, 매우 불만족으로 구분해서 분석해줘"},
    {"role": "user", "content": f"{user_input} json"}
  ]
)
print(response.choices[0].message.content)
pass
