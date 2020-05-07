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

def MakeTree(tree_srcdir,tree_deep,tree_excdir): #ROOT WRONG
    backuplist=[]
    exclist = tree_excdir.split()
#     print(exclist)
    srcdirdeep=tree_srcdir.count(os.sep)
    tree_deep=int(tree_deep)
    for dir_path, dir_names, files_names in os.walk(tree_srcdir):
        for i in exclist:
            if dir_path == i: 
#                 print(f' exc {dir_path}')
                dir_path=''
            
        if dir_path and dir_path.count(os.sep) == srcdirdeep+tree_deep:
#             if tree_excdir != dir_path:
#             print(f'1- dir_path   {dir_path}')
            backuplist.append(dir_path)
            for addfile in files_names:
                backuplist.append(os.path.join(dir_path, addfile))
#                 print(f'2- {os.path.join(dir_path, addfile)}')
            
        elif dir_path and dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+tree_deep:
#             if tree_excdir != dir_path:
            backuplist.append(dir_path)
#             backuplist.append(os.path.join(dir_path, file_names))
            
    return(backuplist)

def MakeArch(MakeArch_SrcDir ,MakeArch_DstDir, MakeArch_BackupList, ArchDate):
    MakeArch_DstDir = os.path.join(MakeArch_DstDir, ArchDate)
    for nowbkp in MakeArch_BackupList:
        base_name_src = os.path.join(MakeArch_SrcDir, nowbkp)
        base_name = nowbkp.replace(MakeArch_SrcDir, MakeArch_DstDir)
        root_dir = nowbkp
#         print("backuping ...", base_name)
        try:
            shutil.make_archive(base_name, "zip", root_dir)
            MakeLog(MakeArch_DstDir, f'Backuping... \n from \t {base_name_src} \n in {base_name} \n', ArchDate)
            MakeLog(MakeArch_DstDir, f'OK Archive \n from \t {base_name_src} \n in {base_name} \n\n', ArchDate)
            print(f'111 --- {root_dir}---{base_name_src} --- {base_name}')
        except Exception:
            MakeLog(MakeArch_DstDir, f'Backuping... \n from \t {base_name_src} \n in {base_name} \n', ArchDate, "ERRlog-")
            MakeLog(MakeArch_DstDir, f'NOT OK Archive \n from \t {base_name_src} \n in {base_name} \n\n', ArchDate, "ERRlog-")
            print(f'222 --- {root_dir}---{base_name_src} --- {base_name}')

def MakeLog(MakeLog_DstDir, WhatWrite, MakeLog_DateTime, MakeLog_NameLog="archivelog-"):
    if not os.path.isdir(MakeLog_DstDir):
        os.mkdir(MakeLog_DstDir)
    with open(os.path.join(MakeLog_DstDir, MakeLog_NameLog + MakeLog_DateTime + '.log'), 'a+') as ArchiveLog:
        ArchiveLog.write(WhatWrite)
    

def MakeDateTime():
    DT = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    return(DT)

def main_backup():

# get date and time
    datetime = MakeDateTime()

# read form config
    srcdir,dstdir,deep,excdir = ReadConfig()

# make list for backup 
    backuplist=MakeTree(srcdir, deep, excdir)
#      = MakeExcept(backuplist)

# make archive
#     print(backuplist)
    print(f"Backup START on {MakeDateTime()}")
    MakeLog(os.path.join(dstdir, datetime), f"Backup START on {MakeDateTime()} \n", datetime)
    MakeArch(srcdir, dstdir, backuplist, datetime)
    MakeLog(os.path.join(dstdir, datetime), f"Backup END on {MakeDateTime()} \n", datetime)
    print(f"Backup END on {MakeDateTime()}")

main_backup()
 



