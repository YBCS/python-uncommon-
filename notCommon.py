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