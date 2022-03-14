# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# coding: UTF-8
import sys

import torch
from pytorch_pretrained_bert import BertAdam
from model import Model
from train import train
from test import test
from data_process import generate_dataset, generate_train_loader, generate_test_loader

# 加载数据集
train_dataset = generate_dataset("./dataset/train.xlsx")  # 获取训练集
test_dataset = generate_dataset("./dataset/test.xlsx")  # 获取测试集
train_loader = generate_train_loader(train_dataset, 8)  # 训练集迭代器
test_loader = generate_test_loader(test_dataset, 8)  # 测试集迭代器

# 定义GPU设备
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义模型
model = Model("./bert_pretrained/")
model.to(DEVICE)

# 定义优化器
NUM_EPOCHS = 20  # 训练批次大小
param_optimizer = list(model.named_parameters())  # 模型参数名字列表
no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
    {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}]
optimizer = BertAdam(optimizer_grouped_parameters,
                     lr=2e-5,
                     warmup=0.05,
                     t_total=len(train_loader) * NUM_EPOCHS
                     )


def run(save_path):
    """
    训练模型
    :param save_path: 模型保存地址
    :return:
    """
    best_acc = 0.0
    for epoch in range(1, NUM_EPOCHS + 1):  # 20个epoch
        train(model, DEVICE, train_loader, optimizer, epoch)
        acc = test(model, DEVICE, test_loader)
        if best_acc < acc:
            best_acc = acc
            torch.save(model.state_dict(), save_path)  # 保存最优模型
        print("acc is: {:.4f}, best acc is {:.4f}\n".format(acc, best_acc))


if __name__ == '__main__':
    # run("./checkpoint/" + sys.argv[1])
    run("./checkpoint/model.pth")
