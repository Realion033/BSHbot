# responses.py

# 인사 대답 데이터
greetings_data = {
    "default": [
        "안녕?", 
        "나는 매우 반가운", 
        "안녕", 
        "나는 안녕을 표하는"
    ],
    "custom": {
        "레오오오오오우야": [
            "오.. 진후가 나한테 인사했어", 
            "진순아 안녕", 
            "와 진후야 안녕"
        ],
    }
}

# 배승현 관련 대답 데이터
bsh_data = {
    "default": [
        "나는 로봇이 되어버린", 
        "-대충 로키 웃는 gif-", 
        "큭...큭소", 
        "이것은 나의 -본체-", 
        "이것은 본체인 나의 다른."
    ],
    "custom": {
        "레오오오오오우야": [
            "질문자1에게 대답1", 
            "질문자1에게 대답2", 
            "질문자1에게 대답3"
        ],
    },
    "gif_url": "https://media.tenor.com/6IKyOjxLlTQAAAAd/scary-creepy.gif"
}

# 도움말 텍스트
HELP_TEXT = "모든 명령어는 `로 시작합니다. 현재 구현된 명령어는 [hello, bsh(배승현이름관련), date, h] 입니다."

# 인사 명령어
greetings_aliases = ["안녕", "ㅎㅇ", "하이", "hello"]

# 배승현 관련 명령어
bsh_aliases = ["배승현", "슘슘이", "BSH", "배", "승현", "배승"]

# 날짜 관련 명령어
date_aliases = ["날짜"]

# 도움말 명령어
help_aliases = ["h", "도움", "?"]
