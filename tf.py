

# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator

"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
    classVec - 类别标签向量
"""


import chardet
import codecs
import jieba
import jieba.analyse
import re
import sys
result1=[]
result2=[]
x = 0
y = 0
n = 0
global dict,vocu
dict_all = []



def createVocabList(dataSet):
    vocabSet = set([])  # 创建一个空的不重复列表
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 取并集
    return list(vocabSet)




splitter=re.compile(r"\W+|\d+|[a-z]+")
with open('D:\\Emile\\trec06c\\trec06c\\full\\index','r') as f:
    for line in f:
        #print(line[16:20])
        #print(line[8:20])
        if line[0]=='s':#正常文件

            result1.append('D:\\Emile\\trec06c\\trec06c\\'+line[8:12]+'\\'+line[13:16]+'\\'+line[17:20])

        else:
            result2.append('D:\\Emile\\trec06c\\trec06c\\'+line[7:11]+'\\'+line[12:15]+'\\'+line[16:19])

        n = n+1
        if n ==10:
            break
for mail in result1:#垃圾邮件
    #print(mail)
    m = open(mail,'rb')
    data = m.read()
    enc=chardet.detect(data)['encoding']
    #print(enc)
    if enc ==None:#无法解码
        x =x+1
        pass
        #print("eror")
    else:
        y=y+1
        with open(mail, 'r')as f:
            try:
                w=f.read()
                #w = splitter.split(w)
                #数据清洗
                w= re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                w = re.sub(
                    '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                    '',
                    w)
                dict = []
                cut_list = jieba.lcut(w,True)
                for word in cut_list:
                    if word not in dict:
                        dict.append(word)
                #print(y)

                dict_all.append(cut_list)
            except UnicodeError:
                pass
                #print("Error: 没有找到文件或读取文件失败")
            else:
                pass
                #print("成功")
#print(x	,y)
#print(dict_all)





def loadDataSet():
    dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表好，0代表不好
    return dataset, classVec


"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
"""


def feature_select(list_words):
    # 总词频统计
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1

    # 计算每个词的TF值
    word_tf = {}  # 存储每个词的tf值
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())

    # 计算每个词的IDF值
    doc_num = len(list_words)
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]

    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select


if __name__ == '__main__':
    data_list,label_list = loadDataSet()  # 加载数据
    features = feature_select(dict_all)  # 所有词的TF-IDF值
    print(features)
    print(len(features))
