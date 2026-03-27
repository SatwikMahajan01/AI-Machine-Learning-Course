expenses=[20,100,45,300]
total_expense=0
# for expense in expenses:
#     total_expense=total_expense+expense
# print(f"you spent {total_expense} on food")
print("Using for loop")
for i in range(len(expenses)):
    expense=expenses[i]
    print(f"On day {i+1} you spent {expense}")
    total_expense=total_expense+expense
print(f"you spent {total_expense} on food")

print("--------------------------------")

print("Using enumerate function")
total_expense=0
for i ,expense in enumerate(expenses):
    # expense=expenses[i]
    print(f"On day {i+1} you spent {expense}")
    total_expense=total_expense+expense
print(f"you spent {total_expense} on food")