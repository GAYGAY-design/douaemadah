a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a==0 and b==0 and c==0 :
    print("x=R")  
elif a==0 and b==0 and c!=0 :
    print("pas de solution")
else :
    print("x=-c/b") 
if  a!=0 and b!=0 and c!=0 :
    delta=b**2 -4*a*c
    if delta==0 :
        print("x=-b/2*a")
    elif delta>0 :
        print("x1=(-b-sqrt(delta))/2*a")
        print("x2=(-b+sqrt(delta))/2*a")
    else :
        print("pas de solution")    