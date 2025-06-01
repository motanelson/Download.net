
print("\033c\033[43;30m\ngive me a piramid size? ")
filesvar="""b,b,b,a,b,b
b,b,a,a,b,a
b,b,b,b,b,a
a,b,a,a,b,b
b,b,b,c,a,c
a,b,b,c,a,c
b,b,a,c,a,c
a,b,a,c,a,c"""

i=int(input())
print("\033[43;30m\ngive me a output file name? ")
filename=input()
filesvar=filesvar.replace("b",str(-(i//2)))
filesvar=filesvar.replace("a",str(i//2))
filesvar=filesvar.replace("c",str((0)))
fa=open(filename,"w") 
fa.write(filesvar)
fa.close()