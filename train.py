import os
import codecs
import re
import math
import jieba
import operator

def freqword(word,file):  # 统计词频，并返回字典
    freword = 0
    for i in file:
        if word is i:
            freword=freword+1
    return freword

def wordinfilecount(word, filelist):  # 查出包含该词的文档数
    count = 0  # 计数器
    for i in filelist:
        if word in i:
            count = count+1
    return count

def tf_idf(filelist):  # 针对filelist中的每个词计算TF-IDF,并返回前500个
    outdic = {}
    for file in filelist:
        for word in file:
            dic = freqword(word,file)
            tf = dic/ len(file)
            idf = math.log(len(filelist) / (wordinfilecount(word, filelist)))
            tfidf = tf * idf  # 计算TF-IDF
            outdic[word]=tfidf
    orderdic = sorted(outdic.items(), key=operator.itemgetter(1), reverse=True)#给字典排序，第一个参数是将字典转化为可排序的列表，第二个参数是key,第三个参数是表示倒序
    return orderdic[:500]


def rlistsSpam(filepath):
    stoppath = "C:/Users/lenovo/Desktop/email/ting_yong_ci.txt"#停用词表
    stopwords = {}.fromkeys(open(stoppath).read())#建立停用词表字典
    str = filepath
    pattern = re.compile('[\u4e00-\u9fa5]+')#正则表达式匹配，unicode编码中[\u4e00-\u9fa5]表示汉字,+表示匹配1个或多个
    regex = re.compile(pattern)
    results = regex.findall(str)#提取出所有的汉字
    lists = []
    lists_spam=[]
    for result in results:
        k = jieba.cut(result,HMM=True)
        for i in k:
            if i not in stopwords:
                lists.append(i)
                
    for i in range(0,len(lists)):
        if lists[i] not in lists0_spam:
            lists0_spam.append(lists[i])
    for i in range(0,len(lists)):
        if lists[i] not in lists_spam:
            lists_spam.append(lists[i])
            if lists[i] not in stopwords:
                if lists[i] in frespam:
                    frespam[lists[i]]+=1#之前出现过，则加1
                else:
                    frespam[lists[i]]=1#之前未出现过则赋为1
    '''for i in range(0,len(lists)):
        if lists[i] not in lists0:
            lists0.append(lists[i])
    for i in range(0,len(lists0)):
        if i not in stopwords:
            if i in frespam:
                frespam[i]+=1#之前出现过，则加1
            else:
                frespam[i]=1#之前未出现过则赋为1'''
    return lists#返回的是邮件中所有的词


def rlistsHam(filepath):
    stoppath = "C:/Users/lenovo/Desktop/email/ting_yong_ci.txt"#停用词表
    stopwords = {}.fromkeys(open(stoppath).read())#建立停用词表字典
    str = filepath
    pattern = re.compile('[\u4e00-\u9fa5]+')#正则表达式匹配，unicode编码中[\u4e00-\u9fa5]表示汉字,+表示匹配1个或多个
    regex = re.compile(pattern)
    results = regex.findall(str)#提取出所有的汉字
    lists = []
    lists_ham=[]
    for result in results:
        k = jieba.cut(result,HMM=True)
        for i in k:
            if i not in stopwords:
                lists.append(i)
    
    for i in range(0,len(lists)):
        if lists[i] not in lists0_ham:
            lists0_ham.append(lists[i])
    for i in range(0,len(lists)):
        if lists[i] not in lists_ham:
            lists_ham.append(lists[i])
            if lists[i] not in stopwords:
                if lists[i] in freham:
                    freham[lists[i]]+=1#之前出现过，则加1
                else:
                    freham[lists[i]]=1#之前未出现过则赋为1
    '''for i in range(0,len(lists0)):
        if i not in stopwords:
            if i in freham:
                freham[i]+=1#之前出现过，则加1
            else:
                freham[i]=1#之前未出现过则赋为1'''
    return lists#返回的是邮件中所有的词



if __name__=='__main__':

    #DicS="C:/Users/lenovo/Desktop/email/dicS.txt"
    #DicH="C:/Users/lenovo/Desktop/email/dicH.txt"

    f = open("C:/Users/lenovo/Desktop/email/trec06c/full/index")
    frespam={}#建立词出现频率的字典
    freham={}
    filelistH=[]
    filelistS=[]
    lists0_spam=[]
    lists0_ham=[]
    i=0
    count_spam=0
    count_ham=0
    for line in f:
        i+=1
        if i == 3000:#2000行
            P_spam=count_spam/(i-1)#训练集中垃圾邮件出现的概率
            P_ham=count_ham/(i-1)#训练集中正常邮件出现的概率
            break
        line=f.readline()
        if "spam" in line:#如果是垃圾邮件
            count_spam+=1
            line1=line.replace("spam ..","C:/Users/lenovo/Desktop/email/trec06c")#将内容换掉是为了打开
            line1 = line1.replace("\n", "")#去掉回车符
            file = open(line1, 'r', errors='ignore')#以只读模式打开文件并且忽略错误
            file1 = file.read()#读取文件内容
            filelistS.append(rlistsSpam(file1))#进行训练,对垃圾邮件的词汇列表进行丰富,并且计算每个词出现的频率
            file.close()
        elif "ham" in line:#如果是正常邮件
            count_ham+=1
            line1=line.replace("ham ..","C:/Users/lenovo/Desktop/email/trec06c")
            line1=line1.replace("\n","")
            file=open(line1,'r',errors = 'ignore')
            file1=file.read()
            filelistH.append(rlistsHam(file1))
            file.close()
    
    f.close()
    dicS=tf_idf(filelistS)#进行排序，排出垃圾邮件特征中权重最高的100个并且储存起来
    dicH=tf_idf(filelistH)
    #print(str(dicS))
    S=open("C:/Users/lenovo/Desktop/email/try1_3000_500/dicS.txt",'w')#可写打开
    H=open("C:/Users/lenovo/Desktop/email/try1_3000_500/dicH.txt",'w')
    fres=open("C:/Users/lenovo/Desktop/email/try1_3000_500/fres.txt",'w')
    freh=open("C:/Users/lenovo/Desktop/email/try1_3000_500/freh.txt",'w')
    p_spam=open("C:/Users/lenovo/Desktop/email/try1_3000_500/p_spam.txt",'w')
    p_ham=open("C:/Users/lenovo/Desktop/email/try1_3000_500/p_ham.txt",'w')
    S.write(str(dicS))#写入
    S.close()
    H.write(str(dicH))
    H.close()
    #print(frespam)
    #print(freham)
    for thing in lists0_spam:
        #print(value)
        frespam[thing]=frespam[thing]/count_spam
        #print(value,"\n")
    for thing in lists0_ham:
        freham[thing]=freham[thing]/count_ham
    fres.write(str(frespam))
    fres.close()
    freh.write(str(freham))
    freh.close()
    p_spam.write(str(P_spam))
    p_spam.close()
    p_ham.write(str(P_ham))
    p_ham.close()
    print("train over")
    print(count_spam)
    print(count_ham)
