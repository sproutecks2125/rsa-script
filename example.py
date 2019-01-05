def prime_num (x, y):
    # Python program to display all the prime numbers within an interval

    # change the values of lower and upper for a different result
    lower = x
    upper = y

    print("Prime numbers between",lower,"and",upper,"are:")

    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               print(num)


def d_val (e, t, x, y):
    d = list(filter(lambda x: x * e % t == 1, range(x, y)))
    print(d)

#x = int(input("Enter the lower number: \n"))
#y = int(input("Enter the upper number: \n"))
#prime_num(x,y)
#d_val(47, 15840, x, y)

c_vals = [3954, 3634, 10591, 13428, 10591, 3911, 10534, 1873, 13428, 15075, 2540, 5050, 2540]
for e in c_vals:
    m = e ** 15503 % 15840
    print(m, " ")
