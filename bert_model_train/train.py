# -*- coding: utf-8 -*-
# @Time : 2021/7/11 12:41
# @Author : XXX
# @Site : 
# @File : train.py
# @Software: PyCharm
# coding: UTF-8
import torch.nn.functional as F


def train(model, device, train_loader, optimizer, epoch):  # 训练模型
    model.train()
    best_acc = 0.0
    for batch_idx, (x1, x2, x3, y) in enumerate(train_loader):
        x1, x2, x3, y = x1.to(device), x2.to(device), x3.to(device), y.to(device)
        y_pred = model([x1, x2, x3])  # 得到预测结果
        model.zero_grad()  # 梯度清零
        loss = F.cross_entropy(y_pred, y.squeeze())  # 得到loss
        loss.backward()
        optimizer.step()
        if (batch_idx + 1) % 100 == 0:  # 打印loss
            print('Train Epoch: {} [{}/{} ({:.2f}%)]\tLoss: {:.6f}'.format(epoch, (batch_idx + 1) * len(x1),
                                                                           len(train_loader.dataset),
                                                                           100. * batch_idx / len(train_loader),
                                                                           loss.item()))  # 记得为loss.item()


if __name__ == "__main__":
    pass
