
upper_interval = 5000
lower_interval = 100
print("Armstrong numbers in given interval:")

for num in range(lower_interval, upper_interval + 1):

   order = len(str(num))

   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
     print(num)


     
