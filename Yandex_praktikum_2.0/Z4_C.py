with open("input_Z4_C.txt", "r") as file:
    text = file.read().split()
word_dict = dict()

for word in text:
    word_dict[word] = word_dict.get(word,0) + 1

sort = (sorted(word_dict.items(),key=lambda x: (-x[1],x[0])))
for i in sort:
    print(i[0])
