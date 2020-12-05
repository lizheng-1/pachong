
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
Xtrain = np.array([[15, 1],[20,3],[25,2],[30,4],[35,2],[25,4],[15,2],[20,3]])
Ytrain = np.array([1,2,1,1,2,1,2,2])
print(Xtrain.shape,Xtrain[:,0],Xtrain[:,1])
Xtest = np.array([[10,2],[20,1],[30,3],[40,2],[15,1]])
Ytest = np.array([2,1,2,2,1])
plt.scatter(Xtrain[:,0],Xtrain[:,1],c = Ytrain)
plt.show()
#初始化树模型，criterion：gini或者entropy,前者是基尼系数，后者是信息熵。
clf = tree.DecisionTreeClassifier(criterion="entropy")

#实例化训练集
clf = clf.fit(Xtrain, Ytrain)
#返回测试集的准确度
score = clf.score(Xtest, Ytest)
y = clf.predict(Xtest)
# print('训练数据的大小为：',Xtrain.shape)
# print('测试数据的大小为：',Xtest.shape)
print('测试集的准确度：',score)
i = 0
lei = ["A","B"]
for each in range(len(Ytest)):
    i += 1
    print("第",i,'个的预测结果：',lei[y[each]-1],'\t真实结果：',lei[Ytest[each]-1],'\n')

