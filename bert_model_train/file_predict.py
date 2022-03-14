# -*- coding: utf-8 -*-
# @Time : 2021/7/10 23:46
# @Author : XXX
# @Site : 
# @File : file_predict.py
# @Software: PyCharm
import sys
import time

from classifier import Classifier

if __name__ == "__main__":
    file_path = sys.argv[1]
    start = time.time()
    classifier = Classifier("./bert_pretrained/bert_config.json", "./checkpoint/my_bert_model.pth",
                            "bert_pretrained/vocab.txt")
    classifier.file_predict(file_path)
    end = time.time()
    print("分类成功！")
    print("用时：{:2f}秒".format(end - start))

