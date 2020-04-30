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
        print("backuping ...", base_name)
        shutil.make_archive(base_name, format, root_dir)

def main_backup():
# read form config
    srcdir,dstdir,deep,exdir = ReadConfig()
# make list for backup 
    backuplist=tree(srcdir, deep, exdir)
#     ex_backuplist = ex_tree(backuplist, exdir)

# make archive
    MakeArch(srcdir, dstdir, backuplist)
    print("Backup THE END")
#### 
#     print("\n--- len IS ", len(backuplist))
#     for i in backuplist:
#         print(i)



main_backup()
 



