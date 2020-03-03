import os

def dirls(pdir):
    if os.path.isdir(pdir):
        ldir=os.listdir(pdir)
    else:
        print("dirls error")
    return(ldir)

def fpath(sdir, ndir):
#do full paths, need source path plus list with directory
    fdir=[]
    for i in ndir:
        if os.path.isdir(os.path.join(sdir, i)):
            fdir.append(os.path.join(sdir, i))
    return(fdir)
    

def backuplist(blist):
    xz=[]
    for i in blist:
        xz.append(i)
    return(xz)

srcdir="/home/voronkov/eclipse-workspace/1"
srcdir=os.path.abspath(srcdir)
deep=3

    
d=0
rootdir=dirls(srcdir)
blist=fpath(srcdir, rootdir)
z=[]
while d<deep:
    for i, j in enumerate(blist):
        x=dirls("/home/voronkov/eclipse-workspace/1/1d/a")
        print(x)
        y=fpath(j, x)
#         print(y)
        z=z+y
    d=d+1
    blist=z
    
print("blist:", blist, "\n", len(blist))




