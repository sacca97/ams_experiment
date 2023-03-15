import os
from bs4 import BeautifulSoup

dir = os.listdir("norules/relevance/")
for file in dir:
    with open("norules/relevance/" + file, "r") as f:
        if file[-4:] != "html":
            continue
        soup = BeautifulSoup(f, "html.parser")
        out = [
            l.get_text().strip()[:50]
            for l in soup.find_all("div", class_="card-text")
            if len(l.get_text().strip()) > 0
        ]
        with open(file[:-4] + "txt", "w") as ff:
            for x in out:
                ff.write(x)
                ff.write("\n")
