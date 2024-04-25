import discord
from discord.ext import commands
import datetime
import random
import os

# 토큰 파일 경로 설정
token_file = os.path.join(os.getcwd(), "token.txt")
print(token_file)

# 토큰 불러오기
def get_token():
    with open(token_file, "r") as file:
        token = file.read().strip()
    return token

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
#명령 딕셔너리
askhi = ["안녕", "ㅎㅇ", "하이", "hello"]

# 대답 딕셔너리
sayhi = {
    "레오오오오오우야": ["오.. 진후가 나한테 인사했어", "진순아 안녕", "와 진후야 안녕"],
    # 추가적인 질문자와 대답을 여기에 추가
}
bshrijinsun = {
    "레오오오오오우야": ["질문자1에게 대답1", "질문자1에게 대답2", "질문자1에게 대답3"],
    # 추가적인 질문자와 대답을 여기에 추가
}

# 일반 대답
helpq = "모든 명령어는 `로 시작합니다. 현재 구현된 명령어는 [hello, bsh(배승현이름관련), date, h] 입니다."
default_sayhi = ["안녕?", "나는 매우 반가운", "안녕", "안녕", "안녕", "안녕", "나는 매우 반가운", "나는 안녕을 표하는", "안녕"]
bshri = ["나는 로봇이되어버린", "-대충 로키 웃는 gif-", "큭...큭소", "이것은 나의 -본체-", "이것은 본체인 나의 다른."]

# 로그인
@bot.event
async def on_ready():
    print(f"BSH봇이 활성화되었습니다. 봇 아이디: {bot.user.id}")
    await bot.change_presence(activity=discord.Game(name="*itomi.la"))  # 온라인 상태 메시지 설정

@bot.event
async def on_disconnect():
    await bot.change_presence(activity=discord.Game(name="아크 서바이벌"))  # 오프라인 상태 메시지 설정

# 문답 이벤트
@bot.command(aliases=askhi)
async def hi(ctx):
    author_name = ctx.author.name
    if author_name in sayhi:
        sayhii = random.choice(sayhi[author_name])
    else:
        sayhii = random.choice(default_sayhi)
    await ctx.send(sayhii)

@bot.command(aliases=["배승현", "섹승현", "색승현", "쉑승현", "쇅승현", "쒝승현", "BSH","배","승현","배승"])
async def bsh(ctx):
    author_name = ctx.author.name
    if author_name in sayhi:
        bshrii = random.choice(bshrijinsun[author_name])
    else:
        bshrii = random.choice(bshri)
        
    if bshrii == "-대충 로키 웃는 gif-":
        # GIF 응답 전송
        gif_url = "https://media.tenor.com/6IKyOjxLlTQAAAAd/scary-creepy.gif"  # 실제 GIF URL로 교체하세요
        await ctx.send(gif_url)
    else:
        await ctx.send(bshrii)

@bot.command(aliases=["날짜"])
async def date(ctx):
    today = datetime.date.today()
    await ctx.send(f"오늘 {today}일이야")

@bot.command(aliases=["h", "도움", "?"])
async def helps(ctx):
    await ctx.send(helpq)

bot.run(get_token())
