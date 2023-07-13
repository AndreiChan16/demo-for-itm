#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):
    following= False
    follower= False
    if from_member in social_graph and to_member in social_graph:
        for value1 in social_graph[from_member]["following"]:
            if to_member==value1: 
                following = True
        for value2 in social_graph[to_member]["following"]:
            if from_member==value2: 
                follower = True
        if following and follower:
            return "friends"
        elif following:
            return "follower"
        elif follower:
            return "followed by"
        else:
            return "no relationship"
social_graph = {
    "@bongolpoc": {
        "first_name": "Joselito",
        "last_name": "Olpoc",
        "following": []
    },
    "@joaquin": {
        "first_name": "Joaquin",
        "last_name": "Gonzales",
        "following": ["@chums", "@jobenilagan"]
    },
    "@chums": {
        "first_name": "Matthew",
        "last_name": "Uy",
        "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]
    },
    "@jobenilagan": {
        "first_name": "Joben",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]
    },
    "@joeilagan": {
        "first_name": "Joe",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@jobenilagan", "@chums"]
    },
    "@eeebeee": {
        "first_name": "Elizabeth",
        "last_name": "Ilagan",
        "following": ["@jobenilagan", "@joeilagan"]
    },
}

first_name = input("What is the username (@)? ")
second_name = input("What is the username (@)? ")

relationship_status(first_name, second_name, social_graph)

def tic_tac_toe(board):
    new_column=[]
    new_diagonal=[]
    new_diagonal2=[]
    indexer=len(board)-1
    for row in board:
        if len(set(row))==1 and row[0]!="":
            return row[0]
    for i in range (0, len(board)):   
        for column in board:
            new_column= new_column+[column[i]]
        if len(set(new_column))==1 and new_column[0] !="":
            return new_column[0]
        else:
            new_column=[]
    
    for i in range (0, 1):   
        for diagonal in board:
            new_diagonal= new_diagonal+[diagonal[i]]
            i += 1   
        if len(set(new_diagonal))==1 and new_diagonal[0] !="":
            return new_diagonal[0]
    
    for i in range (0, 1):   
        for diagonal in board:
            new_diagonal2= new_diagonal2+[diagonal[indexer]]
            indexer -= 1   
        if len(set(new_diagonal2))==1 and new_diagonal2[indexer] !="":
            return new_diagonal2[indexer]
    return "NO WINNER"

     
                
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','O','O'],
['O','X','','']
]

board8=[
['X','X','O','WOW'],
['O','X','WOW','O'],
['X','WOW','O','O'],
['WOW','X','','']
]



tic_tac_toe(board4)

leg1 = {
            ("ust","admu"):{
                 "travel_time_mins":10
             },
             ("admu","dlsu"):{
                 "travel_time_mins":35
             },
             ("dlsu","upd"):{
                 "travel_time_mins":55
             },
             ("upd", "ust"):{
                 "travel_time_mins":65
             }   
        }
leg2 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

leg3 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
def eta(first_stop, second_stop, legs):
    counter=0 
    new_counter=0
    total_time=[]
    for j in range (0, len(legs)):
        if (list(legs)[j][1]) == second_stop:
             label= j
    for i in range(0, len(legs)):
        if (list(legs)[i][0]) == first_stop:
            if list(legs).index(list(legs)[i])%len(legs) <= list(legs).index(list(legs)[label])%len(legs):
                total_time.append(legs[list(legs)[i]]["travel_time_mins"])
                counter=i
                while counter < label:
                    total_time.append(legs[list(legs)[counter+1]]["travel_time_mins"])
                    counter+=1
                print(sum(total_time))
            elif list(legs).index(list(legs)[i])%len(legs)> list(legs).index(list(legs)[label])%len(legs):
                total_time.append(legs[list(legs)[i]]["travel_time_mins"])
                counter=i
                while counter < len(legs)-1:
                    total_time.append(legs[list(legs)[counter+1]]["travel_time_mins"])
                    counter+=1
                while new_counter < list(legs).index(list(legs)[label])+1:
                    total_time.append(legs[list(legs)[new_counter]]["travel_time_mins"])
                    new_counter+=1
                return(sum(total_time))
                
first_stops=input("Where is the stop you are from?")
second_stops= input("Where is the stop you are going to?")
eta(first_stops, second_stops, leg3)



# In[ ]:





# In[ ]:




