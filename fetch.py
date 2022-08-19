from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup

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
def compareVersion():
    if GetVersionLocal() == GetVersionWeb():
        print("No update needed.")
        return
    else:
        urlretrieve(main_url, "./main.py")
        urlretrieve(version_url, "./version")
        print("Updated.")

compareVersion()