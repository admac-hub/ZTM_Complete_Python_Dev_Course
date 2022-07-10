# Password checker 

#user input
username = input('what is your username login: ')
password = input('please type your password: ')

# functions behind the scenes that im using to give me the data i want to print 
password_length = len(password)
hide_password = '*' * len(password)

# return 
print(f'Hello {username}, your password {hide_password} is {password_length} characters long')