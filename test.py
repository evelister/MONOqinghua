from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import urllib.request
from PIL import Image, ImageFont, ImageDraw

browser = webdriver.Chrome()
browser.get('http://mmmono.com/group/100305/')

def execute_times(times):
    for i in range(times + 1):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
execute_times(4)

def write_to_file(content):
    with open('result.text', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def save_pic(item, i):
    i1 = str(i)
    local_pic_url = item.get('pic')
    file_path = "C:/Users/宇峰/Desktop/python/大一第二学期/情话/pic/"
    urllib.request.urlretrieve(local_pic_url, file_path + i1 + '.png')

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

text1 = soup.select('pre.pre-wrap')
texts = []
for text in text1:
    content = text.get_text()
    #content1 = content.replace('\n', '')
    texts.append(content)

pic1 = soup.find_all('div', class_='normal-cover')
pics = []
for p in pic1:
    p1 = p.find_all('img')
    for p2 in p1:
        pic = p2['src']
        pics.append(pic)

i = 1

for text, pic in zip(texts, pics):
    data = {
        'text': text,
        'pic': pic
    }
    save_pic(data, i)
    i += 1

i = 1

for text in texts:
    im = Image.open('C:/Users/宇峰/Desktop/python/大一第二学期/情话/pic/' + str(i) + '.png')
    width, height = im.size[0], im.size[1]
    a = int(width / 15)
    font = ImageFont.truetype('simkai.ttf', a)
    draw = ImageDraw.Draw(im)
    draw.text((width/3, height/3), text, fill=(255, 255, 255), font=font)
    im.save('C:/Users/宇峰/Desktop/python/大一第二学期/情话/pic/' + str(i) + 't.png')
    i += 1

browser.close()