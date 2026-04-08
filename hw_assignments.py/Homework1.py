f = open("Expense_tracker.py")

count = 0
for line in f:
    count = count + 1

print ("Total lines:", count)

f.close()

#able to see how many lines in a file without opening file

f = open