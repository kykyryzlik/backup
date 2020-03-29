import os
import configparser
import shutil
import datetime

def ReadConfig():
    config = configparser.ConfigParser()
    NameFileConfig="backup.cfg"
    FullPathConfig = os.getcwd()
    FullPathConfigFile = os.path.join(FullPathConfig, NameFileConfig)
    if  os.path.isfile(FullPathConfigFile):
        config.read(FullPathConfigFile)
        SrcDir = config.get("Settings", "SrcDir")
        Deep = config.get("Settings", "Deep")
        DstDir = config.get("Settings", "DstDir")
        SrcDir=os.path.abspath(SrcDir)
    else:
        config.add_section("Settings")
        config.set("Settings", "SrcDir", os.getcwd())
        config.set("Settings", "Deep", "0")
        config.set("Settings", "DstDir", os.getcwd())
        ConfigFile=open(os.path.join(FullPathConfig, "backup.cfg.default"), "w", encoding="utf-8")
        config.write(ConfigFile)
        print("Please rename backup.cfg.default to backup.cfg and edit this")
        exit()
    return(SrcDir, Deep, DstDir)

def tree(blist): #ROOT WRONG
    backuplist=[]
    for dir_path, dir_names, file_names in os.walk(srcdir):
        if dir_path.count(os.sep) == srcdirdeep+deep:
            backuplist.append(dir_path)
        elif  dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+deep:
            backuplist.append(dir_path)
    return(backuplist)

def MakeArch(DstDir, SrcDir):
#     ArchName = SrcDir.split(os.sep)[-1]
    ArchName = SrcDir.split(os.sep)[-1]
    print(ArchName)
    ArchDate = str(datetime.datetime.now())
    print(ArchDate)
    shutil.make_archive(os.path.join(DstDir, ArchName), "zip", SrcDir)

### Read config
srcdir,deep,dstdir = ReadConfig()
srcdir=str(srcdir)
deep=int(deep)
dstdir=str(dstdir)
srcdir=os.path.abspath(srcdir)
dstdir=os.path.abspath(dstdir)
srcdirdeep=srcdir.count(os.sep)

### Make list of Backup Directories 
backuplist=tree(srcdir)

### Archive Directories from backuplist

for nowbkp in backuplist:
    MakeArch(dstdir, nowbkp)
 
 

for i in backuplist:
    print(i)

print("--- len IS ", len(backuplist))    
    
    
    
    

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


