def add_expense(expense):
    cur_amount = float(input("please input the amount: "))
    cur_category = input("please input the category: ")
    cur_note = input("please input the note(optional): ") 

    record = {}
    #
    record["amount"] = cur_amount
    record["category"] = cur_category
    record["note"] = cur_note
       
    amount.append(cur_amount)
    category.append(cur_category)
    note.append(cur_note)
    
    return 1

def show_records(expense):
    print("$$ my expense records $$")
    for record in expense:
        cur_amount = record ["amount"]
        cur_category = record["category"]
        cur_note = record ["note"]
            
        print(f"amount: {reord["amount"]}")
    return


if __name__ == "__main__":
    #test_expences[
    #   {"amount": 10, "category": "food", "note": "lunch"},
    #   {"amount": 20, "category": "gas", "note": ""},
    #   {"amount": 15, "category": "food", "note": "snack"},
    #   {"amount": 50, "category": "shopping", "note": "shirt"},
    #]

    expence = []
    add_expense = []