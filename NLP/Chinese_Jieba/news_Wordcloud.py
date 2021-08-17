import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

jieba.set_dictionary("dictionary/dict.txt.big.txt")
jieba.load_userdict("dictionary/user_dict_test.txt")
with open('dictionary/stopWord_cloudmod.txt','r',encoding='utf-8-sig') as f:
    stops = f.read().split("\n")


text = open('news1.txt', "r",encoding="utf-8").read()  
bw = jieba.cut(text, cut_all=False)


word_list = []
for word in bw:
    if word not in stops:
        word_list.append(word)

diction = Counter(word_list)
# print(diction)
# print("|".join(word_list))



font = 'msyh.ttc'  
#mask = np.array(Image.open("heart.png"))  #設定文字雲形狀 
wordcloud = WordCloud(font_path=font) 
#wordcloud = WordCloud(background_color="white",mask=mask,font_path=font)  #背景顏色預設黑色,改為白色 
wordcloud.generate_from_frequencies(frequencies=diction)  #產生文字雲


plt.figure(figsize=(6,6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("news_Wordcloud.png")