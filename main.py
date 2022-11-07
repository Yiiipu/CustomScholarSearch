from serpapi import GoogleSearch
import pickle
import csv
import html
import numpy as np

def search(page):
  params = {
    "engine": "google_scholar",
    "q": "3d printing machine learning",
    "api_key": "73836d2b1c501b29acca781ed571b29e019db90971ee1ae3c3ed67d4b055a11b",
    "start": page,
    "num": 20,
    "filter": 1
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  organic_results = results["organic_results"]
  #print(organic_results)
  return organic_results

for page in range(10):
  if False:
    results = search(page * 20)
    with open(f"result{page}.pkl", "wb") as f:
      pickle.dump(results, f)

  if True:
    with open(f"result{page}.pkl", "rb") as f:
      results = pickle.load(f)
    # print(results[2])
    for i in range(20):
      summary = results[i]["publication_info"]["summary"]
      # print(results[i]['title'])
      # print(summary.split('- ')[1].split(',')[0])

  if True:
    impactTable = {}
    with open("scimagojr 2021.csv") as f:
      allTable = csv.reader(f, delimiter=';')
      for row in allTable:
        # print(f"{row[2]},{row[7]}")
        impactTable[html.unescape(row[2])] = row[7]
        # if row[2][0:3]=="ACS":
        # print(row[2])

  for i in range(20):
    try:
      keykey = []
      info = html.unescape(results[i]["publication_info"]["summary"].split('- ')[1].split(',')[0])
      mystr = info[:-2]
      num = 0
      for key in impactTable:
        if key.startswith(mystr):
          num += 1
          if num >= 2:
            keykey = []
            break
          keykey = key
      if int(impactTable[keykey]) > 200:
        print(f"{results[i]['title']},{results[i]['link']} ,{keykey},{impactTable[keykey]}")
    except:
      pass
