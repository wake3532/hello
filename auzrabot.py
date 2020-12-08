import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["모든 비트코인 구매 : 센트럴젠비코자판기.kro.kr ", "모두들 환영합니다 구매는 : 센트럴젠비코자판기.kro.kr " , "코로나 의심시 1339 " , "코로나 2.5단계 의심시 전화를 해야합니다 😨"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)


@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'모두들 환영해주세요 🎃',
            description=f'{member}님 환영해요. 메리크리스마스 ! \n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None
@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'왜 나가요 😭',
            description=f'{member}님이 센트럴젠을 나갔습니다 😭 \n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None