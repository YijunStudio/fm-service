from io import BytesIO
from wordcloud import ImageColorGenerator, WordCloud
from PIL import Image
import random
import base64

if __name__ == '__main__':

    results = [
        { 'key_name': '演奏者🐂', 'count': random.randint(0, 60) },
        { 'key_name': '...但不无聊呢', 'count': random.randint(0, 60) },
        { 'key_name': '怎么还没结束', 'count': random.randint(0, 60) },
        { 'key_name': '端庄.jpg', 'count': random.randint(0, 60) },
        { 'key_name': '真是优雅', 'count': random.randint(0, 60) },
        { 'key_name': '浪漫死了', 'count': random.randint(0, 60) },
        { 'key_name': '有点笨重', 'count': random.randint(0, 60) },
        { 'key_name': '空灵', 'count': random.randint(0, 60) },
        { 'key_name': '奇怪', 'count': random.randint(0, 60) },
    ]
    freqs = {}
    for item in results:
        freqs[item['key_name']] = item['count']
    result = WordCloud(
        font_path='./HanaminA.ttf', 
        width=800, height=1600, prefer_horizontal=0.98,
        background_color='White',
        mode='RGBA',
        colormap='GnBu',
        repeat=True
    ).generate_from_frequencies(freqs)
    # result.recolor(color_func=ImageColorGenerator(backgroud_image))
    result_img = result.to_image()
    result_img.save('./wordcloud.png')
    # 将图片写入BytesIO
    img_io = BytesIO() 
    result_img.save(img_io, 'PNG') # 保存图片
    # 从BytesIO中获取图片数据
    img_byte = img_io.getvalue()
    # 将图片转换为base64格式
    img_base64 = base64.b64encode(img_byte)
    # 将base64编码转换为字符串
    img_base64_str = img_base64.decode('utf-8')
    print(img_base64_str)
