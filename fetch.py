from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

version_url = ""
main_url = ""

def GetVersionWeb():
    req = Request(version_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    return soup.get_text().strip()
def GetVersionLocal():
    f = open("version", "r")
    return f.read().strip()
def compareVersion():
    print(GetVersionLocal(), GetVersionWeb())
    pass

compareVersion()