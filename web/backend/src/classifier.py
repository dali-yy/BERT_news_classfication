import os

import torch
from pytorch_pretrained_bert import BertTokenizer
import pandas as pd
import numpy as np

from bert_model import Model


def id2category(idx):
    """
    将idx转换成对应的类别
    :param idx:
    :return:
    """
    categories = {0: "财经", 1: "房产", 2: "教育", 3: "科技", 4: "军事", 5: "汽车", 6: "体育", 7: "游戏", 8: "娱乐", 9: "其他"}
    return categories[idx]


class Classifier:
    def __init__(self, config_path, model_path, vocab_path):
        """
        :param config_path: bert模型参数配置文件
        :param model_path: 训练好的模型参数文件
        :param vocab_path: 语料库文件
        """
        self.model = Model(config_path)
        self.model.load_state_dict(torch.load(model_path))

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.tokenizer = BertTokenizer(vocab_path)  # 初始化分词器

    def preprocess(self, title, content, pad_size):
        """
        文本预处理，得到输入模型的数据
        :param title:
        :param content:
        :param pad_size:
        :return:
        """
        x = title + content
        x = self.tokenizer.tokenize(x)
        tokens = ["[CLS]"] + x + ["[SEP]"]

        # 得到input_id, seg_id, att_mask
        ids = self.tokenizer.convert_tokens_to_ids(tokens)
        types = [0] * (len(ids))
        masks = [1] * len(ids)
        # 短则补齐，长则切断
        if len(ids) < pad_size:
            types = types + [1] * (pad_size - len(ids))  # mask部分 segment置为1
            masks = masks + [0] * (pad_size - len(ids))
            ids = ids + [0] * (pad_size - len(ids))
        else:
            types = types[:pad_size]
            masks = masks[:pad_size]
            ids = ids[:pad_size]
        ids = torch.LongTensor(np.array(ids).reshape(1, -1)).to(self.device)
        types = torch.LongTensor(np.array(types).reshape(1, -1)).to(self.device)
        masks = torch.LongTensor(np.array(masks).reshape(1, -1)).to(self.device)
        return ids, types, masks

    def predict(self, title, content):
        """
        根据新闻的标题和内容预测类别
        :param title:
        :param content:
        :return:
        """
        ids, types, masks = self.preprocess(title, content, 300)  # 文本预处理
        self.model.eval()
        y = self.model([ids, types, masks])  # 输入模型
        y_pred = y.argmax().item()  # 得到概率最大者对应的下标
        return y_pred  # 返回新闻类别

    def file_predict(self, file_path):
        """
        预测文件中每条新闻的类别，并将类别写入文件中
        :param file_path:
        :return:
        """
        if os.path.splitext(file_path)[1] == ".csv":
            df = pd.read_csv(file_path, keep_default_na=False)
        else:
            df = pd.read_excel(file_path, keep_default_na=False)

        # 预测文件中每条新闻的类别
        for idx in df.index:
            df.loc[idx, "channelName"] = id2category(self.predict(df.loc[idx, "title"], df.loc[idx, "content"]))

        # 将预测结果写入源文件
        if os.path.splitext(file_path)[1] == ".csv":
            df.to_csv(file_path, index=False)
        else:
            df.to_excel(file_path, index=False)


if __name__ == "__main__":
    content = "阿松大"
    title = "哈哈哈"
    classifier = Classifier("bert_trained/bert_config.json", "bert_trained/roberta_model.pth", "bert_trained/vocab.txt")
    # print(classifier.predict(title, content), end='')
    classifier.file_predict("./dataset/test1.xlsx")
