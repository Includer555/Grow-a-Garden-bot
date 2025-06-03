import discord
import os
import pyautogui

bought_items_file = "BoughtItemCount.txt"

#DiscordBot TOKEN
TOKEN_PATH = "C:/Users/Levi/Desktop/discordbottoken.txt"

f = open(TOKEN_PATH, "r")
TOKEN = f.read()
f.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!screenshot':
        for i in range(9): 
            screenshot_path = "Screenshot"+str(i)+".png"
            await message.channel.send(file=discord.File(screenshot_path))
        await message.channel.send("------------------------------------")
    
    if message.content == '!boughtitems':
        f = open(bought_items_file, "r")
        items = f.read()
        f.close()
        for i in range(int(items)): 
            screenshot_path = "BoughtItem"+str(i)+".png"
            await message.channel.send(file=discord.File(screenshot_path))
        await message.channel.send("------------------------------------")

client.run(TOKEN)