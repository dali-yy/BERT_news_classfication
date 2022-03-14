# -*- coding: utf-8 -*-
# @Time : 2021/7/11 12:42
# @Author : XXX
# @Site : 
# @File : data_process.py
# @Software: PyCharm
# coding: UTF-8
# coding: UTF-8
import torch
from pytorch_pretrained_bert import BertModel, BertTokenizer, BertConfig, BertAdam
import pandas as pd
import numpy as np
from tqdm import tqdm
from torch.utils.data import *

tokenizer = BertTokenizer("bert_pretrained/vocab.txt")  # 初始化分词器
# 新闻类别字典
category_dict = {"财经": 0, "房产": 1, "教育": 2, "科技": 3, "军事": 4, "汽车": 5, "体育": 6, "游戏": 7, "娱乐": 8, "其他": 9}


def generate_inputs(title, content, pad_size):
    """
    将文本转换成模型的输入格式
    :param title:
    :param content:
    :param pad_size:
    :return:
    """
    x = title + content
    x1 = tokenizer.tokenize(x)
    tokens = ["[CLS]"] + x1 + ["[SEP]"]

    # 得到input_id, seg_id, att_mask
    ids = tokenizer.convert_tokens_to_ids(tokens)
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
    return ids, types, masks


def generate_dataset(file_path):
    """
    根据文件生成数据集
    :param file_path: 文件路径
    :return:
    """
    input_ids = []  # input char ids
    input_types = []  # segment ids
    input_masks = []  # attention mask
    labels = []  # 标签
    pad_size = 300  # 也称为 max_len

    # 读取文件
    df = pd.read_excel(file_path, sheet_name=None, keep_default_na=False)
    # 拼接excel文件中每个表
    df = pd.concat([df["财经"], df["房产"], df["教育"], df["科技"], df["军事"], df["汽车"], df["体育"], df["游戏"], df["娱乐"], df["其他"]])
    # 打乱文件中条目的顺序
    indices = np.arange(0, len(df))
    np.random.shuffle(indices)
    df = df.iloc[indices]
    # 修正索引
    df.reset_index(drop=True, inplace=True)

    for i in tqdm(df.index):
        title = df.loc[i, "title"]
        content = df.loc[i, "content"]

        ids, types, masks = generate_inputs(title, content, pad_size)
        y = category_dict[df.loc[i, "channelName"]]

        input_ids.append(ids)
        input_types.append(types)
        input_masks.append(masks)
        assert len(ids) == len(masks) == len(types) == pad_size
        labels.append([int(y)])

    return np.array(input_ids), np.array(input_types), np.array(input_masks), np.array(labels)


def generate_train_loader(train_dataset, batch_size):
    """
    训练集数据迭代器
    :param train_dataset:tuple (input_ids_train, input_types_train, input_masks_train, y_train)
    :param batch_size:批次大小
    :return:
    """
    train_data = TensorDataset(torch.LongTensor(train_dataset[0]),
                               torch.LongTensor(train_dataset[1]),
                               torch.LongTensor(train_dataset[2]),
                               torch.LongTensor(train_dataset[3]))
    train_sampler = RandomSampler(train_data)
    train_loader = DataLoader(train_data, sampler=train_sampler, batch_size=batch_size)
    return train_loader


def generate_test_loader(test_dataset, batch_size):
    """
    测试集数据迭代器
    :param test_dataset: tuple (input_ids_test, input_types_test, input_masks_test, y_test)
    :param batch_size: 批次大小
    :return:
    """
    test_data = TensorDataset(torch.LongTensor(test_dataset[0]),
                              torch.LongTensor(test_dataset[1]),
                              torch.LongTensor(test_dataset[2]),
                              torch.LongTensor(test_dataset[3]))
    test_sampler = SequentialSampler(test_data)
    test_loader = DataLoader(test_data, sampler=test_sampler, batch_size=batch_size)
    return test_loader


if __name__ == "__main__":
    pass