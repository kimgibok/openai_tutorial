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

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content)
pass



# want_to = """너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
# content
# {}
# """
# content="오늘 아침은 없고 점심은 치킨이야 그리고 저녁은 철판삼겹구이야"

# # GPT에게 질문하고 응답 받는 함수
# def ask_to_gpt(messages):
#     response = client.chat.completions.create(
#         model=MODEL,
#         top_p=0.1,
#         temperature=0.1,
#         messages=messages,
#     )

#     return response.choices[0].message.content

# messages=[
#         {'role': 'system', 'content': want_to.format(content)},
#     ]

# user_input = input('You: ')

# messages.append(
#         {'role': 'user', 'content': user_input},
#     )

# response = ask_to_gpt(messages)

# print(response)