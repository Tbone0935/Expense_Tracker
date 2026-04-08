def show_summary(expenses):

    if len(expenses) == 0:
        print("No expenses yet.")
        return
    
    total = 0
    for item in expenses:
        total = total + item["amount"]

    print(f"Total spending: ${total:.2f}")

    unique_categories = []

    for item in expenses:
        c = item["category"]
        if c not in unique_categories:
            unique_categories.append(c)

    print("================")
    print("Total by category:")

    for c in unique_categories:
        category_total = 0
        for item in expenses:
            if item["category"] == c:
                category_total = category_total + item["amount"]

        print(f"{c}: ${category_total:.2f}")



if __name__ == "__main__":
    test_expenses = [
        {"amount": 10, "category": "food", "note": "lunch"},
        {"amount": 20, "category": "gas", "note": ""},
        {"amount": 15, "category": "food", "note": "snack"},
        {"amount": 50, "category": "shopping", "note": "shirt"}
    ]

    show_summary(test_expenses)
