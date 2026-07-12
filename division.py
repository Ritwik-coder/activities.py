print("Enter a Number (Numerator) :  ")
num = int(input())
print("Enter a Number(denominoter) :  ")
deno = int(input())
if num % deno == 0:
    print("\n" +str(num)+ "is divisible by " +str(deno))
else:
     print("\n" +str(num)+ "is not divisible by " +str(deno))