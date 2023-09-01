import os
def GetPath(path,key='csv'):
    if(os.path.exists(path)==True):
        filelist=[]
        for i in os.listdir(path):
            if(key in i and i.find('.crc')==-1):
                filelist.append(path+i)
        if(len(filelist)==1):
            return filelist[0]
        return filelist
    else:
        return []