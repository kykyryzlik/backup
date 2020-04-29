import os
import configparser
import shutil
import datetime
import logging
# logging.basicConfig(filename="sample.log", level=logging.INFO)

def ReadConfig():
    config = configparser.ConfigParser()
    NameFileConfig="backup.cfg"
    FullPathConfig = os.getcwd()
    FullPathConfigFile = os.path.join(FullPathConfig, NameFileConfig)
    if  os.path.isfile(FullPathConfigFile):
        config.read(FullPathConfigFile)
        SrcDir = config.get("Settings", "DocumentDir")
        DstDir = config.get("Settings", "BackupDir")
        Deep = config.get("Settings", "Deep")
        SrcDir=os.path.abspath(SrcDir)
    else:
        config.add_section("Settings")
        config.set("Settings", "DocumentDir", os.getcwd())
        config.set("Settings", "BackupDir", os.getcwd())
        config.set("Settings", "Deep", "0")
        ConfigFile=open(os.path.join(FullPathConfig, "backup.cfg.default"), "w", encoding="utf-8")
        config.write(ConfigFile)
        print("Please rename backup.cfg.default to backup.cfg and edit this")
        exit()
    return(SrcDir, DstDir, Deep)

def tree(tree_srcdir,tree_deep): #ROOT WRONG
    backuplist=[]
    srcdirdeep=tree_srcdir.count(os.sep)
    tree_deep=int(tree_deep)
    for dir_path, dir_names, file_names in os.walk(tree_srcdir):
        if dir_path.count(os.sep) == srcdirdeep+tree_deep:
            backuplist.append(dir_path)
        elif  dir_names == [] and  dir_path.count(os.sep) <= srcdirdeep+tree_deep:
            backuplist.append(dir_path)
    return(backuplist)

def MakeArch(MakeArch_SrcDir ,MakeArch_DstDir, MakeArch_BackupList):
    ArchDate = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    MakeArch_DstDir = os.path.join(MakeArch_DstDir, ArchDate)
    for nowbkp in MakeArch_BackupList:
        base_name = nowbkp.replace(MakeArch_SrcDir, MakeArch_DstDir)
        format = "zip"
        root_dir = nowbkp
#         base_dir = '' 
#         verbose = ''
#         dry_run = ''
#         owner = ''
#         group = ''
#         logger = ''
#         shutil.make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group, logger)
        shutil.make_archive(base_name, format, root_dir)

def main_backup():
# read form config
    srcdir,dstdir,deep = ReadConfig()

# make list for backup 
    backuplist=tree(srcdir, deep)

# make archive
    MakeArch(srcdir, dstdir, backuplist)

#### 
#     print("\n--- len IS ", len(backuplist))
#     for i in backuplist:
#         print(i)



main_backup()
 



