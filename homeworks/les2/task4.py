user_text = 'hello my friend Kudaibergenov'
arr = user_text.split()
for item in arr:
    if len(item)> 12:
        print(item[0:10])
    else:
        print(item)
