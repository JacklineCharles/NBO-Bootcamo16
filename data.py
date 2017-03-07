def data_type(n):
	if type(n) is str:
		return len(n)
	elif n==None:
		return "no value"
	elif type(n) is bool:
		return n
	elif type(n) is int:
	    if n<100:
	        return "less than 100"
	    elif n>100:
	        return "more than 100"
	    else:
	        return "equal to 100"
	elif type(n) is list:
	       if len(n)<3:
	           return None
	       else:	
	           return n[2] 
print(data_type([3,4,5,6]))	                           	
	    	
	    	