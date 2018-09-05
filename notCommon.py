## Variables for all version
a = [1,2,3,4]
b = [8,7,9,2,1]

c = []

##########################
##Version 1

def loop_to_check(e,f):				
		for i in range(len(e)):			
			if e[i] not in f:			
				c.append(e[i])			
										
loop_to_check(a,b)					
loop_to_check(b,a)					
										
print(c)								
###########################

##########################
##Version 2

def disjoint(e,f):
	c = e[:]
	d = f[:]
	for i in range(len(e)):
		for j in range(len(f)):
			if e[i] == f[j]:
				c.remove(e[i])
				d.remove(d[j])
	final = c + d
	print(final)

print(disjoint(a,b))							
###########################