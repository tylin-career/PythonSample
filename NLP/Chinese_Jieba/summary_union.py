import AutoSummary as ausu
import requests
from bs4 import BeautifulSoup as soup

stops = []
with open('dictionary/stopWord_summar.txt','r', encoding='utf8') as f:  #停用詞庫
    for line in f.readlines():
        stops.append(line.strip())

urls = []
url = 'https://udn.com/news/breaknews/1'  #聯合報新聞
html = requests.get(url)
sp = soup(html.text, 'html.parser')
data1 = sp.select('#breaknews_body dl dt h2 a')
for d in data1:  #取得新聞連結
    urls.append('https://udn.com' + d.get('href'))

i = 1
for url in urls:  #逐一取得新聞
    html = requests.get(url)
    sp = soup(html.text, 'html.parser')
    data1 = sp.select('#story_body_content p')  #新聞內容
    print('處理第 {} 則新聞'.format(i))
    text = ''
    for d in data1:
        if d.text.find('延伸閱讀') != -1:  #遇到延伸閱讀就結束此則新聞
            break
        if d.text != '':  #有新聞內容
            text += d.text
    sentences,indexs = ausu.split_sentence(text)  #按標點分割句子
    tfidf = ausu.get_tfidf_matrix(sentences,stops)  #移除停用詞並轉換為矩陣
    word_weight = ausu.get_sentence_with_words_weight(tfidf)  #計算句子關鍵詞權重
    posi_weight = ausu.get_sentence_with_position_weight(sentences)  #計算位置權重
    scores = ausu.get_similarity_weight(tfidf)  #計算相似度權重
    sort_weight = ausu.ranking_base_on_weigth(word_weight, posi_weight, scores, feature_weight = [1,1,1])
    summar = ausu.get_summarization(indexs,sort_weight,topK_ratio = 0.3)  #取得摘要
    print(summar)
    print('==========================================================')
    i += 1
    