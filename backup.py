import os
import configparser

deep=1
# if last simvol is / delete him
srcdir="/home/kyk/wine/os/windows"
srcdir=os.path.abspath(srcdir)
srcdirdeep=srcdir.count(os.sep)

def ReadOrCreateConfig(pathConfig):
    config = configparser.ConfigParser()
#      NEED try construct
    FullPath = os.path.abspath(os.path.join(pathConfig, "backup.cfg"))
    if os.path.exists(FullPath):
        srcdir=config.get("Settings", "BackupDir")
        deep=config.get("Settings", "Deep")
    else:
        config.add_section("Settings")
        config.set("Settings", "BackupDir", ".")
        config.set("Settings", "Deep", "0")
    ConfigFile=open(os.path.abspath(os.path.join(pathConfig, "backup.cfg")), "w", encoding="utf-8")
    config.write(ConfigFile)
    

ReadOrCreateConfig(os.getcwd())




def tree(blist):
    backuplist=[]
    for dir_path, dir_names, file_names in os.walk(srcdir):
        if dir_path.count(os.sep) == srcdirdeep+deep:
            backuplist.append(dir_path)
        elif  dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+deep:
            backuplist.append(dir_path)
    return(backuplist)

 
b=tree(srcdir)
for i in b:
    print(i)

print("--- len IS ", len(b))    
    
    
    
    

# def dirls(pdir):
# # do list dir, need list of directories     
#     dlist=[]
#     flist=[]
#     if os.path.isdir(pdir):
#         ldir=os.listdir(pdir)
#         for i in ldir:
#             if os.path.isdir(os.path.join(pdir, i))==True:
#                 dlist.append(i)
#             elif os.path.isdir(os.path.join(pdir, i))==False:
#                 flist.append(i)
#     return(dlist, flist)
#     
# 
# def fpath(sdirs):
# # do full paths, need source path list AND list with directory`s and files names
#     fdir=[]
#     ffil=[]
#     for src in sdirs:
#         ld,lf=dirls(src)
#         for ndir in ld:
#             fdir.append(os.path.join(src, ndir))
#         for nfil in lf:
#             ffil.append(os.path.join(src, nfil))
#     return(fdir, ffil)


