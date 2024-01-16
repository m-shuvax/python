#-*-coding: utf-8-*-

def CheckID(id):
    if(len(id)!=9):
        return False
    
    CheckDigit=int(id[8])
    sum=0
    a=0
    
    for i in range(0,8,2):
        sum+=int(id[i])
        i+=1
        a=int(id[i])*2
        if(a<10):
            sum+=a
        else:
            sum+=1+a%10
            
    if(CheckDigit==(10-(sum%10)) or CheckDigit==0==sum%10):
        return True
    return False


id=input('Enter your ID number: ')
print(CheckID(id))




