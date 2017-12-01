import os
import shutil
alllist=os.listdir(u"D:\\learn\\1709\\")
for i in alllist:
    aa,bb=i.split(".")
    if 'rp' in bb.lower():
        oldname= u"D:\\learn\\170901\\"+aa+"."+bb
        newname=u"D:\\learn\\170901\\rpfile\\"+aa+"."+bb
        shutil.copyfile(oldname,newname)
