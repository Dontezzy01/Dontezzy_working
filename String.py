list = ["car", "cat", "fear", "center"]

longest = ""
for lst in list:
    if longest > len(lst):
        longest = lst
        print("The longest string is ",lst )