print("Hello World!")
# Finding the factorial using the recursion
def fact(num):
  if num==1:
    return 1
  else:
    return num* fact(num-1)
  
 num = int(input())
res = fact(num)
print(res)
