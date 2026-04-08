import time
from show_summary import * 
import ui
import tracker


if __name__ == "__main__":
    expense = []

    while True:

        time.sleep(2)
        ui.show_menu()
        choice = input("input choice 1-4: ").strip()
        if choice == '4':
            print("bye!")
            break


        if choice == '1':
            status = tracker.add_expense(expense)
            if status == 1:
                print("one record added!")
                # show_expenses
                tracker.show_records(expense)
            continue

        if choice == '2':
            # show expenses
            # print("current state is: ",  amounts, categories, notes)
            length = len(expense)
            print(f"{length} records so far")

            if length == 0:
                continue

            tracker.show_records(expense)
            continue

        if choice == '3':
            # show summary
            show_summary(expense)
            continue
            

        # if the choice is invalid
        print("please select from 1-4")