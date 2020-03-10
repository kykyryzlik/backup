import os

def dirls(pdir, FileOrDir):
    dlist=[]
    flist=[]
    if os.path.isdir(pdir) and FileOrDir=='D':
        ldir=os.listdir(pdir)
        for i in ldir:
            if os.path.isdir(os.path.join(pdir, i)):
                dlist.append(i)
        return(dlist)
    
    elif os.path.isdir(pdir)==False and FileOrDir=='F':
        lfil=os.listdir(pdir)
        print("aaaaaaaaa", type(lfil))
        for j in lfil:
            #os.path.join(pdir, j)
            flist.append(j)
    return(dlist, flist)
    

def fpath(sdirs):
#do full paths, need source path list AND list with directory`s name
    fdir=[]
    ffil=[]
    for src in sdirs:
        ld=dirls(src, 'D')
        for ndir in ld:
            fdir.append(os.path.join(src, ndir))
        lf=dirls(src, 'F')
        print(type(lf))
        for nfil in lf:
            print("222222222222222")
            ffil.append(os.path.join(src, nfil))
    return(fdir, ffil)

# def backuplist(blist):
#     xz=[]
#     for i in blist:
#         xz.append(i)
#     return(xz)

# srcdir=["/home/voronkov/yandex-disk", "/home/voronkov/torrents"]
# srcdir=["/home/voronkov/disk_V"]
srcdir=["/home/voronkov/eclipse-workspace"]


# sd=srcdir
# n=0
# while n<2:
#     z=fpath(sd)
#     sd=z
#     n=n+1
# 
# print(sd, "\n", len(sd))

x,y=fpath(srcdir)
print(x, "\n", len(x))
print(y, "\n", len(y))




