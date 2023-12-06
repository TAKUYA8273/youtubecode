import fortnitepy
import json
from fortnitepy.ext import commands
import asyncio
import aiohttp

with open("device_auths.json","r",encoding="UTF-8") as f:
    device_auth = json.load(f)

bot = commands.Bot(command_prefix='!',auth=fortnitepy.DeviceAuth(device_auth['device_id'],device_auth['account_id'],device_auth['secret'],case_insensitive=True))

#起動時の動作
@bot.event
async def event_ready():
    # await fortnitepy.ClientPartyMember.set_outfit(asset=str("CID_028_Athena_Commando_F"))
    print(f"{bot.user.display_name}にログインしました")
    print("起動完了！")
    

#フレンドリクエスト時の動作
@bot.event
async def event_friend_request(request):
    await request.accept()

#コマンド
@bot.command(name="hello")
async def hello(ctx, self):
    await ctx.send(f"こんにちは {ctx.author.display_name} さん。")

#スキンコマンド
@bot.command()
async def s(ctx: fortnitepy.ext.commands.Context) -> None:
    await bot.party.me.set_outfit(asset="AthenaCharacterItemDefinition'/BRCosmetics/Athena/Items/Cosmetics/Characters/CID_096_Athena_Commando_F_Founder.CID_096_Athena_Commando_F_Founder'")
