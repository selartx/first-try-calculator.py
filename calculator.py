#calculator program 
while(1):

 class calculate():
  print("**CALCULATOR**")
  print("1-Addition")
  print("2-subtraction")
  print("3-division")
  print("4-multiply")
  print("5-exponentiation")
  print("6-square root")
  print("7-factorial")
  print("8-rooting")
  calculating=int(input())
  no1=int(input("1. Sayıyı giriniz:"))
  no2=int(input("2. sayıyı giriniz:"))

 i=calculate()
 if i.calculating==1:
  addition=i.no1+i.no2
  print(addition)
 elif i.calculating==2:
  subtraction=i.no1-i.no2
  print(subtraction)
 elif i.calculating==3:
  division=i.no1/i.no2
  if i.no2==0:
   print("Error")
  else:
   print(division)
 elif i.calculating==4:
  multiply=i.no1*i.no2
  print(multiply)
 elif i.calculating==5:
  exponentiation=i.no1**i.no2
  print(exponentiation)
 elif i.calculating==6:
  print("1. Square Root:")
  squareroot1=i.no1**(1/2)
  print(squareroot1)
  print("2.Square Root")
  squareroot2=i.no2**(1/2)
  print(squareroot2)
 elif i.calculating==7:
  if i.no1<0:
   print("error")
  else:
   x=1
   factorial1=1
   while(x<=i.no1): 
    factorial1*=x
    x+=1
    print("1.Factorial:")
    print(factorial1)
  if i.no2<0:
   print("error")
  else:
   x=1
   factorial2=1
   while(x<=i.no2):
    factorial2*=x
    x+=1
    print("2.factorial:")
    print(factorial2)
 elif i.calculating==8:
  root=i.no1**(1/i.no2)
  print(root)
 else :
  print("error")