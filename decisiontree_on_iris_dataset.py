import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

#loading iris dataset
iris = load_iris()  

#making test index for testing,you can change the value for prediction
test_idx = [0,50,100]
# printing columns name i.e: features
print (iris.feature_names)
# printing last column name i.e: label
print (iris.target_names)
#checking rows
print (iris.data[0])
#checking labels
print (iris.target[0])

#printing iris dataset 
for i in range(len(iris.target)):
   print (" Example  %d : label %s, features %s" %(i, iris.target[i], iris.data[i]))

 #taining data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data,test_idx, axis =0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

#print testing labels
print(test_target)
#predicting test_idx
print(clf.predict(test_data))

