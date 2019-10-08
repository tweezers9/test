import urllib.request

url = "https://www.baidu.com/"
response = urllib.request.urlopen(url)
html_string = response.read().decode("utf-8")
print(html_string)
with open("baidu1.html","w",encoding="utf-8") as fp:
    fp.write(html_string)
