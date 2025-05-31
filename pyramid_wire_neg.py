
print("\033c\033[43;30m\ngive me a piramid size? ")
filesvar="""b,a,b,a,a,b
a,a,b,a,a,a
a,a,a,b,a,a
b,a,a,b,a,b
b,a,b,c,c,c
a,a,b,c,c,c
a,a,a,c,c,c
b,a,a,c,c,c"""

i=int(input())
print("\033[43;30m\ngive me a output file name? ")
filename=input()
filesvar=filesvar.replace("b",str(-(i//2)))
filesvar=filesvar.replace("a",str(i//2))
filesvar=filesvar.replace("c",str((0)))
fa=open(filename,"w") 
fa.write(filesvar)
fa.close()