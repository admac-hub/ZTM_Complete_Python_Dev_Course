def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)

print(highest_even([10,1,2,3,4,8]))
