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




# id=int (input (" input a ID " ))
# id=id
# CheckDigit=(id%10)
# i=(id//10)
# a=0
# b=0
# c=0

# while(i>0):
#     if( (a%2)==0):
#         b=( (i%10)*2)
#         if(b>9):
#             b=( 1+(b%10))
#     else:
#         b=(i%10)
#     a=a+1
#     c=c+b
#     i=i//10
    
# if( 10-(c%10)==CheckDigit) or (CheckDigit==0==(c%10) ):
#     print("Check digit is valid!")
# else:
#     print("Check digit is not valid!")
