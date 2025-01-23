d={}
ans="yes"
while ans=="yes" :
    p_name=input("enter the product name:")
    p_price=float(input("enter the product price:"))
    d[p_name]=p_price
    ans=input("do you want to enter the product names ?yes or no:")
ans="yes"
while ans=="yes":
    p_name=input("enter the product name to search:")
    print("price:",d.get(p_name,"item not available"))
    ans=input("do you want to know the product to search?yes or no:")
