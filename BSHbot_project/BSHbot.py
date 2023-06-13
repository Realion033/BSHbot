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

# 대답 리스트
sayhi = ["안녕하세요!", "반갑습니다!", "안녕하십니까!"]
bshri = ["저의 다른 본체이기도 하죠!", "-대충 로키 웃는 gif-", "저의 다른 본체이기도 하죠!", "저의 다른 본체이기도 하죠!"]

# 로그인
@bot.event
async def on_ready():
    print(f"BSH봇 출격 완료... 봇 아이디: {bot.user.id}")

# 문답 이벤트
@bot.command(aliases=["안녕", "ㅎㅇ", "하이"])
async def hi(ctx):
    sayhii = random.choice(sayhi)
    await ctx.send(sayhii)

@bot.command(aliases=["배승현", "섹승현", "색승현", "쉑승현", "쇅승현", "쒝승현", "BSH"])
async def bsh(ctx):
    bshrii = random.choice(bshri)
    await ctx.send(bshrii)

@bot.command(aliases=["날짜"])
async def date(ctx):
    today = datetime.date.today()
    await ctx.send(f"오늘 날짜는 {today}입니다.")

bot.run(get_token())
