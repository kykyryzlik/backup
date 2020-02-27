import os

# def dirls(x):
#     if x:
#         a=os.listdir(x)
#         #dirls(x[0)
#     return(a)
# 

def dirls(x):
    a=os.walk(x)
    return(a)


docdir="//home//voronkov//eclipse-workspace"
dls=dirls(docdir)
print(dls)

for r, d, f in dls:
    print(r)
    print(d)
    print(f)
    print("---")