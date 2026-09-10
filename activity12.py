import getpass 

username = 'deleon'
password = '123456789'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')

if username == u and p == password : 			
	print("ACCESS GRANTED")
else: 
	print("ACCESS DENIED")