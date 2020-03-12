import os
import pandas as pd

def dirls(pdir):
# do list dir, need list of directories     
    dlist=[]
    flist=[]
    if os.path.isdir(pdir):
        ldir=os.listdir(pdir)
        for i in ldir:
            if os.path.isdir(os.path.join(pdir, i))==True:
                dlist.append(i)
            elif os.path.isdir(os.path.join(pdir, i))==False:
                flist.append(i)
    return(dlist, flist)
    

def fpath(sdirs):
# do full paths, need source path list AND list with directory`s and files names
    fdir=[]
    ffil=[]
    for src in sdirs:
        ld,lf=dirls(src)
        for ndir in ld:
            fdir.append(os.path.join(src, ndir))
        for nfil in lf:
            ffil.append(os.path.join(src, nfil))
    return(fdir, ffil)

# def backuplist(blist):
#     xz=[]
#     for i in blist:
#         xz.append(i)
#     return(xz)

# srcdir=["/home/voronkov/yandex-disk", "/home/voronkov/torrents"]
# srcdir=["/home/voronkov/disk_V"]
#srcdir=["/home/voronkov/eclipse-workspace"]
# srcdir=["E:\dlna", "E:\downloads"]
srcdir="E:\downloads"
# srcdir=["E:\dlna"]
# srcdir=["E:\downloads"]

# sd=srcdir
# n=0
# while n<2:
#     z=fpath(sd)
#     sd=z
#     n=n+1
# 
# print(sd, "\n", len(sd))

########
# x,y=fpath(srcdir)
# print(x, "\n", len(x))
# print(y, "\n", len(y))

alltree=os.walk(srcdir)


for root, dirs, files in alltree:
#     print(root, dirs, files)
    if files:
        print(root)

# print(merge_data)

