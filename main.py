import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()


def update_votes(votop):
  if "votos" in db.keys():
    votos = db["votos"]
    votos.append(votop)
    db["votos"] = votos
  else:
    db["votos"] = [votop]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
    
  if msg.startswith("$votopaulo"):
    votop=int(msg.split('$votopaulo',1)[1])
    update_votes(votop)
    await message.channel.send("voto computado")

  if msg.startswith("$votohenrique"):
    votoh=int(msg.split('$votohenrique',1)[1])
    update_votes(votoh)
    await message.channel.send("voto computado")  
  
  if msg.startswith("$resultado"):
    if len(db["votos"])==2:
      soma= db["votos"][0]+db["votos"][1]
      if soma>10:
        mensagem="Faremos sim"
      if soma==10:
        mensagem="Empate"
      if soma<10:
        mensagem="Ish...Não vai rolar!"
      await message.channel.send(mensagem)
    else:
      await message.channel.send("há mais de 2 votos")

  if msg.startswith("$deletar"):
    db["votos"]=[]
    await message.channel.send(db["votos"])


  if msg.startswith("$votos"):
    if "votos" in db.keys():
      votos = db["votos"]
    await message.channel.send(votos)



client.run("OTM2ODkyMzkwNTU0MzU3ODIy.YfTzCA.6OL6XTVJqIwV1x12zlVDZcwsVBU")