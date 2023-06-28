#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Individual Programming Assignment 1

20 points

This assignment will develop your basic familiarity with Python.
'''



#Savings.
   
def savings (gross_pay, tax_rate, expenses):
    
    if tax_rate<=1 and tax_rate>=0:
        final_pay= int((gross_pay)*(1-tax_rate))-(expenses)
        return(f"your final pay is: {final_pay} Philippine centavos")
    else: 
        return("not valid tax value")
    
gross = int(input("What is your total pay(in centavos):"))
tax = float(input("What is the tax rate (between 0 and 1):"))
expense = int(input("What are your expenses(in centavos):"))

savings (gross,tax,expense)



#Material Waste.



    
def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste= total_material- (num_jobs*job_consumption)
    Waste=str(waste)
    return ("The total remaining material is: " + Waste+ material_units)

totalmaterial= int(input("What is the total material available?:"))
numjobs= int(input("What are the number of jobs?:"))
jobconsumption=int(input("What is the material consumption per job?:"))
materialunits= str(input("What are the units of materials (e.g. kg, L, ton,etc.)"))

material_waste(totalmaterial, materialunits, numjobs, jobconsumption)



#'''Interest.

    
def interest(principal, rate, periods):
    if rate >= 0 and rate<=1: 
        Interest= principal*(rate)*periods
        final= int(principal + Interest)
        return (f"your final investment is: {final}")
    else:
        return("invalid interest rate")
principalI= int(input("Principal investment amount:"))
rateI= float(input("Interest rate (in decimal form of percentage (3%=0.03):"))
periodsI= int(input("Number of periods invested:"))

interest(principalI, rateI, periodsI)

#'''Body Mass Index.
   
    
def body_mass_index(weight, height):
    BMI= (weight*0.4536)/((((height[0]*12)+(height[1]))*0.0254)**2)
    return(f"your BMI is: {BMI}")
weightI= float(input("Enter your weight in lbs:"))
heightI= [int(input("How tall are you in feet (disregard excess inches not in a whole foot):")), int(input("how many inches did you exceed of a whole number of a foot (inches component)?:"))]

body_mass_index(weightI, heightI)
    

