# -*- coding: utf-8 -*-
# @Time : 2021/7/10 23:46
# @Author : XXX
# @Site : 
# @File : one_predict.py
# @Software: PyCharm
import sys
import time

from classifier import Classifier, id2category


if __name__ == "__main__":
    content = sys.argv[1]
    title = sys.argv[2]
    start = time.time()
    classifier = Classifier("bert_pretrained/bert_config.json", "checkpoint/my_bert_model.pth", "bert_pretrained"
                                                                                                "/vocab.txt")
    category = id2category(classifier.predict(title, content))
    end = time.time()
    print("新闻类别：" + category)
    print("用时：{:2f}秒".format(end-start))
