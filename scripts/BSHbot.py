# bot.py

import discord
from discord.ext import commands
import datetime
import random
import os
import responses as res  # responses 모듈을 res로 축약하여 가져옵니다.

# 토큰 파일 경로 설정
TOKEN_FILE_PATH = os.path.join(os.getcwd(), "token.txt")

# 토큰 불러오기
def load_token():
    with open(TOKEN_FILE_PATH, "r") as file:
        return file.read().strip()

# 봇 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="`", intents=intents)

### 봇 이벤트 및 명령어 ###

@bot.event
async def on_ready():
    print(f"BSH봇이 활성화되었습니다. 봇 아이디: {bot.user.id}")
    await bot.change_presence(activity=discord.Game(name="울트라킬 크랙버전 하는중..."))

@bot.event
async def on_disconnect():
    await bot.change_presence(activity=discord.Game(name="아크 서바이벌"))

# 인사 명령어
@bot.command(aliases=res.greetings_aliases)
async def hi(ctx):
    author_name = ctx.author.name
    if author_name in res.greetings_data["custom"]:
        response = random.choice(res.greetings_data["custom"][author_name])
    else:
        response = random.choice(res.greetings_data["default"])
    await ctx.send(response)

# 배승현 관련 명령어
@bot.command(aliases=res.bsh_aliases)
async def bsh(ctx):
    author_name = ctx.author.name
    if author_name in res.bsh_data["custom"]:
        response = random.choice(res.bsh_data["custom"][author_name])
    else:
        response = random.choice(res.bsh_data["default"])

    # 특정 응답이 GIF일 경우 처리
    if response == "-대충 로키 웃는 gif-":
        await ctx.send(res.bsh_data["gif_url"])
    else:
        await ctx.send(response)

# 날짜 명령어
@bot.command(aliases=res.date_aliases)
async def date(ctx):
    today = datetime.date.today()
    await ctx.send(f"오늘은 {today}일이야")

# 도움말 명령어
@bot.command(aliases=res.help_aliases)
async def helps(ctx):
    await ctx.send(res.HELP_TEXT)

# 봇 실행
bot.run(load_token())
