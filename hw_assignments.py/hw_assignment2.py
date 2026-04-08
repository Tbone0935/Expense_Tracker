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


#1) For unique_cats I used a for loop, if cat not in, and a list to store values in. 
#This ensured that the new categories from the expenses were added to the list, 
#and already present ones were not added twice.

#2) For the cat_total I set up a loop with range(len(category)) to go through the expenses 
# by their index. Then I used the same index [i] for category and amount, so the code was able 
# to add the expenses together for the same categories. Final I format my answers 
# using .2f to format to 2 decimals. 