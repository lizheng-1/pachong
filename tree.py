#导入 tree 模块
from sklearn import tree

from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split
import pandas as pd
#import pydotplus
#红酒数据集的数据探索
wine = load_wine()

print('x数据集形状：',wine.data.shape)

print('y数据集形状：',wine.target.shape)
#将x,y都放到数据集data_frame中
data_frame = pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
#显示前10行
print('数据前十行显示:\n',data_frame.head(10))
#显示数据集特征列名
print('数据集特征列名:',wine.feature_names)
#显示数据集的标签分类
print('数据集标签分类:',wine.target_names)
#70%为训练数据，30%为测试数据
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.3)
print('训练数据的大小为：',Xtrain.shape)
print('测试数据的大小为：',Xtest.shape)
#初始化树模型，criterion：gini或者entropy,前者是基尼系数，后者是信息熵。
clf = tree.DecisionTreeClassifier(criterion="entropy")
#实例化训练集
clf = clf.fit(Xtrain, Ytrain)
#返回测试集的准确度
score = clf.score(Xtest, Ytest)
y = clf.predict(Xtest)
print('测试集的准确度：',score)
# for each in range(len(Ytest)):
#     print('预测结果：',y[each],'\t真实结果：',Ytest[each],'\n')
# #特征重要性
# feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类',\
#                 '花青素','颜色强度','色调','od280/od315 稀释葡萄酒','脯氨酸']
# print(clf.feature_importances_)
# print([*zip(feature_name,clf.feature_importances_)])
