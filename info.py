user_info = {"first_name" : "Mike", "last_name" : "Yampolsky"}
print(user_info["first_name"])

dictionary = {"city": "Москва", "temperature": "20"}
print(dictionary["city"])
dictionary["temperature"] = int(dictionary["temperature"]) - 5
dictionary["temperature"] = str(dictionary["temperature"])
print(dictionary)
print(dictionary.get("country"))
print(dictionary.get("country", "Россия"))
dictionary["date"] = "27.05.2019"
print(dictionary)
print(len(dictionary))
len(dictionary)