from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

url = "https://smartstore.naver.com/thesis_shop/products/4698725205?NaPm=ct%3Dlto35u08%7Cci%3D2517be7fd74c157f647ebe9d29b52f0d23b2d315%7Ctr%3Dnshfu%7Csn%3D676302%7Chk%3D759cbf64e86eda286355c77d668fdbbfc271c728#REVIEW"

# 웹드라이버 초기화 (Chrome을 사용한다고 가정)
driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

# URL로 이동
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기
time.sleep(5)  # 로딩 시간에 따라 조절이 필요할 수 있습니다.

# 페이지의 소스 코드를 가져옴
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 이제 BeautifulSoup 객체를 사용하여 원하는 정보를 추출할 수 있습니다.
results = soup.find_all('span', class_='_2L3vDiadT9')

for result in results:
    print(result)

# 드라이버 종료
driver.quit()
