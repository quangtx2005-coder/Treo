import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot Discord đang hoạt động 24/24!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã online 24/24 dưới tên: {bot.user.name} (ID: {bot.user.id})")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"Pong! Độ trễ: {round(bot.latency * 1000)}ms")

if __name__ == "__main__":
    keep_alive()
    TOKEN = "MTU3MzE2ODA2NTk1OTY5MDM5Mg.G5jks4.qfjSL4iX4qjpE5WydtaVn64XEm24zGO42rwQ3I"
    bot.run(TOKEN)