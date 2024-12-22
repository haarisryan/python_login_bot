import random
list1=['apple','orange','carrot','strawberry','dragon','muscle','aircraft','engine','computer']
game_over=False
count=0
letters=[]
x=random.choice(list1)
#print(x)
y=int(len(x))
#print(y)
for i in range(y):
    letters.append('_')
print(letters)    

# split_word=x.split()
# print(split_word)
while not game_over:
    g=input("guess a letter:")
    if(g in x):
        
        for p in range(len(x)):
               let=x[p]
               if(g==let):
                  letters[p]=g
        print(letters)          
        if '_' not in letters:
            print("you win")  
            game_over=True
               
       
    else:
        count+=1
        if(count==1):
              print(" o ")
        elif(count==2):
            print(" o ")
            print(" | ")
        elif (count==3):
            print(" o ")
            print("/| ")
        elif(count==4):
            print(" o ")
            print("/|\\")
        elif(count==5):
            print(" o ")
            print("/|\\")
            print("/   ")
        else:
            print(" o ")
            print("/|\\")
            print("/ \\")
            print("you loose")
            break;
          