# Iterate over a dictionary while having access to i, key and value: (super iteration)
l={"x":20, "k":30, "a":10}
# jt=list(l.items())
# print("this is jt list:\t \t",jt)
for i,jj in enumerate(list(l.items())):
	print("i:\t",i,jj)
	print("jj:\t",jj)