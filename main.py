from unicodedata import category
import discord
from discord.ext import commands
import discord.utils
import fetch

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

# For better commands create new ones with better options

'''
* InitChannel Function:
- Creating normal channel:
    · InitChannel [ChannelName] "[Topic]" // Example: InitChannel general "Canal off-topic para hablar de lo que sea."
- Creating RotMG Mode Channel: Mode = {ppe, tpe, npe}
    · InitChannel [Mode] [Class] [User] // Example: InitChannel PPE Knight @neokeee
'''

RotMGMode = ['PPE', 'TPE', 'NPE']
ModeRule = {
    "tpe": "Tweakin Player Experience, similar a un ppe, pero los que inicien el TPE pueden intercambiar items que les sirvan entre ellos, solo si lo consiguen de manera de PPE. (También cuentan las pots.)"
}

@bot.command()
async def InitChannel(ctx, *args): # InitChannel [ChannelName or Mode] "[Topic]" \\ IMPORTANT: topic must be in ""
    categories = list(ctx.message.guild.categories)
    if args[0] in RotMGMode or args[0] in [x.lower() for x in RotMGMode]:
        GameMode = args[0]
        Class = args[1]
        _user = str(args[2]).replace("@", "").replace("<", "").replace(">", "").strip()
        RealUser = await ctx.message.guild.fetch_member(int(_user))
        NewChannelID = await ctx.message.guild.create_text_channel(f'{Class}-{GameMode}-{str(RealUser).split("#")[0]}', category=categories[3])
        ChannelTag = f'<#{NewChannelID.id}>'
        await ctx.send(f"Channel Created: {ChannelTag}")
        if GameMode == "TPE" or GameMode == "tpe":
            await ctx.message.guild.create_text_channel('tpe-progress', category=categories[3], topic=ModeRule["tpe"])
        return # TODO
    channelName = args[0]
    topic = args[1]
    NewChannelID = await ctx.message.guild.create_text_channel(channelName, category=categories[2], topic=topic)
    ChannelTag = f'<#{NewChannelID.id}>'
    await ctx.send(f"Channel Created: {ChannelTag}")

@bot.command()
async def BotUpdate(ctx):
    if ctx.message.author.id == neokeeeID:
        await ctx.send("Checking for updates")
        await fetch.compareVersion(ctx)
    else: await ctx.send("You don't have permission to do that.")
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
bot.run(open("token", "r").read().strip())
