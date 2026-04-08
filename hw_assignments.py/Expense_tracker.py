def add_expense(amount, category, note):
    cur_amount = float(input("please input the amount: "))
    cur_category = input("please input the category: ")
    cur_note = input("please input the note(optional): ")    
       
    amount.append(cur_amount)
    category.append(cur_category)
    note.append(cur_note)
    
    return 1

def show_records(amount, category, note):
    print("$$ my expense records $$")
    for i in range(len(amount)):
            
        print(f"amount: {amount[i]}, type: {category[i]}, note: {note[i]}", amount[i], category[i], note[i])
    return


def show_menu():
    print("/nMenu: ") #/n creates an empy space from the default python code
    print("1. add expense")
    print("2. print expenses")
    print("3. show the summary")
    print("4. exit")

#def_Summary (this is assingment 2)
def show_summary(amount, category):
     if len(amount) == 0:
          print("No expenses yet.")
          return
     
     total_spending = 0
     for a in amount:
        total_spending = total_spending + a
        
     print(f"Total spending: ${total_spending: .2f}")


     unique_cats = []
     for cat in category:
        if cat not in unique_cats:
            unique_cats.append(cat)
    
     print("Total by cateogry:")
     for ucat in unique_cats:
        cat_total = 0
        
        for i in range(len(category)):
                if category[i] == ucat:
                        cat_total = cat_total + amount[i]
        print(f"-{ucat}: ${cat_total: .2f}")




amount = []
category = []
note = []

while True:

    show_menu()

    choice = input("input choice from 1-4: ").strip() #strip removes extra spaces the users might add
    if choice == '4':
        print("bye!")
        break

    if choice == '1': #add expense
        status = add_expense(amount, category, note)
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
        
        show_records(amount, category, note)
        continue

    if choice == '3': #show the summary
        print("show summary")
        
        show_summary(amount, category)
        continue

#if choice is invalid
print("please select from 1-4") 



#1) For unique_cats I used a for loop, if cat not in, and a list to store values in. 
#This ensured that the new categories from the expenses were added to the list, 
#and already present ones were not added twice.

#2) For the cat_total I set up a loop with range(len(category)) to go through the expenses 
# by their index. Then I used the same index [i] for category and amount, so the code was able 
# to add the expenses together for the same categories. Final I format my answers 
# using .2f to format to 2 decimals. 