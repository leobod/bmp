

from bmpentry.BMPModel.PicProcess import Handle
from bmpentry.BMPModel.PicProcess import Step1, Step2, Step3

class ProcessChain(Handle):

    def __init__(self):
        self.s1 = Step1()
        self.s2 = Step2()
        self.s3 = Step3()

        self.s1.nextHandle(self.s2)
        self.s2.nextHandle(self.s3)

    def doProcess(self, pic_dir, oid):
        self.s1.doProcess(pic_dir, oid)

