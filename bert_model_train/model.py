# -*- coding: utf-8 -*-
# @Time : 2021/7/11 12:41
# @Author : XXX
# @Site : 
# @File : model.py
# @Software: PyCharm
import time

import torch.nn as nn
from pytorch_pretrained_bert import BertModel, BertConfig


class Model(nn.Module):
    def __init__(self, bert_path):
        super(Model, self).__init__()
        config = BertConfig.from_json_file(bert_path)
        self.bert = BertModel(config)
        # self.bert = BertModel.from_pretrained(bert_path)  # /bert_pretrain/
        for param in self.bert.parameters():
            param.requires_grad = False  # 每个参数都要 求梯度
        self.fc = nn.Linear(768, 10)  # 768 -> 10

    def forward(self, x):
        context = x[0]  # 输入的句子   (ids, seq_len, mask)
        types = x[1]
        mask = x[2]  # 对padding部分进行mask，和句子相同size，padding部分用0表示，如：[1, 1, 1, 1, 0, 0]
        _, pooled = self.bert(context, token_type_ids=types,
                              attention_mask=mask,
                              output_all_encoded_layers=False)  # 控制是否输出所有encoder层的结果
        out = self.fc(pooled)  # 得到10分类
        return out


if __name__ == "__main__":
    pass
