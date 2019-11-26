import requests
import pandas as pd
import jieba
import wordcloud
import random
import matplotlib.pyplot as plt
from lxml import etree

# 颜色函数
def random_color_func(word, font_size, position, orientation, font_path, random_state):
    s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
    print(s)
    return s


url = 'http://comment.bilibili.com/123072475.xml'
response = requests.get(url)
print(response)
xml = etree.fromstring(response.content)

dm = xml.xpath("/i/d/text()")
print(dm)

dm_df = pd.DataFrame(dm,columns=['comment~~~'])
print(dm_df)

dm_df.to_csv('./res/雨幕-弹幕.csv',encoding='utf_8_sig')

dm_str = ''.join(dm)
words_list = jieba.lcut(dm_str)
words_str = ''.join(words_list)

background_Image = plt.imread('./res/girl.jpg')
wc = wordcloud.WordCloud(
    background_color='white',
    mask=background_Image,
    font_path='./font/msyh.ttf',

    max_words=2000,
    max_font_size=100,
    min_font_size=10,
    color_func=random_color_func,
    random_state=50,
)

word_cloud = wc.generate(words_str)
word_cloud.to_file('./res/wordCloud.jpg')