#A Reverse Cipher program  
message =  input("enter the text :\t") 
translated = ""  
i = len(message)  -  1   
while  i >=  0 :   
         translated = translated + message[i]      
         i  =  i  -  1
print("\n output :- \n")
print(translated)