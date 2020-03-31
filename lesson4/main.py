s = "Hello my dear Friend.Hi my name is Yerassyl.Are you"
key="my"
key_count=0
words = s.split(" ")
for word in words:
    if word == key:
        key_count = key_count + 1
print(key_count)