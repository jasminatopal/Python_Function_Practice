# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max(a,b,c)

print(max_num(12, 22, 7))



# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    product = list[0]

    if len(list) == 0:
        return 0
    if len(list) > 0:
        for i in list:
            product = product * i
    return product

print(mult_list([11,15,7,6]))


# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

print(rev_string("Good morning"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, beg_range, end_range):
    return beg_range <= num <= end_range

result = num_within(5, -3, 7)
print(result)  

result = num_within(10,2,5)
print(result)  

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal_triangle(n):
   frow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(frow)
      frow=[l+r for l,r in zip(frow+y, y+frow)]
   return n>=1
pascal_triangle(4) 




