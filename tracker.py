def add_expense(expense):
    cur_amount = float(input("please input the amounts: "))
    cur_category = input("please input the category: ")
    cur_note = input("please input the note(optional): ")

    record = {}
    # {"amount": 10, "category": "food", "note": "lunch"},
    record["amount"] = cur_amount
    record["category"] = cur_category
    record["note"] = cur_note
    expense.append(record)
   
    return 1 
    
  
def show_records(expense):
    print ("$$ my expense records$$")
    for record in expense:
        cur_amount = record["amount"]
        cur_category = record["category"]
        cur_note = record["note"]

        print(f"amount: {cur_amount}, type: {cur_category}, note: {cur_note} ") 

if __name__ == "__main__":
    test_expenses = [
        {"amount": 10, "category": "food", "note": "lunch"},
        {"amount": 20, "category": "gas", "note": ""},
        {"amount": 15, "category": "food", "note": "snack"},
        {"amount": 50, "category": "shopping", "note": "shirt"}
    ]

    

    show_records(test_expenses)
    # expense = []
    # add_expense(expense)
    # print(expense)