number_1 = input("Insert firtst number :") #user 1  select number 1
number_2 = input("insert second number :") #user 2 select number 2 
opration = input("select a opration +,-,*,/ :") #on of them select a operation

if opration == "+": #if user select +  resault = number_1 + number_2
    resault = float(number_1) + float(number_2)

elif opration == "-":#if user select -  resault = number_1 - number_2
    resault = float(number_1) - float(number_2)

elif opration == "*":#if user select *  resault = number_1 * number_2
    resault = float(number_1) * float(number_2)

elif opration == "/":#if user select /  resault = number_1 / number_2
    resault = float(number_1) / float(number_2)

else:#if user enter a false operation this massage will show
    resault = "this is false"

print(resault)# and print resault



