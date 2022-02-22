import greeting

greeting.display_greeting()

hours_worked = 45

pay_rate = 15
 
over_time_rate = 1.5

if(hours_worked > 40):
  extra_hours = hours_worked - 40
  over_time = extra_hours * pay_rate * over_time_rate
  total_pay = 40 * pay_rate + over_time
else:
  total_pay = hours_worked * pay_rate




print(total_pay)

# ================================================
i=1
while i <= 5:
  print(i)
  i += 1

word = input('enter a word:')


for char in word:
  print(char)

# =================================================

def run_calculations():
  print(add_two_numbers(3,5))
  print(subtract_two_numbers(10,2))
  print(multiply_two_numbers_and_divide(5,8,2))

def add_two_numbers(num1, num2):
  result = num1 + num2
  return result

def subtract_two_numbers(num, num2):
  result = num1 - num2
  return result

def multiply_two_numbers_and_divide(num1, num2, num3):
  result = (num1 * num2)/num3
  return result



run_calculations()

def add_all_odd_numbers(numbers):
  grand_total = 0
  for val in numbers:
    if val % 2 != 0:
      grand_total += val
  return grand_total  


print('here it is===>',add_all_odd_numbers([1,2,1,4,3,3,2,4]))    

def sum_mul(n, m):
    if m < n or n == 0:
        return 'INVALID'
    current_value = n
    result = 0
    while current_value < m:
        result += current_value
        current_value = n + current_value
    if result == 0:
        return 'INVALID'
    else:
         return result    

print(sum_mul(941,382))



a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)


a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)



#============================================================





  