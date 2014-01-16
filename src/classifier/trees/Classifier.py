#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cross_validation import cross_val_score
from sklearn import cross_validation
from sklearn.datasets import load_iris
import classifier.trees.ProcessData
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier

#gestures = classifier.trees.ProcessData.getTestData("../../../gestures/Daniel/gesture_0/1388424714_zimmer_left.txt")
gestures = classifier.trees.ProcessData.getTestData("../../../gestures/Daniel/gesture_3/1387647860_zimmer_left.txt")
#classifier.trees.ProcessData.plotTestData(gestures)
classifier.trees.ProcessData.findAmplitude(gestures[2])


iris = load_iris()
X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)


clf = AdaBoostClassifier(n_estimators=5)
clf.fit(X_train, y_train)
result = clf.predict(X_test) == y_test
rightPredicts = len([x for x in result if x == True])
print 100. / len(result) * rightPredicts 

clf = RandomForestClassifier(n_estimators=3) # Ergebnis schwankt ähnlich bei verschieden Eingaben
clf = clf.fit(X_train, y_train)
result = clf.predict(X_test) == y_test
rightPredicts = len([x for x in result if x == True])
print 100. / len(result) * rightPredicts

clf = GradientBoostingClassifier(n_estimators=100, max_depth=1, random_state=0).fit(X_train, y_train)
result = clf.predict(X_test) == y_test
rightPredicts = len([x for x in result if x == True])
print 100. / len(result) * rightPredicts

clf = ExtraTreesClassifier(max_depth=None, min_samples_split=1, random_state=0)
scores = cross_val_score(clf, iris.data, iris.target)
print scores