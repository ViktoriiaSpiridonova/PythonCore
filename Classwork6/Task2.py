# Вивести список кольору, який найчастіше зустрічається в даному списку  [red, green, black, red, brown, red, blue, red, red, yellow ] 
# використовуючи функцію filter.

color_list = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
sort_red = list(filter(lambda x: x == "red", color_list))
print(sort_red)
