from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


im = Image.open('C:/Users/宇峰/Desktop/python/大一第二学期/情话/pic/1.png')
width, height = im.size[0], im.size[1]
i = int(width/15)
font = ImageFont.truetype('simkai.ttf', i)
draw = ImageDraw.Draw(im)
draw.text((width/3, height/3), '吴宇峰', fill=(255, 0, 0), font=font)
im.save('C:/Users/宇峰/Desktop/python/大一第二学期/情话/pic/1t.png')
