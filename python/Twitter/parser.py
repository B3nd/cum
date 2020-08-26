from bs4 import BeautifulSoup
import requests

r = requests.get("""https://""" + """www.youtube.com/feed/trending""")
data = r.text

f = open('text.html', 'wb')
f.write(r.content)
f.close()
f = open('text.html', 'r', encoding='utf-8')
text = f.read()
f.close()

soup = BeautifulSoup(text, 'html.parser')

all_videos = soup.findAll('div', {'class': 'yt-lockup-content'})

i = 1
for video in all_videos:
    link = video.find('h3', {"class": "yt-lockup-title"})
    print(str(i) + ") " + link.find('a').get_text())
    i +=1


