import pandas as pd
from numpy import array as arr
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from imblearn.combine import SMOTEENN
from sklearn import metrics
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ChurnModel:

    def __init__(self):
        self.istrain = False
    
    def Training(self):
        df=pd.read_csv("tel_churn.csv",index_col='Customer')
        x=df.drop('Churn',axis=1)
        y=df['Churn']
        sm = SMOTEENN()
        X_resampled, y_resampled = sm.fit_resample(x, y)
        X_resampled = X_resampled.values
        y_resampled = y_resampled.values
        xr_train,xr_test,yr_train,yr_test=train_test_split(X_resampled, y_resampled,test_size=0.2)
        self.model_knn = KNeighborsClassifier(n_neighbors=5)  
        self.model_knn.fit(xr_train, yr_train)
        self.istrain = True
    
    def Predicting(self,x_test):
        if(self.istrain == True):
            self.y_predict = self.model_knn.predict(x_test)
        else:
            print("Model not trained")
        


        
'''df=pd.read_csv("/Users/nandanyadav/Desktop/sample/pream project/tel_churn.csv")
x=df.drop('Churn',axis=1)
y=df['Churn']
sm = SMOTEENN()
X_resampled, y_resampled = sm.fit_resample(x, y)
xr_train,xr_test,yr_train,yr_test=train_test_split(X_resampled, y_resampled,test_size=0.2)
model_knn = KNeighborsClassifier(n_neighbors=5) 
model_knn.fit(xr_train, yr_train)
yr_predict = model_knn.predict(xr_test)
model_score_r3 = model_knn.score(xr_test, yr_test)
print(model_score_r3)
print(metrics.classification_report(yr_test, yr_predict))

'''


