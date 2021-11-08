def get_Amount_Apples_Oranges():
    apples_Func = int (input(f"How many apples do you want to buy? "))
    apples = apples_Func*20
    oranges_Func = int (input(f"How many oranges do you want to buy? "))
    oranges = oranges_Func*25
    return apples, oranges 






#Steps:
#1.) Ask for amount of apples and oranges you want to buy. Save to variables. Compute respective cost.
apples, oranges = get_Amount_Apples_Oranges ()
#2.) Add total apples and oranges. Save total to variable.
#3.) Display the output in the following format: The total amount is_ 