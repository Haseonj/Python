"""
날짜 : 2023/01/12
이름 : 하선주
내용 : 파이썬 외부 패키지모듈 실습
"""
from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 첫번째 시트 활성화
sheet = workbook.active
sheet.merge_cells('A1:B1')

# 데이터 입력
sheet['A1'] = '파이썬 엑셀 실습'
sheet.append(['a101', '김유신', '010-1234-1001', '25', '김해시'])
sheet.append(['a102', '김춘추', '010-1234-1002', '35', '김해시'])
sheet.append(['a103', '장보고', '010-1234-1003', '45', '김해시'])
sheet.append(['a104', '강감찬', '010-1234-1004', '55', '김해시'])
sheet.append(['a105', '이순신', '010-1234-1005', '65', '김해시'])

# 저장닫기
workbook.save('C:/Users/java2/Desktop/Member.xlsx')
workbook.close()

print('프로그램종료...')