print("Exam Grade Finder")
print("-----------------")
paper1 = int(input("Enter paper 1 mark: "))
paper2 = int(input("Enter paper 2 mark: "))
total = paper1 + paper2
print("Total mark", total)
if total >= 40:
    print ("Pass")
else:
    print("Fail")
