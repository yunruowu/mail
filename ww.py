# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
import re
import sys

"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
    classVec - 类别标签向量
"""

# 停用词表
f_stop = open("stop_use.txt")
stop_word = []
for line in f_stop:
    m = line.strip()
    stop_word.append(m)
f_stop.close()

f = open('qwe.txt', 'r')
a = f.read()
tf_idf = eval(a)

# print(tf_idf)
"""
f = open('spam.txt', 'r')
a = f.read()
sham_va = eval(a)
print(sham_va)
f = open('ham.txt', 'r')
a = f.read()
ham_va = eval(a)
"""
sham_va_word = []
sham_va_p = []
sum = 0
for word in tf_idf:
    sum = sum + word[1]
for word in tf_idf:
    if word[1] != 0:
        sham_va_word.append(word[0])
        sham_va_p.append(word[1] / sum)

ham_va_word = []
ham_va_p = []
sum1 = 0
for word in tf_idf:
    sum1 = sum1 + word[2]
for word in tf_idf:
    if word[2] != 0:
        ham_va_word.append(word[0])
        ham_va_p.append(word[2] / sum1)
print(sham_va_word, sham_va_p)
print(ham_va_word, ham_va_p)

i = 0
print(len(ham_va_p))
while i < len(ham_va_word):
    j = 1
    while j < len(ham_va_p) - i:
        if ham_va_p[j - 1] < ham_va_p[j]:
            t = ham_va_p[j]
            ham_va_p[j] = ham_va_p[j - 1]
            ham_va_p[j - 1] = t
            m = ham_va_word[j]
            ham_va_word[j] = ham_va_word[j - 1]
            ham_va_word[j - 1] = m
        j = j + 1
    i = i + 1
i = 0
while i < len(sham_va_word):
    j = 1
    while j < len(sham_va_p) - i:
        if sham_va_p[j - 1] < sham_va_p[j]:
            t = sham_va_p[j]
            sham_va_p[j] = sham_va_p[j - 1]
            sham_va_p[j - 1] = t
            m = sham_va_word[j]
            sham_va_word[j] = sham_va_word[j - 1]
            sham_va_word[j - 1] = m
        j = j + 1
    i = i + 1
ham_va_word = ham_va_word[0:200]
ham_va_p = ham_va_p[0:200]
sham_va_word = sham_va_word[0:200]
sham_va_p = sham_va_p[0:200]
sum_h = 0
sum_s = 0
for i in range(200):
    sum_s = sum_s + sham_va_p[i]
    sum_h = sum_h + ham_va_p[i]
for i in range(200):
    sham_va_p[i] = sham_va_p[i] / sum_s
    ham_va_p[i] = ham_va_p[i] / sum_h
print(ham_va_word, ham_va_p)
print(sham_va_word, sham_va_p)

import chardet
import codecs
import jieba
import sys

nnn = 200

y = 1
x = 0
n = 1
global dict
dict_all = []  # 所有文件的数组
class_all = []  # 对应文件的类别
tarin_set = []


# def createVocabList(dataSet):
#     vocabSet = set([])  # 创建一个空的不重复列表
#     for document in dataSet:
#         vocabSet = vocabSet | set(document)  # 取并集
#     return list(vocabSet)
#
#
#
# def feature_select(list_words):
#     # 总词频统计
#     doc_frequency = defaultdict(int)
#     for word_list in list_words:
#         for i in word_list:
#             doc_frequency[i] += 1
#
#     # 计算每个词的TF值
#     word_tf = {}  # 存储每个词的tf值
#     for i in doc_frequency:
#         word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
#
#     # 计算每个词的IDF值
#     doc_num = len(list_words)
#     word_idf = {}  # 存储每个词的idf值
#     word_doc = defaultdict(int)  # 存储包含该词的文档数
#     for i in doc_frequency:
#         for j in list_words:
#             if i in j:
#                 word_doc[i] += 1
#     for i in doc_frequency:
#         word_idf[i] = math.log(doc_num / (word_doc[i] + 1))
#
#     # 计算每个词的TF*IDF的值
#     word_tf_idf = {}
#     for i in doc_frequency:
#         word_tf_idf[i] = word_tf[i] * word_idf[i]
#
#     # 对字典按值由大到小排序
#     dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
#     word_lists =[]
#     for word in dict_feature_select:
#         word_lists.append(word[0])
#         #print(word[0:2])
#     return word_lists
def dect(mail):
    # print(mail)
    words = get_word(mail)
    # print(words)
    returnVec = [0] * 500
    p0 = 0.8844221105527639
    p1 = 0.11557788944723618
    if words == None:
        print("文件无法解码")
    else:
        # print("zhengchang")
        # print(words)
        for word in words:  # 遍历集合

            if word in sham_va_word:  # 如果词条存在于词汇表中，则置1
                # print("d222222222222222222222222    sa")
                for i in range(len(sham_va_word)):
                    if sham_va_word[i] == word:
                        m = sham_va_p[i]
                        p0 = p0 * m

                    else:
                        p0 = p0 * 1

            else:
                p0 = p0 * 0.00003
                # print("the word: %s is not in my Vocabulary!" % word)
        for word in words:  # 遍历集合

            if word in ham_va_word:
                # print("1111111111111")
                for i in range(len(ham_va_word)):
                    if ham_va_word[i] == word:
                        m = ham_va_p[i]
                        # print(m)
                        if (m == 0.0):
                            print("我睡觉哦")
                        p1 = p1 * m

                    else:
                        p1 = p1 * 1
            else:
                p1 = p1 * 0.00003
                # print("the word: %s is not in my Vocabulary!" % word)
        print(p0, p1)
        if p0 > p1:
            # print("lahji")
            return 1

        if p0 < p1:
            # print("zhanghc")
            return 0


def get_word(mail):
    m = open(mail, 'rb')
    data = m.read()
    enc = chardet.detect(data)['encoding']
    # print(enc)
    if enc == None:  # 无法解码
        # x = x + 1
        print("无法解码")
        return None
        pass
    # print("eror")
    else:
        # y = y + 1
        with open(mail, 'r')as f:
            try:
                w = f.read()
                w = re.sub('[a-z A-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘ ’ ！[\\]^_`{|}~\s]+', "", w)
                w = re.sub(
                    '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
                    '',
                    w)
                dict = []
                cut_list = jieba.lcut(w, False)
                # print(cut_list)
                for word in cut_list:

                    if word not in stop_word:
                        if len(word) > 1:
                            dict.append(word)
                # print(y)
                # fea = feature_select(cut_list)
                print(dict)
                return dict
            except UnicodeError:
                return None
                pass
            # print("Error: 没有找到文件或读取文件失败")
        # else:
        #    pass


with open('D:\\Emile\\trec06c\\trec06c\\full\\index', 'r') as f:
    for line in f:
        # print(line[16:20])
        # print(line[8:20])
        if line[0] == 's':  # 垃圾文件
            mail = 'D:\\Emile\\trec06c\\trec06c\\' + line[8:12] + '\\' + line[13:16] + '\\' + line[17:20]
            if get_word(mail) == None:
                pass
            if get_word(mail) == []:
                pass
            else:
                dict_all.append(mail)
                class_all.append(1)
                n = n + 1

        else:
            mail = 'D:\\Emile\\trec06c\\trec06c\\' + line[7:11] + '\\' + line[12:15] + '\\' + line[16:19]
            if get_word(mail) == None:
                pass
            if get_word(mail) == []:
                pass
            else:
                dict_all.append(mail)
                class_all.append(0)
                n = n + 1
        if n == nnn:
            break

# sham_va = [('dw',12.23),('dddd',23)]
# ham_va = [('dw',12.23),('dddd',23)]


class_t = []
num_t = 0
for mail in dict_all:
    i = dect(mail)
    class_t.append(i)
    num_t = num_t + 1
m = 0
f = 0
num_s = 0
num_h = 0
for i in range(num_t):
    if (class_all[i] == 0 ):
            num_s = num_s + 1
    else:
        num_h = num_h + 1

    if class_all[i] == class_t[i]:
        m = m + 1
    else:
        f = f + 1
fp = 0
fn = 0
tn = 0
tp = 0
for i in range(num_t):
    if (class_all[i] == 0 and class_t[i] == 0):
        fp = fp + 1
    if (class_all[i] == 1 and class_t[i] == 0):
        fn = fn + 1
    if (class_all[i] == 0 and class_t[i] == 1):
        tn = tn + 1
    if (class_all[i] == 1 and class_t[i] == 1):
        tp = tp + 1

print(num_h, num_s)
print(num_h / (num_s + num_h), num_s / (num_s + num_h))
print(m)
print(f)
print(m / (m + f))
print("DSD")
print(tp/(fp+tp))
print(tp/(tp+fn))