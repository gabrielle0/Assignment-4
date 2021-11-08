def enter_Money_Apple ():
    amount_Money = int (input("How much money do you have? "))
    apple_Price = int (input("How much is an apple? "))
    return amount_Money, apple_Price

def max_Apples (money, apples):
    max_Apples_ = money // apples
    return max_Apples_

def remaining_Money (money, apples):
    remaining_Money_ = money % apples
    return remaining_Money_


#Steps:
#1.) Enter amount of money and price of an apple. Save to variables. 
money, apples  = enter_Money_Apple ()
#2.) Calculate maximum number of apples and remaining money. 
maximum_Apples = max_Apples (money, apples)
change = remaining_Money (money, apples)
#3.) Display the maximum number of apples that you can buy and the remaining money that you will have.
