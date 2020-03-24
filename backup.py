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
#     print(srcdirdeep)
elif os.name == 'posix':
    srcdir="~"

deep=2
# print("now deep is:", srcdirdeep, "\n", "need deep:", deep, "\n-----\n", adeep, "\n-----")


def tree(blist):
    backuplist=[]
    for dir_path, dir_names, file_names in os.walk(srcdir):
        if  dir_names == []:
            dir_path_deep=dir_path.split(sep="\\")
            print(dir_path_deep)
            qwe=os.path.join(dir_path_deep[0], os.sep, dir_path_deep[1], dir_path_deep[2])
            print(qwe)
            backuplist.append(os.path.abspath(qwe))
#dir_path.count("\\") < deep and
#         elif dir_path.count("\\") < deep and dir_names != []:
#             backuplist.append(os.path.abspath(dir_path))
#         print(dir_path)
    return backuplist
 
b=tree(srcdir)
print("\n-----", len(b))
for i in b:
    print(i)
    
    
    
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




