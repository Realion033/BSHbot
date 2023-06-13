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
bot = commands.Bot(command_prefix="/", intents=intents)

# 대답 딕셔너리--------

#진순 전용 대답
sayhi = {
    "ㅂ": ["질문자1에게 대답1", "질문자1에게 대답2", "질문자1에게 대답3"],
    # 추가적인 질문자와 대답을 여기에 추가
}
bshrijinsun = {
    "레오오오오오우야": ["질문자1에게 대답1", "질문자1에게 대답2", "질문자1에게 대답3"],
    # 추가적인 질문자와 대답을 여기에 추가
}

#일반대답
default_sayhi = ["안녕?", "나는 매우 반가운", "안녕","안녕","안녕","안녕","나는 매우 반가운","나는 안녕을 표하는","안녕"]
bshri = ["저의 다른 본체이기도 하죠!", "-대충 로키 웃는 gif-", "저의 다른 본체이기도 하죠!", "저의 다른 본체이기도 하죠!", "이것은 본체인 나의 다른."]

# 로그인---------
@bot.event
async def on_ready():
    print(f"BSH봇이 활성화되었습니다. 봇 아이디: {bot.user.id}")
    await bot.change_presence(activity=discord.Game(name="*itomi.la"))  # 온라인 상태 메시지 설정

async def on_disconnect():
    await bot.change_presence(activity=discord.Game(name="아크 서바이벌"))  # 오프라인 상태 메시지 설정

# 문답 이벤트--------
@bot.command(aliases=["안녕", "ㅎㅇ", "하이"])
async def hi(ctx):
    author_name = ctx.author.name
    if author_name in sayhi:
        sayhii = random.choice(sayhi[author_name])
    else:
        sayhii = random.choice(default_sayhi)
    await ctx.send(sayhii)

@bot.command(aliases=["배승현", "섹승현", "색승현", "쉑승현", "쇅승현", "쒝승현", "BSH"])
async def bsh(ctx):
    author_name = ctx.author.name
    if author_name in sayhi:
        bshrii = random.choice(bshrijinsun[author_name])
    else:
        bshrii = random.choice(bshri)
        # GIF 응답 전송
        gif_url = "https://media.tenor.com/6IKyOjxLlTQAAAAd/scary-creepy.gif"  # 실제 GIF URL로 교체하세요
        await ctx.send(gif_url)
    await ctx.send(bshrii)

@bot.command(aliases=["날짜"])
async def date(ctx):
    today = datetime.date.today()
    await ctx.send(f"오늘 {today}일이야")

bot.run(get_token())
