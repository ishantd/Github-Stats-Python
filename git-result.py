import json
import pandas as pd
from pandas import DataFrame

total_files = 0
total_languages = []
total_lines = 0

with open('data/new_data.json') as f:
    repos = json.load(f)

for i in range(0, len(repos["full_name"])):
    with open('data/repos/'+str(i)+'.json') as f:
        code = json.load(f)
    for j in range(0, len(code["linesOfCode"])):
        total_lines = code["linesOfCode"][str(j)] + total_lines
    for j in range(0, len(code["files"])):
        total_files = code["files"][str(j)] + total_files
    for j in range(0, len(code["language"])):
        total_languages.append(code["language"][str(j)])


total_languages = list(dict.fromkeys(total_languages))

result = [total_files, total_lines, len(
    total_languages), len(repos["full_name"])]


with open('data/result.json', 'w') as file:
    json.dump(result, file)
