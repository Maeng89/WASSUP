#!/usr/bin/env python
# coding: utf-8

# # 전화번호 프로그램 만들기
# 
# * 홍길동 010-123-4567
# * 기능1 : 연락처 추가
# * 기능2 : 연락처 전체 보기
# * 기능3 : 검색, 이름을 입력받아서 전화번호 조회
# * 기능4 : 수정, 이름을 입력받아서 전화번호 입력수정
# * 기능5 : 삭제, 이름 입력받아서 삭제
# * 기능6 : 프로그램 종료

# ## 요구사항 분석 및 설계
# * 요구사항 분석 -> 구체적인 동작을 정의
# * I/O 설계
# * 홍길동, 010-123-4567 -> 딕셔너리  Key : value
# * input을 받아야 되겠구나, str
# * 프로그램 : while 반복
# * 기능 1,2,3,4,5 : if 분기문, 숫자를 입력했을 때 해당 기능이 동작
# * 기능 1 연락처 추가 : dict 추가, dict[key]=value
# * 기능 2 보기 : for문 돌려서 출력
# * 기능 3 조회 : 이름을 입력했을 때 전화번호 출력, dict[key]
# * 기능 4 수정 : dict[key]=value
# * 기능 5 삭제 : del
# * 기능 6 종료 : break
# * 예외처리

# In[9]:


contact = {}

while True:
    print('----- 전화번호부 프로그램 실행 -----')
    print('1.추가    2.보기   3.검색   4.수정   5.삭제   9종료')

    try :
        menu = int(input('메뉴선택'))

        if menu == 1:
            print('연락처 추가 작업 실행')
            new_name = input('이름: ')
            new_tel = input('전화번호: ')
            contact.setdefault(new_name, new_tel)        

        elif menu == 2:
            print('연락처 보기 작업 실행')
            for name, tel in contact.items():
                print(name, ":", tel)

        elif menu == 3:
            print('연락처 검색 작업 실행')
            search_name = input('검색 이름: ')
            print(contact.get(search_name, '없는 연락처입니다.'))
    #         print('---------')
    #         if search_name not in contact:
    #             print('등록되지 않은 이름입니다.')
    #         else : 
    #             print(search_name, ':', contact[search_name])    

        elif menu == 4:
            print('연락처 수정 작업 실행')
            mod_name = input('수정 이름: ')
            # 만약에 연락처 저장소에 수정 이름이 존재하면, 저장소에서 수정해줘 
            if mod_name in contact:
                mod_tel = input('새전화번호: ')
                contact[mod_name] = mod_tel            
            else :
                print('등록되지 않은 이름입니다.')

        elif menu == 5:
            print('연락처 삭제 작업 실행')
            del_name = input('삭제 이름: ')
            # 만약에 연락처 저장소에 삭제 이름이 존재하면, 저장소에서 삭제해줘 
            if del_name in contact:
                del contact[del_name]
            else :
                print('등록되지 않은 이름입니다.')

        elif menu == 9:
            print('연락처 종료 작업 실행')
            break

        else :
            print('잘못된 메뉴 선택입니다.')   
    except :
        print('잘못된 입력입니다.')

