my_age = 29

print(f'I am {my_age} years old')

first_name= input('Please enter your first name:   ', )

last_name= input('Please enter your last name:   ', )

full_name = f'{first_name} {last_name}'

print(f'My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}')

temp_bool = input('Hey, wanna see what a temperature in Fahrenheit is converted to Celsuis? (y or n only please): ', )


if(temp_bool ==  'y'):
  temp_fahrenheit = input('What temperature Fahrenheit would you like to convert?: numbers only please:  ', )
  try:
    int(temp_fahrenheit)

  except:
    print('Please only provide an integer to be evaluated')
elif(temp_bool == 'n'):
  print('Awe shucks, perhaps next time :( ')
else:
  print('you entered the wrong input')

if(temp_fahrenheit):
  
  celsius = (int(temp_fahrenheit) - 32) * 5.0/9.0
  print(f'{temp_fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius....thank you and come on back to visit us again.')
