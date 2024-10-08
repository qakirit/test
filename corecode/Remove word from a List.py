list = ["test", "two", "test", "one"]

numberoftime = 2
count = 0
for i in range(len(list) - 1):

    if list[i] == list:
        numberoftime = numberoftime + 1
        if count == numberoftime:
            del list[i]
print(list)