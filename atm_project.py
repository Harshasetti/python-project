name="harsha"
password="123"
user_name=input("enter your username:")
pass_word=input("enter your password:")
s='''
1.credit
2.debit
3,mini statement
4.exit
'''
amount=1000
if user_name==name and pass_word==password:
    print(s)
    option=int(input("enter the option:"))
    if option==1:
        credit_ammount=float(input("enter your ammount:"))
        print("ammount after credited",amount+credit_ammount)
    elif option==2:
        debit_ammount=float(input("enter your ammount:"))
        print("ammount after debited",amount-debit_ammount)
    elif option==3:
        print("ammount",amount)
else:
    print("in correct")


