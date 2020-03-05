import os

def dirls(pdir):
    if os.path.isdir(pdir):
        ldir=os.listdir(pdir)
    else:
        print("input str or list")
    return(ldir)

def fpath(sdirs):
#do full paths, need source path list AND list with directory`s name
    fdir=[]
    for src in sdirs:
        if os.path.isdir(src):
            ld=dirls(src)
            for ndir in ld:
                if os.path.isdir(os.path.join(src, ndir)):
                    fdir.append(os.path.join(src, ndir))
    return(fdir)
    

def backuplist(blist):
    xz=[]
    for i in blist:
        xz.append(i)
    return(xz)

srcdir=["/home/voronkov/yandex-disk", "/home/voronkov/torrents"]

y=fpath(srcdir)
print(y, "\n", len(y))

x=fpath(y)
print(x, "\n", len(x))

    

    


