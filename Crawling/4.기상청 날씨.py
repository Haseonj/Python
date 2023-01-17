"""
날짜 : 2023/01/17
이름 : 하선주
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                user='root',
                password='1234', 
                db='java2db', 
                charset='utf8')

cur = conn.cursor()

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    sql = "insert into `Weather` values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NOW())"

    print('지역 :', tds[0].text)
    cur.execute(sql % (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text, tds[12].text, tds[13].text))
    conn.commit()

# 가상 브라우저 종료
browser.close()

# DB 종료
conn.close()
print('프로그램 종료...')