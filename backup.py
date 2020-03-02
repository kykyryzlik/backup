import os

def dirls(pdir):
    if pdir:
        ldir=os.listdir(pdir)
        for i, j in enumerate(ldir):
            if os.path.isdir(os.path.join(pdir,j)):
                ldir[i]=os.path.join(pdir,j)
            else: 
                ldir.pop[i]
    #print(ldir[0])
    #dirls(ldir[0])
    

    return(ldir)
    
srcdeep=3
deep=1
srcdir="/home/voronkov/eclipse-workspace"
srcdir=os.path.abspath(srcdir)
dls=dirls(srcdir)
#print(dls)

print(dirls(dls[0]))

# bdir=[]
# for n in dls:
#     if os.path.isdir(n) and deep>0:
#         bdir.append(dirls(n))
#     deep = deep-1
#         
# print(bdir)