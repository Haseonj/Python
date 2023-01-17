"""
날짜 : 2023/01/16
이름 : 하선주
내용 : 파이썬 네이버 뉴스 크롤링 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# 엑셀파일 생성
workbook = Workbook()
sheet = workbook.active


pg = 1
count = 1

while True:
    # HTML 요청
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&page=%d' % pg # pg: url로 불러온 페이지
    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

    # 엑셀 시트 생성
    #sheetPg = workbook.create_sheet('Page %d' % (pg))

    # print(html)

    # 문서객체 생성
    dom = bs(html, 'html.parser')

    # 문서 현재 페이지
    currentPage = dom.select_one('#main_content > div.paging > strong').text


    if pg != int(currentPage) :
        print('프로그램 종료...')
        break


    # 데이터 파싱
    tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
    print('tit :', tit)

    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

    # 시작 시트에 카테고리를 출력 할 조건문
    """
    if pg == 1 :
        sheetPg.append(['뉴스 카테고리 : %s' % (tit)])
        sheetPg.append([])
        sheetPg.append([])
    """

    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href = tag_a['href']

        # 주저진 시트에 값을 삽입
        """
        sheetPg.append(['뉴스 번호 : %s' % (count)])
        sheetPg.append(['뉴스 제목 : %s' % (title.strip())])
        sheetPg.append(['뉴스 링크 : %s' % (href.strip())])
        sheetPg.append([])
        """
        sheet.append([count, title.strip(), href.strip()])
        print('%d건...'% count)

        print('count :', count)
        print('title :', title.strip())
        print('href :', href.strip())

        # 게시글 번호 처리
        count += 1

    # 엑셀 저장 및 닫기
    workbook.save('C:/Users/java2/Desktop/NaverNews.xlsx')
    workbook.close()

    # 페이지 처리
    pg += 1



