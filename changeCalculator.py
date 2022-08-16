#Danial Syed
x = int(input("Enter the number of cents: "))
hd = x//50
q_a = x%50
q = q_a//25
q_b = q_a%25
d = q_b//10
q_c = q_b%10
n = q_c//5
q_d = q_c%5
p = q_d//1
print (hd,"half dollars\n",q,"quarters\n",d,"dimes\n",n,"nickels\n",p,"pennies\n")
