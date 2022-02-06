# jetosd 2-22
# simple http ls script created while going down the rabbit hole
# python http-ls.py [ip] [/directory/]

import requests
import sys

host = sys.argv[1]
directory = sys.argv[2]
url = "http://" + host + directory
print("url is {}".format(url))

r = requests.get(url)

for i in r.text.split():
    if "href" in i:
        if "?C=" not in i:
            if ">Parent" not in i:
                print(i.split('="')[1].split('"')[0])