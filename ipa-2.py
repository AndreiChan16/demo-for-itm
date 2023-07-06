#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def shift_letter(letter, shift):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if letter==" ":
            new_letter=" "
            return(new_letter)
    else:
        new_letter=alphabet_list[(alphabet_list.index(letter)+shift)%26]
        return(new_letter)
    
letters=str(input("Add a letter:"))
shifts=int(input("How many shifts to the right?:"))

shift_letter(letters.upper(), shifts)
    
    
def caesar_cipher(message, shift):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_message=""
    for i in range (0, len(message)):
        if message[i]==" ":
            new_word=" "
            new_message+=new_word
       
        else:
            new_word= alphabet_list[((alphabet_list.index(message[i])+shift)%26)]
            new_message+=new_word
    return new_message
    
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
        return(new_letter)
    
letters=str(input("Add a letter:"))
shifts=str(input("How many shifts to the right? (letter):"))

shift_by_letter(letters.upper(), shifts.upper())

def vigenere_cipher(message, key):
    alphabet_list=["A","B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_message2=""
    for i in range (0, len(message)):
        if message[i]==" ":
            new_word=" "
            new_message2+=new_word
           
           
        else:
            new_word= alphabet_list[((alphabet_list.index(message[i])+(alphabet_list.index(key[i%len(key)])))%26)]
            new_message2+=new_word
    return new_message2
             
letters=str(input("Add a word:"))
shifts=str(input("How many shifts to the right?(key word):"))

vigenere_cipher(letters.upper(), shifts.upper())

def scytale_cipher(message, shift):
    new_message3=""
    if len(message) % shift== 0:
        message= message 
    else:
        while len(message) % shift != 0:
            message = message+ "_" 
    for i in range(0,len(message)):
        word= message[(i // shift) +(len(message) // shift) * (i % shift)]
        new_message3+=word
    return new_message3
    
        
letters=str(input("Add a word:"))
shifts=int(input("How many shifts to the right?:"))

scytale_cipher(letters.upper(), shifts)

def scytale_decipher(message, shift):
    new_message4=""
    for i in range (0, len(message)):
        decipher_word= message[(i // int(len(message)/shift)) +(len(message) // int(len(message)/shift)) * (i % int(len(message)/shift))]
        new_message4 += decipher_word
    return new_message4
    

letters=str(input("Add a word:"))
shifts=int(input("How many shifts to the right?:"))

scytale_decipher(letters.upper(), shifts)


# In[ ]:




