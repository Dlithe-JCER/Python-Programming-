# Custom Exception 

class InsufficientBal(Exception):
    pass
bal=90
amt=100
try:
    if(bal<amt):
        raise InsufficientBal()
    else:
        print('Debited Sucessfully')
except:
    print("check balance")
    
