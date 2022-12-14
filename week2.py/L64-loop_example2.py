# clalculate the sum of digit
# num, is 1256
total = 0
num = input("enter a number : ")
for i in range(0, len(num)):
    total += int(num[i])
    print(total)
    #logic
    # num = "1256" , length = 4
    # int(num[0]) ---->1
    # int(num[1]) ----> 
    #int(num[2]) --->5
    #int(num[3]) ----6
    # i ---- 0 to 3