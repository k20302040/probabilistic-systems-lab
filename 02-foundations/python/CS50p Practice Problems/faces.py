emoji_dict = {
    ":)" : "🙂",
    ":(" : "🙁"
}
user_input = input("")
user_input_list = user_input.split(" ")

for item in user_input_list:
    if item not in emoji_dict:
        pass
    if item in emoji_dict:
        item_index = user_input_list.index(item)
        user_input_list[item_index] = emoji_dict[item]

output = ' '.join(user_input_list)
print(output, end = "")
