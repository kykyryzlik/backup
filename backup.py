import os
import configparser
import shutil
import datetime
import logging
from os.path import isfile
# logging.basicConfig(filename="sample.log", level=logging.INFO)

def ReadConfig():
    config = configparser.ConfigParser()
    NameFileConfig="backup.cfg"
    FullPathConfig = os.getcwd()
    FullPathConfigFile = os.path.join(FullPathConfig, NameFileConfig)
    if  os.path.isfile(FullPathConfigFile):
        config.read(FullPathConfigFile, encoding="utf-8")
        SrcDir = config.get("Settings", "DocumentDir")
        DstDir = config.get("Settings", "BackupDir")
        Deep = config.get("Settings", "Deep")
        ExDir = config.get("Settings", "except_documentdir")
        SrcDir=os.path.abspath(SrcDir)
        DstDir=os.path.abspath(DstDir)
        ExDir=os.path.abspath(ExDir)
        print("------------------", ExDir)
    else:
        config.add_section("Settings")
        config.set("Settings", "DocumentDir", os.getcwd())
        config.set("Settings", "BackupDir", os.getcwd())
        config.set("Settings", "Deep", "0")
        config.set("Settings", "except_documentdir", '')
        ConfigFile=open(os.path.join(FullPathConfig, "backup.cfg.default"), "w", encoding="utf-8")
        config.write(ConfigFile)
        print("Please rename backup.cfg.default to backup.cfg and edit this")
        exit()
    return(SrcDir, DstDir, Deep, ExDir)

# def ex_tree(ex_tree_backuplist, ex_tree_exdir):
#     ex_backuplist=[]
#     for i in ex_tree_backuplist:
#         if i != ex_tree_exdir:
#             ex_backuplist.append(i)
#         print(i, "---", ex_tree_exdir)
#     return(ex_backuplist)

def tree(tree_srcdir,tree_deep,tree_exdir): #ROOT WRONG
    backuplist=[]
    srcdirdeep=tree_srcdir.count(os.sep)
    tree_deep=int(tree_deep)
    for dir_path, dir_names, file_names in os.walk(tree_srcdir):
        if dir_path.count(os.sep) == srcdirdeep+tree_deep:
            if tree_exdir != dir_path:
                backuplist.append(dir_path)
        elif  dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+tree_deep:
            if tree_exdir != dir_path:
                backuplist.append(dir_path)
    return(backuplist)

def MakeArch(MakeArch_SrcDir ,MakeArch_DstDir, MakeArch_BackupList, ArchDate):
#     ArchDate = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    MakeArch_DstDir = os.path.join(MakeArch_DstDir, ArchDate)
#     if not os.path.isdir(MakeArch_DstDir):
#         os.mkdir(MakeArch_DstDir)
#     ArchiveLog=open(os.path.join(MakeArch_DstDir, 'archivelog-' + ArchDate + '.log'), 'a+', encoding='utf-8')
#     with open(os.path.join(MakeArch_DstDir, 'archivelog-' + ArchDate + '.log'), 'a+') as ArchiveLog:
    for nowbkp in MakeArch_BackupList:
        base_name = nowbkp.replace(MakeArch_SrcDir, MakeArch_DstDir)
        root_dir = nowbkp
        print("backuping ...", base_name)
#         ArchiveLog.write(f'Backuping ... {base_name} \n')
        MakeLog(MakeArch_DstDir, f'Backuping ... {base_name} \n')
        try:
            shutil.make_archive(base_name, "zip", root_dir)
            MakeLog(MakeArch_DstDir, f'\tOK Archive {base_name} \n')
#             ArchiveLog.write(f'\tOK Archive {base_name} \n')
        except Exception:
            print(f'kyExceptError base_name = {base_name}, root_dir =  {root_dir}')
            MakeLog(MakeArch_DstDir, f'\tNOT OK Archive {base_name} \n')
#             ArchiveLog.write(f'\tNOT OK Archive {base_name} \n')
#     ArchiveLog.close()

def MakeLog(MakeLog_DstDir, WhatWrite):
    if not os.path.isdir(MakeLog_DstDir):
        os.mkdir(MakeLog_DstDir)
    with open(os.path.join(MakeLog_DstDir, 'archivelog.log'), 'a+') as ArchiveLog:
        ArchiveLog.write(WhatWrite)
    

def MakeDateTime():
    DT = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
#     MakeArch_DstDir = os.path.join(MakeArch_DstDir, ArchDate)
    return(DT)

def main_backup():
    datetime = MakeDateTime()
# read form config
    srcdir,dstdir,deep,exdir = ReadConfig()
# make list for backup 
    backuplist=tree(srcdir, deep, exdir)
#     ex_backuplist = ex_tree(backuplist, exdir)

# make archive
    MakeArch(srcdir, dstdir, backuplist, datetime)
    MakeLog(dstdir, "Backup THE END")
    print("Backup THE END")
#### 
#     print("\n--- len IS ", len(backuplist))
#     for i in backuplist:
#         print(i)



main_backup()
 



