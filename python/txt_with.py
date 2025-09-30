import requests

url = "https://www.ymori.com/books/python2nen/test1.html"

response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)

filename = "download.txt"

# 1回目の書き込み
with open(filename, mode="w", encoding="utf-8") as f:
    f.write(response.text)

# 2回目の書き込み（もし必要なら残してもOK）
with open(filename, mode="w", encoding="utf-8") as f:
    f.write(response.text)
