import random

bintypeslist = ['bit','binary']
engli_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbertypeslist = ['real','smallint','integer','int','float','numeric','number','bigint','money','smallmoney']
varchartypeslist = ['char','nchar','nvarchar2','varchar2','varchar','tynitext','text']
datetimetypeslist = ['time','date','datetime','datetime2','smalldatetime','timestamp','year','datetimeoffset']

init_var = 0
end = []
print('pls, enter value types')
types = [str(intype) for intype in input().split()]  #input types into massive
print(types)
print('pls, enter varchar length')
varlen = [int(intype) for intype in input().split()] #input lenght of varchar types into massive
print(varlen)
print('how much strings')
iterationamount = int(input())

def str_generator():
	global init_var
	var = ''
	for i in range(0,varlen[init_var]):
		var += random.choice(engli_alphabet)
	init_var+=1
	return(var)
def int_generator():
	var = random.randrange(0,1000)
	return(var)
def dtm_generator():
	var = ''
	var += str(random.randrange(1900,2018)) + '-' + str(random.randrange(1,12)) + '-' + str(random.randrange(1,25))
	return(var)
def bin_generator():
	var = random.randrange(0,1)
	return(var)
def looper(types):
	op_mass = []
	for i in range(0,len(types)):
		if types[i] in varchartypeslist:
			op_mass.append(str_generator())
		elif types[i] in numbertypeslist:
			op_mass.append(int_generator())
		elif types[i] in datetimetypeslist:
			op_mass.append(dtm_generator())
		elif types[i] in bintypeslist:
			op_mass.append(bin_generator())
		else:
			op_mass.append('ERROR')
			print(i,'- index',types[i],' - not the sql type')
	return(op_mass)
while iterationamount !=0:
	init_var = 0
	end.clear()
	end.append(looper(types))
	print(end)
	iterationamount -=1

