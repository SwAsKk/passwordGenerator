import random


lower_case = "abcdefghijklmnopqrstuvwyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
digit = "1234567890"
symbols = "@#$%^&/\?"
Use_fir =lower_case+upper_case+digit+symbols

length_for_pass = int(input("Length of password: "))
    

password = "".join(random.sample(Use_fir,length_for_pass))



print("Your generated password is: " + password)
