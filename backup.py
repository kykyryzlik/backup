import os
import configparser

def ReadConfig():
    config = configparser.ConfigParser()
    FullPathConfig = os.path.join(os.getcwd(), "backup.cfg")
    if  os.path.isfile(FullPathConfig):
        config.read(FullPathConfig)
        BackupDir=config.get("Settings", "BackupDir")
        Deep=config.get("Settings", "Deep")
        BackupDir=os.path.abspath(BackupDir)
    else:
        config.add_section("Settings")
        config.set("Settings", "BackupDir", os.getcwd())
        config.set("Settings", "Deep", "0")
        ConfigFile=open(FullPathConfig, "w", encoding="utf-8")
        config.write(ConfigFile)
        
        BackupDir=config.get("Settings", "BackupDir")
        Deep=config.get("Settings", "Deep")
        
    return(BackupDir, Deep)

def tree(blist):
    backuplist=[]
    for dir_path, dir_names, file_names in os.walk(srcdir):
        if dir_path.count(os.sep) == srcdirdeep+deep:
            backuplist.append(dir_path)
        elif  dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+deep:
            backuplist.append(dir_path)
    return(backuplist)


srcdir,deep = ReadConfig()
srcdir=str(srcdir)
deep=int(deep)
print(type(srcdir), type(deep))
srcdir=os.path.abspath(srcdir)
srcdirdeep=srcdir.count(os.sep)

 
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


