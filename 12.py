#1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
##############################################################################################################################


def remove_duplicates_and_get_unique_values(input_dict):
    unique_values = list(set(input_dict.values()))
    unique_dict = {key: value for key, value in input_dict.items() if list(input_dict.values()).count(value) == 1}
    return unique_dict

# ფუნქციის გამოძახება
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result_dict = remove_duplicates_and_get_unique_values(sample_dict)

print("ორიგინალი ლექსიკონი:", sample_dict)
print("უნიკალური value-ების მქონე ლექსიკონი:", result_dict)

#########################################################################################################################
#2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.
#########################################################################################################################


def is_dict_empty(input_dict):
    return not bool(input_dict)

#Semowmeba

empty_dict = {}
non_empty_dict =  {'a': 1, 'b': 2, 'c': 3  }

result_empty = is_dict_empty(empty_dict)
result_non_empty = is_dict_empty(non_empty_dict)

print("ცარიელი ლექსიკონი:", result_empty)
print("არ არის ცარიელი ლექსიკონი:", result_non_empty)

#########################################################################################################################
# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}
#########################################################################################################################



def string_to_dict(s):
    result_dict = {}
    for char in s:
        result_dict[char] = result_dict.get(char, 0) + 1
    return result_dict


input_string = 'racoon'
result_dict = string_to_dict(input_string)

print(result_dict)