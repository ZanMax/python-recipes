# List recepies
Examples of work with list

#### Item with max length in list
```python

lst = ["one", "test", "pyton"]

max_length = max(lst, key=len, default="")

print(max_length)
```

#### Merge two sorted lists
```python
def merge2sortedlist(list1, list2):
    res = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    res = res + list1[i:] + list2[j:]
    return res
```