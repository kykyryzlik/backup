import os

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



if os.name == 'nt':
    srcdir=os.path.abspath("e:\dlna")
    srcdirdeep=srcdir.count("\\")
elif os.name == 'posix':
    srcdir="~"

deep=3
adeep=deep-srcdirdeep
print("now deep is:", srcdirdeep, "\n", "need deep:", deep, "\n-----\n", adeep, "\n-----")


def tree(blist):
    backuplist=[]
    for dir_path, dir_names, file_names in os.walk(srcdir):
        if  dir_path.count("\\") == srcdirdeep:
            print(dir_path)
#             backuplist.append(dir_path)
        elif dir_path.count("\\") < deep and dir_names == []:
            print("---2 ELIF---", dir_path, "---", dir_names)
#         elif dir_path.count("\\") < adeep and dir_names != []:
#             print("---3 ELIF---", dir_path, "---", dir_names)
    return backuplist
 
b=tree(srcdir)
print(b)
    
    
    
###############
# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1
# 
# asd=countdown(10)
# print(next(asd))
# print(next(asd))
# print("-------------")
# for h in asd:
#     print(h)




