lst = [1, 2, 3]
counter = 1
if len(lst) != 1:
    for i in lst:
        if lst.index(i) == 0:
            last = i
            continue
        if i == last + 1:
            last = i
            counter += 1
        else:
            print("No")
            break
        if counter == len(lst):
            print("Yes")
else:
    print("No")