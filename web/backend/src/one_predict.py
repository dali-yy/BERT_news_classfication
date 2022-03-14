# -*- coding: utf-8 -*-
# @Time : 2021/7/10 23:46
# @Author : XXX
# @Site : 
# @File : one_predict.py
# @Software: PyCharm
import sys
from classifier import Classifier


if __name__ == "__main__":
    content = sys.argv[1]
    title = sys.argv[2]
    classifier = Classifier("src/bert_trained/bert_config.json", "src/bert_trained/my_bert_model.pth", "src/bert_trained/vocab.txt")
    print(classifier.predict(title, content), end="")
