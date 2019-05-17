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
import math
import collections

result1 = []
result2 = []
x = 0
y = 0
n = 0
sham = 0
ham = 0
global dict, vocu

# 停用词表
f_stop = open("stop_use.txt")
stop_word = []
for line in f_stop:
    m = line.strip()
    stop_word.append(m)
f_stop.close()
#print(stop_word)

def createVocabList(dataSet):
    vocabSet = set([])  # 创建一个空的不重复列表
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 取并集
    return list(vocabSet)


splitter = re.compile(r"\W+|\d+|[a-z]+")
with open('D:\\Emile\\trec06c\\trec06c\\full\\index', 'r') as f:
    for line in f:
        # print(line[16:20])
        # print(line[8:20])
        if line[0] == 's':  # 非正常文件
            sham = sham + 1
            result1.append('D:\\Emile\\trec06c\\trec06c\\' + line[8:12] + '\\' + line[13:16] + '\\' + line[17:20])

        else:
            ham = ham + 1
            result2.append('D:\\Emile\\trec06c\\trec06c\\' + line[7:11] + '\\' + line[12:15] + '\\' + line[16:19])

        n = n + 1
        if n == 3000:
            break


def get_dict(result):
    dict_all = []
    for mail in result:
        # print(mail)
        m = open(mail, 'rb')
        data = m.read()
        enc = chardet.detect(data)['encoding']
        # print(enc)
        if enc == None:  # 无法解码
            # x =x+1
            pass
            # print("eror")
        else:
            # y=y+1
            with open(mail, 'r')as f:
                try:
                    w = f.read()
                    # w = splitter.split(w)
                    # 数据清洗
                    # rint(w)
                    w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                    w = re.sub(
                        '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                        '', w)
                    # print(w)
                    dict = []
                    cut_list = jieba.lcut(w, False)
                    for word in cut_list:

                        if word not in stop_word:
                            if len(word)>1:
                                dict.append(word)

                    # print(y)

                    dict_all.append(dict)

                except UnicodeError:
                    pass
                    # print("Error: 没有找到文件或读取文件失败")
    return dict_all
    # print(x	,y)
    # print(dict_all)


def Creat_dict(result1, result2):
    global stop_word
    dict_all = []
    for mail in result1:  # 垃圾邮件
        # print(mail)
        m = open(mail, 'rb')
        data = m.read()
        enc = chardet.detect(data)['encoding']
        # print(enc)
        if enc == None:  # 无法解码
            # x =x+1
            pass
            # print("eror")
        else:
            # y=y+1
            with open(mail, 'r')as f:
                try:
                    w = f.read()
                    # w = splitter.split(w)
                    # 数据清洗
                    # rint(w)
                    w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                    w = re.sub(
                        '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                        '', w)
                    # print(w)
                    dict = []
                    cut_list = jieba.lcut(w, False)
                    for word in cut_list:
                        if word not in dict_all:
                            if len(word)>1:
                                #print(len(word), word)
                                if word not in stop_word:
                                    dict_all.append(word)
                    # print(y)



                except UnicodeError:
                    pass
                    # print("Error: 没有找到文件或读取文件失败")

    for mail in result2:  # 垃圾邮件
        # print(mail)
        m = open(mail, 'rb')
        data = m.read()
        enc = chardet.detect(data)['encoding']
        # print(enc)
        if enc == None:  # 无法解码
            # x =x+1
            pass
            # print("eror")
        else:
            # y=y+1
            with open(mail, 'r')as f:
                try:
                    w = f.read()
                    # w = splitter.split(w)
                    # 数据清洗
                    # rint(w)
                    w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                    w = re.sub(
                        '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                        '', w)
                    # print(w)
                    dict = []
                    cut_list = jieba.lcut(w, False)
                    for word in cut_list:
                       # print(len(word),word)
                        if word not in dict_all:
                            if len(word) > 1:
                                #print(len(word), word)
                                if word not in stop_word:
                                    dict_all.append(word)

                    # dict_all.append(cut_list)

                except UnicodeError:
                    pass
                    # print("Error: 没有找到文件或读取文件失败")
    return dict_all


def cut_mial(mail):
    dict = []
    m = open(mail, 'rb')
    data = m.read()
    enc = chardet.detect(data)['encoding']
    # print(enc)
    if enc == None:  # 无法解码
        # x =x+1
        pass
        # print("eror")
    else:
        # y=y+1
        with open(mail, 'r')as f:
            try:
                w = f.read()
                # w = splitter.split(w)
                # 数据清洗
                # rint(w)
                # w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                w = re.sub(
                    '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                    '', w)
                # print(w)

                cut_list = jieba.lcut(w, False)
                for word in cut_list:
                    if word not in stop_word:
                        if len(word) > 1:
                            #print(len(word), word)
                            dict.append(word)
            except UnicodeError:
                pass
    return dict


sham_dic = get_dict(result1)
ham_dic = get_dict(result2)

dict_all = Creat_dict(result1, result2)
#print(dict_all)
"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
"""


def feature_select(list_words):
    """

    :param list_words:
    :return:
    """
    # 总词频统计
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        #print(word_list)
        for i in word_list:
            doc_frequency[i] += 1
    print(doc_frequency)
    # 计算每个词的TF值
    word_tf = {}  # 存储每个词的tf值
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
    print(word_tf)
    # 计算每个词的IDF值
    doc_num = len(list_words)
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    print(word_doc)
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]
    # print(word_tf_idf)
    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)

    return dict_feature_select[0:500]


if __name__ == '__main__':
    # data_list,label_list = loadDataSet()  # 加载数据
   # print("dddddddddddd")
    #print(sham_dic)
    features = feature_select(sham_dic)  # 所有词的TF-IDF值
    # print(features)
    # print(len(features))
    f = open('spam1.txt', 'w')
    f.write(str(features))
    f.close()
    features = feature_select(ham_dic)  # 所有词的TF-IDF值
    #print(features)
    # print(len(features))
    f = open('ham2.txt', 'w')
    f.write(str(features))
    f.close()
    p_sham = sham / (sham + ham)
    p_ham = ham / (sham + ham)
    f = open('p.txt', 'w')

    f.write(str(p_sham))
    f.write("        ")
    f.write(str(p_ham))
    f.close()

    # tfs = []
    # text_all = []
    # for mail in result1:
    #     tf = []
    #     # print(len(dict_all))
    #     for i in range(len(dict_all)):
    #         # print(i)
    #         tf.append(0)
    #     m = cut_mial(mail)
    #     count = 0
    #     if m != []:
    #         for i in range(len(dict_all)):
    #             if dict_all[i] in m:
    #                 tf[i] = tf[i] + 1
    #                 count = count + 1
    #             else:
    #                 pass
    #         for i in range(len(dict_all)):
    #             tf[i] = tf[i] / count
    #         # print(count,len(m))
    #         tfs.append(tf)
    #         text_all.append(m)
    #         # print(m)
    #         # print(tf)
    # idf = []
    # for word in dict_all:
    #     fenzi = 1
    #     fenmu = len(text_all) + 1
    #     for i in range(len(text_all)):
    #         text = text_all[i]
    #         if word in text:
    #             fenzi = fenzi + 1
    #     idf.append(math.log(fenmu / fenzi))
    # tf_idfs = []
    # for tf in tfs:
    #     tf_idf = []
    #     for i in range(len(tf)):
    #         tf_idf.append(tf[i] * idf[i])
    #     tf_idfs.append(tf_idf)
    # print(len(tf_idfs), len(text_all))
    # for j in range(len(tf_idfs)):
    #     tf_idf = tf_idfs[j]
    #     max1 = max(tf_idf)
    #     for i in range(len(tf_idf)):
    #         if tf_idf[i] == max1:
    #             print(dict_all[i])
    #             break
    # tfs = []
    # text_all = []
    # for mail in result2:
    #     tf = []
    #     # print(len(dict_all))
    #     for i in range(len(dict_all)):
    #         # print(i)
    #         tf.append(0)
    #     m = cut_mial(mail)
    #     count = 0
    #     if m != []:
    #         for i in range(len(dict_all)):
    #             if dict_all[i] in m:
    #                 tf[i] = tf[i] + 1
    #                 count = count + 1
    #             else:
    #                 pass
    #         for i in range(len(dict_all)):
    #             tf[i] = tf[i] / count
    #         # print(count,len(m))
    #         tfs.append(tf)
    #         text_all.append(m)
    #         # print(m)
    #         # print(tf)
    # idf = []
    # for word in dict_all:
    #     fenzi = 1
    #     fenmu = len(text_all) + 1
    #     for i in range(len(text_all)):
    #         text = text_all[i]
    #         if word in text:
    #             fenzi = fenzi + 1
    #     idf.append(math.log(fenmu / fenzi))
    # tf_idfs = []
    # for tf in tfs:
    #     tf_idf = []
    #     for i in range(len(tf)):
    #         tf_idf.append(tf[i] * idf[i])
    #     tf_idfs.append(tf_idf)
    # print(len(tf_idfs), len(text_all))
    # for j in range(len(tf_idfs)):
    #     tf_idf = tf_idfs[j]
    #     max1 = max(tf_idf)
    #     for i in range(len(tf_idf)):
    #         if tf_idf[i] == max1:
    #             print(dict_all[i])
    #             break

    # result = []
    # for re1 in result1:
    #     result.append(re1)
    # for re1 in result2:
    #     result.append(re1)
    # print(result1)
    # print(result)
    # tfs = []
    # text_all = []
    # for mail in result:
    #     tf = []
    #     # print(len(dict_all))
    #     for i in range(len(dict_all)):
    #         # print(i)
    #         tf.append(0)
    #     m = cut_mial(mail)
    #     count = 0
    #     if m != []:
    #         for i in range(len(dict_all)):
    #             if dict_all[i] in m:
    #                 tf[i] = tf[i] + 1
    #                 count = count + 1
    #             else:
    #                 pass
    #         for i in range(len(dict_all)):
    #             tf[i] = tf[i] / count
    #         # print(count,len(m))
    #         tfs.append(tf)
    #         text_all.append(m)
    #         # print(m)
    #         # print(tf)
    # idf = []
    # for word in dict_all:
    #     fenzi = 1
    #     fenmu = len(text_all) + 1
    #     for i in range(len(text_all)):
    #         text = text_all[i]
    #         if word in text:
    #             fenzi = fenzi + 1
    #     idf.append(math.log(fenmu / fenzi))
    # tf_idfs = []
    # for tf in tfs:
    #     tf_idf = []
    #     for i in range(len(tf)):
    #         tf_idf.append(tf[i] * idf[i])
    #     tf_idfs.append(tf_idf)
    # print(len(tf_idfs), len(text_all))
    # for j in range(len(tf_idfs)):
    #     tf_idf = tf_idfs[j]
    #     max1 = max(tf_idf)
    #     for i in range(len(tf_idf)):
    #         if tf_idf[i] == max1:
    #             print(dict_all[i])
    #             break
    # print(len(tf_idfs),len(text_all))

    dict_sham = []
    for mail in result1:
        words = cut_mial(mail)
        for word in words:
            dict_sham.append(word)
    dict_ham = []
    for mail in result2:
        words = cut_mial(mail)
        for word in words:
            dict_ham.append(word)

    # sham
    tf_sham = []
    for i in range(len(dict_all)):
        # # print(i)
        tf_sham.append(0)
    count = 0
    for i in range(len(dict_all)):
        for j in range(len(dict_sham)):
            if dict_all[i] in dict_sham[j]:
                tf_sham[i] = tf_sham[i] + 1
                count = count + 1
            else:
                pass
    #print(tf_sham)
    for i in range(len(dict_all)):
        tf_sham[i] = tf_sham[i] / count
    #print(tf_sham)
    # ham
    tf_ham = []
    for i in range(len(dict_all)):
        # # print(i)
        tf_ham.append(0)
    count = 0
    for i in range(len(dict_all)):
        for j in range(len(dict_ham)):
            if dict_all[i] in dict_ham[j]:
                tf_ham[i] = tf_ham[i] + 1
                count = count + 1
            else:
                pass
            pass
    for i in range(len(dict_all)):
        tf_ham[i] = tf_ham[i] / count
    # print(count,len(m))
    # tfs.append(tf)
    # text_all.append(m)
    idf = []
    for word in dict_all:
        fenzi = 1
        fenmu = 3
        if word in dict_sham:
            fenzi = fenzi + 1
        if word in dict_ham:
            fenzi = fenzi + 1
        idf.append(math.log(fenmu / fenzi))
    tf_idf_sham = []
    tf_idf_ham = []
    for i in range(len(dict_all)):
        tf_idf_sham.append(idf[i] * tf_sham[i])
        tf_idf_ham.append(idf[i] * tf_ham[i])

   # print(tf_idf_sham)
    mmm=[]
    for i in range(len(dict_all)):
        m = (dict_all[i],tf_idf_sham[i],tf_idf_ham[i])
        #print(m)
        mmm.append(m)
    f = open('qwe.txt', 'w')
    f.write(str(mmm))
    f.close()
    print("stop")