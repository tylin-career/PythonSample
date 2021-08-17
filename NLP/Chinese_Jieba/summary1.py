import AutoSummary as ausu

content = 'issue1.txt'  
with open(content, 'r', encoding='utf8') as f:  #讀取原始文章
    text = f.read()

stops = []
with open('dictionary/stopWord_summar.txt','r', encoding='utf8') as f:  #停用詞庫
    for line in f.readlines():
        stops.append(line.strip())

sentences,indexs = ausu.split_sentence(text)  #按標點分割句子
tfidf = ausu.get_tfidf_matrix(sentences,stops)  #移除停用詞並轉換為矩陣
word_weight = ausu.get_sentence_with_words_weight(tfidf)  #計算句子關鍵詞權重
posi_weight = ausu.get_sentence_with_position_weight(sentences)  #計算位置權重
scores = ausu.get_similarity_weight(tfidf)  #計算相似度權重
sort_weight = ausu.ranking_base_on_weigth(word_weight, posi_weight, scores, feature_weight = [1,1,1])  #按句子權重排序
summar = ausu.get_summarization(indexs,sort_weight,topK_ratio = 0.1)  #取得摘要
print('原文:\n', text)
print('==========================================================')
print('摘要:\n',summar)
    