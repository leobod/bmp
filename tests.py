# Create your tests here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmp.settings")# project_name 项目名称
django.setup()

from bmpentry.BMPModel.PicProcess import Step3, ProcessChain


chain = ProcessChain()

chain.doProcess("static/data/16/4/", 4)

