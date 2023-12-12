from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import math, time, pandas as pd

options = Options()
options.add_argument('--window-size=974,1047')
options.add_argument('--window-position=953,0')
options.add_experimental_option("detach", True)

search = input('검색어:')
cnt = int(input('스크래핑 할 건수는 몇건입니까?: '))
page_cnt = math.ceil(cnt / 10)  # 크롤링 할 전체 페이지 수 

URL = 'https://korean.visitkorea.or.kr/search/search_list.do?keyword='+search
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(2)

# 여행기사 더보기 클릭
driver.find_element(By.CSS_SELECTOR, "#s_recommend > .more_view > a").click()

title_list = []
contents_list = []

def page_work():
    result = driver.find_elements(By.CSS_SELECTOR,'#search_result .tit>a')
    global contents_no, cnt
    global title_list, contents_list
    
    for item in result:
        contents_no += 1
        
        if contents_no <= cnt :    
            print(f'[콘텐츠 {contents_no}]')  
            item.send_keys(Keys.ENTER) # .click()은 에러 잘남

            time.sleep(2)
            html = driver.page_source
            html_dom = BeautifulSoup(html, 'lxml')

            title = html_dom.find(id='topTitle')
            title_list.append(title.text)
            print(title.text)
            
            contents = driver.find_elements(By.CLASS_NAME, 'txt_p')
            contents_merge = ' '.join([item.text for item in contents])        
            contents_list.append(contents_merge)
            
            driver.back()
            time.sleep(2)     


contents_no = 0
today = time.localtime()
print('스크래핑 프로그램 실행')

for page_no in range(1, page_cnt+1):    
    print(f'====== {page_no} 페이지 스크래핑 시작 ======')
    page_work()
    print(f'====== {page_no} 페이지 스크래핑 완료 ======')
    
    DF = pd.DataFrame({"제목":title_list, "내용":contents_list})
    filename = f'{search}여행기사_{cnt}건_{today.tm_year}{today.tm_mon}{today.tm_mday}.xlsx'
    DF.to_excel(filename)
    print(f'====== {page_no} 페이지 {filename}파일 저장 완료 ======')
    
    if page_no < page_cnt:
        driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[15]/a[{page_no+1}]').click()
        time.sleep(2)
                   
                   
print('스크래핑 프로그램 종료')
driver.close()