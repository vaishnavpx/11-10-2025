def total_calc(subtotal):
    onepercenttip=subtotal/100
    total=onepercenttip+subtotal
    print(f"Your total is {total}")
    
subtotal=int(input("Enter a subtotal: "))

total_calc(subtotal)