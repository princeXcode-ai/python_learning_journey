import random
import string
# alpha ={
#     "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
# }
# num ={
#     "0","1","2","3","4","5","6","7","8","9"
# }

# spchar={
#     "!","@","#","$","%","^","&","*"


while True:
    alpha = random.choices(string.ascii_letters,k=5)
    num = random .choices(string.digits,k=3)
    spchar= random.choices("!@#$%^&*",k=2)
    
    password = alpha + num + spchar
    random.shuffle(password)
    password="".join(password)
    print("password is: ", password)
    
    user = input("\n do you want to anothor password? (YES/NO)") .strip().upper()
    
    if user == "NO":
        break
    
print("\n\n thanks for using Password generator \n\n BE YOURSELF")