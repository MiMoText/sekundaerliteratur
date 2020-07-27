my_dict = {"key1" : "value1",  "key2" : "value2"}
my_list = ["key2"]
my_dict_list = [{"key1" : "value1"},  {"key2" : "value2"}]

if "key1" in my_dict:
    print("ok")

if my_list[0] in my_dict:
    print("ok2")

for i in range(len(my_list)):
    if my_list[i] in my_dict:
        print("ok3")

for i in range(len(my_list)):
    if my_list[i] in my_dict:
        my_dict["key1"] = i
        print(my_dict)

file = open("dict_test.csv", "w")
for i in range(len(my_dict_list)):
    print(my_dict_list[i])
    my_id = my_dict_list[i]
    file.write(str(my_id))

with open("../data_in/rieger.txt", encoding="utf-8") as file:
    text = file.read()
print(text)
