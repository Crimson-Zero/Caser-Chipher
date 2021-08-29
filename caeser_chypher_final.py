# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:56:36 2021

@author: wajee
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
           't', 'u', 'v', 'w', 'x', 'y', 'z']

def caser_chiper(string,shift,func):
    
    test=[]
    for char in string:
        if (char=='!' or char==',' or char=='?' or char==';' or char=='.' or char==" "):
            test.append(char)        
        else:
            if(func=='E' or func=='e'):
                
                  position=letters.index(char)
                  new_position=(position)+int(shift)
                  if(new_position>len(letters)-1):
                      new_position=(new_position % 26)
                      new_char=letters[new_position]
                      test.append(new_char)
                      
                  else:
                      new_char=letters[new_position]
                      test.append(new_char)
                  
            if(func=='D' or func=='d'):
                
                 position=letters.index(char)
                 
                 if(new_position>len(letters)-1):
                      new_position=(new_position % 26)
                      new_char=letters[new_position]
                      test.append(new_char)
                      
                 else:
                      new_char=letters[new_position]
                      test.append(new_char)
        
    print("Here is the resulting message")
    final="".join(test)
    return(final)

def main():
    String=input("Enter the string:")
    new_string=String.lower()
    print("Do you wish to encode or decode the message ? ")
    func=input("Press E for Encode and D for Decode:")
    key=input("Please provide the shift key number:")
    print(caser_chiper(new_string, key, func))

main()
    