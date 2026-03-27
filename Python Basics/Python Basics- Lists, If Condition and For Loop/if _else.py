n=input("Enter a number: ")
n=int(n)
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
    
message=f"{n} is even" if n%2==0 else f"{n} is odd"
print(message)

