import fortnitepy
import json
from fortnitepy.ext import commands

with open("device_auths.json","r",encoding="UTF-8") as f:
    device_auth = json.load(f)

bot = commands.Bot(command_prefix='!',auth=fortnitepy.DeviceAuth(device_auth['device_id'],device_auth['account_id'],device_auth['secret'],case_insensitive=True))

#起動
@bot.event
async def event_ready():
    print(f"アカウント '{bot.user.display_name}' にログインしました")

#フレンドリクエスト
@bot.event
async def event_friend_request(request):
    await request.accept()

#hello 名前
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"こんにちは {ctx.author.display_name} さん。")

bot.run()
