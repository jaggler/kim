#!/usr/bin/env python
# coding: utf-8

# **11. Scenario:**
# 
# You're creating a program to calculate discount prices for customers based on their age and purchase amount. The program takes three inputs:
# * Customer's age (integer)
# * Purchase amount (float)
# * Membership status (string, either "Gold" or "Regular")
# 
# The program should apply discounts based on the following rules:
# **Gold Members:**
# * If they are 65 years or older, they get an additional 10% discount on top of the base 15% discount for Gold members.
# * Otherwise (younger than 65), they only get the base 15% discount.
# 
# **Regular Members:**
# * If the purchase amount is over 100, they get a 10% discount.
# * If the purchase amount is less than or equal to 100, they don't get any discount.
# 
# The program should output the final discounted price after applying the appropriate discounts (if any).
# 
# **Challenge:**
# 
# Can you write a single Python code block using if statements to calculate and print the discounted price based on the given scenario?
# 

# In[ ]:


customer_age = int(input('Enter age: '))
purchase_amount = float(input('Enter purchase amount: '))
membership_status = input('Enter membership status either G for "Gold" or R for "Regular": ' ).title()

# #Gold members discount
gold_discount = float(10/100)
gold_above_65_discount = gold_discount + float(15/100)

if membership_status == 'G' and customer_age >= 65:
    gold_purchase_disc =  gold_above_65_discount * purchase_amount
    price = purchase_amount - gold_purchase_amount
    print(f"purchase amount is Kshs {price} after of discount Kshs {gold_purchase_disc} ")

elif membership_status == 'G' and customer_age < 65:
        gold_purchase_disc =  gold_discount * purchase_amount
        price = purchase_amount - gold_purchase_disc
        print(f"purchase amount is Kshs {price} after of discount Kshs {gold_purchase_disc} ")

# regular members discout

regular_discount_over_100 = float(10/100)*purchase_amount

if purchase_amount >= 100 and membership_status == 'R' :
    regular_price = purchase_amount - regular_discount_over_100
    print(f"purchase amount is Kshs {regular_price} after of discount Kshs {regular_discount_over_100} ")

elif purchase_amount <= 100 and membership_status == 'R' :
    print(f"purchase amount is Kshs {purchase_amount} ")
    
    
    

