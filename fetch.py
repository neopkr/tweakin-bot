from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import os

version_url = "https://raw.githubusercontent.com/neopkr/tweakin-bot/main/version?token=GHSAT0AAAAAABXZYJSLQUNE2KQ5O6MCDDVYYYAD6LA"
main_url = "https://raw.githubusercontent.com/neopkr/tweakin-bot/main/main.py?token=GHSAT0AAAAAABXZYJSKTCSOHFLECAUYPA52YYAD6TQ"

def GetVersionWeb():
    req = Request(version_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    return soup.get_text().strip()
def GetVersionLocal():
    f = open("version", "r")
    return f.read().strip()
async def compareVersion(ctx):
    if GetVersionLocal() == GetVersionWeb():
        await ctx.send("No update needed.")
        return
    else:
        await ctx.send("An update was found. Downloading...")
        urlretrieve(main_url, "./main.py")
        urlretrieve(version_url, "./version")
        await ctx.send("Updated Finished.")
        await ctx.send("Re-starting bot...")
        await os.system('python3 main.py')