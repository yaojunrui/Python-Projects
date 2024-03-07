friends = ["Tom", "Jim" , "Ryan", "Mike"]
# friends.append("John")
# friends.insert(1, "Jim")
# friends.remove("Tom")
# friends.pop() #pop out the last value
# friends.insert(2, "Mike")
friends.sort()

print(friends)

#the position of the "Mike"
print(friends.index("Mike"))

#How many times does the name "Jim" appear in the list
print(friends.count("Jim"))

lucky_num = [23, 63, 53, 3, 5, 13]
lucky_num.sort()
print(lucky_num)
print(lucky_num[-1], lucky_num[0])

#string 和 list 都有count（）
