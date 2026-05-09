import requests
from DATABASEINFO import DB
import math as m

NDB = DB()

headers = {
    "Authorization": "Bearer " + NDB.TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2026-03-11" # 최신 버전 확인 권장
}


def create_page(description, date, n1, n2): # status 기본값 설정
    create_url = "https://api.notion.com/v1/pages"
    
    data = {
        "parent": { "database_id": NDB.ID },
        "properties": {
            "이름": {
                "title": [
                    { "text": { "content": description } }
                ]
            },
            "날짜": {
                "date": { "start": date }
            },
            "숫자": {
                "number": n1
            },
            "숫자1": {
                "number": n2
            },
            "숫자2": {
                "number": (m.sqrt(n1) + m.cos(n2))
            }
            
        }
    }
    
    response = requests.post(create_url, headers=headers, json=data)
    
    # 수정된 부분: .status_code 사용
    if response.status_code == 200:
        print(f"'{description}' 데이터 업로드 성공!")
    else:
        print(f"오류 발생: {response.status_code}")
        print(response.text)

# 실행 예시
create_page("파이썬 공부하기", "2026-05-10", 3, m.pi/2)
