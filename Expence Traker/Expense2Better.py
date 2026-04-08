import time
from show_summary import *
import Ui
import tracker




amount = []
category = []
note = []


if __name__ == "__main__":
   expense = []
   
   
   while True:
        time.sleep(2)
        Ui.show_menu()
        choice = input("input choice from 1-4: ").strip() #strip removes extra spaces the users might add
        if choice == '4':
        print("bye!")
        break
   
        if choice == '1': #add expense
        status = tracker.add_expense(expense)
        if status == 1:
                print("one record added!")
                #show_expenses
            
        continue

        if choice == '2': #print expense
        #print("current list is: ", amount, category, note)
        length = len(amount)
        print(f"{length} records so far")

        if length == 0:
             continue
        
        tracker.show_records(expense)
        continue

    if choice == '3': #show the summary
        print("show summary")
        
        show_summary(expense)
        continue

#if choice is invalid
print("please select from 1-4") 


expense = [
   {"amount": 10, "category": "food", "note": Lunch"}, 
    {"amount": 20, "category": "gas", "note: ""}
]








#1) For unique_cats I used a for loop, if cat not in, and a list to store values in. 
#This ensured that the new categories from the expenses were added to the list, 
#and already present ones were not added twice.

#2) For the cat_total I set up a loop with range(len(category)) to go through the expenses 
# by their index. Then I used the same index [i] for category and amount, so the code was able 
# to add the expenses together for the same categories. Final I format my answers 
# using .2f to format to 2 decimals. 