a = {"five": 5, "four": 4, "three": 3, "two": 2, "one": 1}
s = input()
if s in ["one", "two", "three", "four", "five"]:
    print(a[s])
else:
    print("I don't know this number!")