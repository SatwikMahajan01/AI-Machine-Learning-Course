indian=["samosa","daal","naan"]
chinese=["egg roll","fried rice","dim sum"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish: ")
if dish in indian:
    print(f"{dish} is an indian dish")
elif dish in chinese:
    print(f"{dish} is an chinese dish")
elif dish in italian:
    print(f"{dish} is an italian dish")
else:
    print(f"{dish} is not a valid dish")