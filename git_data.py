import json
import pandas as pd
from pandas import DataFrame
import threading
import time

from timeloop import Timeloop
from datetime import timedelta


data = pd.read_json("https://api.github.com/users/ishantd/repos")
df = pd.DataFrame(data)


Export = df.to_json(
    r'/home/ishant/ishant_linux/my-website-new/scripts/data/new_data.json')

with open('/home/ishant/ishant_linux/my-website-new/scripts/data/new_data.json') as f:
    repos = json.load(f)

# print(repos["full_name"]["0"])
url_list = [None] * len(repos["full_name"])

for i in range(0, len(repos["full_name"])):
    url_list[i] = "https://api.codetabs.com/v1/loc?github=" + \
        repos["full_name"][str(i)]


def repo_data(count):
    print(url_list[count])
    data = pd.read_json(url_list[count])
    print(data)
    df = pd.DataFrame(data)
    Export = df.to_json(
        r'/home/ishant/ishant_linux/my-website-new/scripts/data/repos/'+str(count)+'.json')


for i in range(0, len(repos["full_name"])):
    repo_data(i)
    time.sleep(10)
    print("The " + str(i) + " git stats is successfully saved ")
