#!/usr/bin/env python
# coding: utf-8

def shift_letter(letter, shift):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if letter==" ":
            new_letter=" "
            return(new_letter)
    else:
        new_letter=alphabet_list[(alphabet_list.index(letter)+shift)%26]
        print(new_letter)
        return(new_letter)
    
letters=str(input("Add a letter:"))
shifts=int(input("How many shifts to the right?:"))

shift_letter(letters.upper(), shifts)
    
    
    def caesar_cipher(message, shift):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range (0, len(message)):
        if message[i]==" ":
            new_word=" "
            print(new_word,end="")
       
        else:
            new_word= alphabet_list[((alphabet_list.index(message[i])+shift)%26)]
            print(new_word,end="")
    
letters=str(input("Add a word:"))
shifts=int(input("How many shifts to the right?:"))

caesar_cipher(letters.upper(), shifts)
    def shift_by_letter(letter, shift):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if letter==" ":
            new_letter=" "
            return(new_letter)
    else:
        new_letter=alphabet_list[(alphabet_list.index(letter)+alphabet_list.index(shift))%26]
        print(new_letter)
        return(new_letter)
    
letters=str(input("Add a letter:"))
shifts=str(input("How many shifts to the right? (letter):"))

shift_by_letter(letters.upper(), shifts.upper())
    def vigenere_cipher(message, key):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range (0, len(message)):
        if message[i]==" ":
            new_word=" "
            print(new_word,end="") 
           
        else:
            new_word= alphabet_list[((alphabet_list.index(message[i])+(alphabet_list.index(key[i%len(key)])))%26)]
            print(new_word,end="")
          
    
letters=str(input("Add a word:"))
shifts=str(input("How many shifts to the right?(key word):"))

vigenere_cipher(letters.upper(), shifts.upper())def scytale_cipher(message, shift):
    if len(message) % shift== 0:
        message= message 
    else:
        while len(message) % shift != 0:
            message = message+ "_" 
    for i in range(0,len(message)):
        word= message[(i // shift) +(len(message) // shift) * (i % shift)]
        print(word,end="")
        
letters=str(input("Add a word:"))
shifts=int(input("How many shifts to the right?:"))

scytale_cipher(letters.upper(), shifts)def scytale_decipher(message, shift):
    for i in range (0, len(message)):
        decipher_word= message[(i // int(len(message)/shift)) +(len(message) // int(len(message)/shift)) * (i % int(len(message)/shift))]
        print(decipher_word, end="")

letters=str(input("Add a word:"))
shifts=int(input("How many shifts to the right?:"))

scytale_decipher(letters.upper(), shifts)

# In[ ]:




