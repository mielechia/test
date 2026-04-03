#Loop
for i in range(3):                  #(from 0, count till before what number?)
    print(i)

for i in range(1, 5):               #(from 1, count till before what number?)
    print(i)

for i in range(0, 8, 2):            #(from 0, count till before what number?, in even 2,4,6,8)
    print(i)

#While Loop
count = 0                           #(count from what number?)
while count < 5:                    #(count less than 5)
    print(count)
    count += 1                      #(from 0, count adding 1 and accordinly)

#Loop control statement:
for i in range(10):
    if i == 3:
        continue                    #(Skip this iteration, skip 3)
    if i == 7:
        break                       #(Stop at this iteration, stop at 7)
    print(i)

#Nested Loop:
for i in range(2):                   #(Parent)
    for j in range(3):               #(Children)
        for m in range(2):              #(Grand Children)
            print(f"({i},{j},{m})")


#Exercise 

#Code

limit = 20

for num in range (2, limit + 1):
    prime = True

    for n in range (2, num):
        if num % n ==0:
            prime = False
            break
    
    if prime:
        print(num)

