# -BERT-
通过python爬虫获取人民网、新浪等网站新闻作为训练集，基于BERT构建新闻文本分类模型，并结合node.js + vue完成了一个可视化界面。

### 一、新闻爬取

#### 1、python依赖

```
pip install demjson==2.2.4  // 解析json数据
pip install requests==2.25.1  // 请求网页
pip install Beautifulsoup4==0.0.1  // 解析HTML源码
pip install loguru==0.5.3
pip install install openpyxl==3.0.7
```

#### 2、爬取过程

主要依赖request库请求网页源码或JavaScript数据，然后通过bs4s识别标签进行解析，获取网页中的新闻内容。不同网页代码框架不同，四个文件针对不同网站的HTML代码进行解析。爬取的新闻内容通过openpyxl保存在excel文件中



### 二、基于BERT的新闻文本分类模型

#### 1、python 依赖

```
pip install pytorch-pretrained-bert==0.6.2

CUDA-10.2 PyTorch builds are no longer available for Windows, please use CUDA-11.3
```

有关pytorch和cuda 10.2 的安装可参见官网：

pytorch：https://pytorch.org/

cuda10.2：https://developer.nvidia.com/cuda-10.2-download-archive

#### 2、代码使用说明

（1）代码中使用的bert预训模型来自哈工大https://github.com/ymcui/Chinese-BERT-wwm

（2）可运行 main.py 文件自行训练模型，使用的数据集类似于 dataset 中的文本格式即可

（3）one_predict.py 可实现对单条新闻文本的分类

（4）file_predict.py 可实现对文件中所有的新闻进行分类



### 三、web端应用

#### 1、前端

基于 Vue 框架

项目热启动于http://localhost:8080

```
cd frontend
npm install
npm run dev
```

#### 2、后端

基于 node.js 中的 express 框架

项目热启动于http://localhost:3000

```
cd backend
npm install
npm run dev
```



注意：在使用的时候需要将训练好的分类模型放在 \backend\src\bert_trained 文件夹中，否则无法实现新闻文本分类功能

