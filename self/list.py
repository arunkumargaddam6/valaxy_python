luckynum = [4,5,6,7]
friends = ["ram", "karen", "arun", "radha"]

friends.extend(luckynum)
print(friends)
friends.insert(1, "kelly")
print(friends)
friends.remove("arun")
print(friends)
friends.clear()
print (friends)

# friends.count()
# luckynum.sort()
# luckynum.reverse()
# friends2 = friends.copy()