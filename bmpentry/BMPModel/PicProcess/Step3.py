import pandas as pd
from sklearn.externals import joblib
import numpy as np
from sklearn import svm

from bmpentry.BMPService import HistoryService
from bmpentry.BMPModel.PicProcess.Handle import Handle

class Step3(Handle):

    def __init__(self):
        pass

    def doProcess(self, pic_dir, oid):
        history = HistoryService()
        rr, rg, ro = history.queryRatio(oid)
        resultab = self.predictAB(rr, rg)
        resultall = self.predictAll(rr, rg, ro)
        history.updateResult(oid, resultab, resultall)
        print("Chain 003 execute")

    def predictAB(self, RatioR, RatioG):
        data = {
            'RatioR': [RatioR],
            'RatioG': [RatioG],
        }
        frame = pd.DataFrame(data)
        clf = joblib.load('bmpentry/BMPModel/PicProcess/mmodel/PredictAB.m')
        res = clf.predict(frame)
        return res

    def predictAll(self, RatioR, RatioG, RatioBg):
        data = {
            'RatioR': [RatioR],
            'RatioG': [RatioG],
            'RatioBg': [RatioBg],
        }
        frame = pd.DataFrame(data)
        clf = joblib.load('bmpentry/BMPModel/PicProcess/mmodel/PredictAll.m')
        res = clf.predict(frame)
        return res
