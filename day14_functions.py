def square(x):
    return x*x

print(square(5))

def is_even(n):
    if n % 2 == 0:
        return n
    else:
        return None
print(is_even(4))
print(is_even(7))
    
def factorial(n):
  factorial = 1
  while n > 0:
    factorial *= n
    n -= 1
  return factorial

print(factorial(5))

def greet_user(name, age):
   print(f"Привет, {name}. Тебе {age} лет.")
greet_user("Андрей", 26)


def avg(*nums):
    return sum(nums) / len(nums)
print(avg(1,2,3,4,5))