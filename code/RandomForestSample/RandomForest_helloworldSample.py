from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

X,y = make_blobs(n_samples = 10000,n_features=10,centers = 100,random_state = 0)

#对决策树和随机森林对比
clf = DecisionTreeClassifier(max_depth = None,min_samples_split=2,random_state = 0)
scores = cross_val_score(clf,X,y)
print("决策树准确率；",scores.mean())

clf = RandomForestClassifier(n_estimators=10,max_depth = None,min_samples_split=2,random_state = 0)
scores = cross_val_score(clf,X,y)
print("随机森林准确率：",scores.mean())
