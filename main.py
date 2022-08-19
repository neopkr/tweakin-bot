from unicodedata import category
import discord
from discord.ext import commands
import discord.utils

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == "https://tenor.com/view/monkey-monkey-gif-gif-monkey-gif-funny-gif-21180838":
            clear()


neokeeeID = 382263610791034890
neokeeeTag = "neokeee#9998"

LEmote = "🇱"

IDsCanAdmin = [neokeeeID, 181460698981728256]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

try:
    pass
except commands.errors.CommandNotFound:
    pass
@bot.command()
async def init(ctx, *args):
    guild = ctx.message.guild
    myList = list(guild.categories)
    if args[0] == "set":
        if args[1] == "channel" and args[3] == "new":
            channelName = args[2]
            mode = args[4]
            if args[5] == "group":
                user = "group"
            else:
                _user = str(args[5]).replace("@", "").replace("<", "").replace(">", "").strip()
                userPurge = await ctx.message.guild.fetch_member(int(_user))
                user = str(userPurge).split("#")[0]
            _global = f'{channelName}-{mode}-{user}'
            await guild.create_text_channel(_global, category=myList[3])
    if args[0] == "create":
        if args[1] == "channel":
            channelName = args[2] # knight-ppe
            try:
                if args[3] is not None:
                    topico = args[3]
            except:
                topico = ""
            await guild.create_text_channel(channelName, category=myList[2], topic=topico)
@bot.command(name="https://tenor.com/view/monkey-monkey-gif-gif-monkey-meme-monkey-gif-funny-gif-21180838")
async def clear(ctx):
    message = ctx.message
    if message.author.id in IDsCanAdmin:
        await ctx.channel.purge(limit=10)
    else:
        pass

@bot.command(name="https://tenor.com/view/cocainer-gif-21483639")
async def tenor(ctx):
    await ctx.send("cocainer")

@bot.command()
async def ppe(ctx, *args):
    _user = str(args[0]).replace("@", "").replace("<", "").replace(">", "").strip() # ID
    userPurge = await ctx.message.guild.fetch_member(int(_user))
    user = str(userPurge).split("#")[0]
    print("called ppe")
    if args[1] == "status":
        print("status")
        if args[2] == "dead":
            channel=ctx.channel
            print("ppe", "status", "user:", user, _user, ctx.message.author)
            msg = []
            async for m in ctx.channel.history():
                if m.author == userPurge:
                    msg.append(m)
            await ctx.channel.delete_messages(msg)
            await ctx.channel.send(f'{userPurge}, STATUS: Dead')
            await ctx.send("https://tenor.com/view/monkey-monkey-gif-gif-monkey-gif-funny-gif-21180838")

@bot.command()
async def delete(ctx, *args):
    if ctx.message.author.id in IDsCanAdmin:
        print("ID")
        id = str(args[0]).replace("<", "").replace(">", "").replace("#", "")
        existing_channel = discord.utils.get(ctx.guild.channels, id=int(id))
        if existing_channel is not None:
            await existing_channel.delete()
        else:
            await ctx.send(f'No channel called {args[0]} was found')
    else: await ctx.send("No tienes permisos para esto.")
@bot.command()
async def L(ctx):
    message = []
    async for m in ctx.channel.history(limit=2):
        message.append(m)
    await message[1].add_reaction(LEmote)
    pass

@bot.command()
async def _help(ctx):
        monsur = '```PPE:\n- init set channel "Character" new "mode" @user\n- ppe @user status dead\nCHANNELS:\n- init create channel "channel-name"\n- delete #channel (Admin)\n-A:\n- L```'
        await ctx.send(monsur)
client = MyClient(intents=intents)
bot.run('MTAxMDA2MTY2MTQwMDQ3Nzc0Ng.GvG0Kk.8YWJNuEdfSt2QM0meGNpFasaYFPXYXpyW8JBG4')
#client.run('MTAxMDA2MTY2MTQwMDQ3Nzc0Ng.GvG0Kk.8YWJNuEdfSt2QM0meGNpFasaYFPXYXpyW8JBG4')