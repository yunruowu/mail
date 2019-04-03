import chardet
import codecs
import sys
result1=[]
result2=[]
with open('D:\\Emile\\trec06c\\trec06c\\full\\index','r') as f:
	for line in f:
		#print(line[16:20])
		#print(line[8:20])
		if line[0]=='s':

			result1.append('D:\\Emile\\trec06c\\trec06c\\'+line[8:12]+'\\'+line[13:16]+'\\'+line[17:20])
		else:
			result2.append('D:\\Emile\\trec06c\\trec06c\\'+line[7:11]+'\\'+line[12:15]+'\\'+line[16:19])
for mail in result1:
	#print(mail)
	m = open(mail,'rb')
	data = m.read()
	enc=chardet.detect(data)['encoding']
	#print(enc)
	if enc ==None:
		pass
		#print("eror")
	else:
		with codecs.open(mail, 'r', enc)as f:
			try:
				f.read()
			except UnicodeError:
				pass
				#print("Error: 没有找到文件或读取文件失败")
			else:
				pass
				#print("成功")

