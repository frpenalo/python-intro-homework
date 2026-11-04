list1 = ["Python", "Delphi", "Basic", "JavaScript"]
list2 = ["Python", "JavaScript", "Cobol", "DBase"]

set1 = set(list1)
set2 = set(list2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)