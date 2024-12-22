alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
option=int(input("choose 1 for encrypt or 2 for decrypt"))
n=int(input("enter the number:"))
w=input("enter the text:")
enc_text=[]
dec_text=[]
def encrypt(w,n):
    word=list(w.upper())
    for i in word:
        if(i==' '):
            enc_text.append(' ')
            continue
        p=alphabet.index(i)
        e=(p+n)%26
        x=alphabet[e]
        enc_text.append(x)
    cipher=""    
    for j in enc_text:
        cipher+=j
    print(cipher.lower())    

def decrypt(enc_text,n):
    my_str=""
    for i in enc_text:
        my_str+=i
    word1=list(my_str.upper())
    for i in word1:
        if(i==' '):
            dec_text.append(' ')
            continue
        f=alphabet.index(i)
        g=(f-n)%26
        y=alphabet[g]
        dec_text.append(y)
    
    decipher=""
    for j in dec_text:
        decipher+=j
    print(decipher.lower())
        
    
if (option==1):
    encrypt(w,n)   
else:
    decrypt(enc_text,n)
option=input("want to decrypt?(yes/no)")
if (option=='yes'):
    decrypt(enc_text,n)
else:
    print("THE END") 
    