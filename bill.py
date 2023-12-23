
produt={"cold drink":170,"energy drink":330,"chicken":290,"beef":550,"chai":60,"roti":25,"candy":30,"sugar":120,"oil":450}
price={}

while True:
    items=input("enter a product or type'done' to exit: ")
    if items == 'done':
        print("thanks!!!")
        break
    elif items in produt:
        quantity=int(input("enter the quantity: "))
        price[items]=produt[items]*quantity
    else:
        print("product not avaiable!!")
total=sum(price.values())
print("total price - ",total,"rupees")
    
