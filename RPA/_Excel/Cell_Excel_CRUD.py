from openpyxl import Workbook
from openpyxl import load_workbook # 파일 불러오기
from random import *
from openpyxl.utils.cell import coordinate_from_string

wb = load_workbook("_Sample_RPA.xlsx")
ws = wb.active # 현재 활성화된 Sheet 활성화

ws.insert_rows(8,5) # 8번째 5줄 추가
ws.insert_cols(2,3) # 2번째 3열이 열이 비워짐. 

#wb.save("_Sample_RPA_C.xlsx")



wb.close()