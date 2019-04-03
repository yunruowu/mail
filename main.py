import jieba


s = "标题中的单词单独作为特征，添加标志"
seg_list = jieba.lcut("我来到北京清华大学", cut_all=True)
print(seg_list)
print("全模式: " + "/ ".join(seg_list))  # 全模式