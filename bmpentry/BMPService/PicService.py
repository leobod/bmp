
from bmpentry.BMPModel.PicProcess import ProcessChain
from bmpentry.BMPService import HistoryService

class PicService:

    def __init__(self):
        pass

    def doChain(self, aid, imgfile):
        history = HistoryService()
        oid , tmpdir = history.createInitOrder(aid)
        tmpdir2 = tmpdir + "01.jpg"
        fobj = open(tmpdir2, 'wb')
        fobj.write(imgfile.read())
        fobj.close();

        process = ProcessChain()
        process.doProcess(tmpdir, oid)
