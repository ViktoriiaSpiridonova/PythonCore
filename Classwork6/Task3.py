# Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, 
# всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

string_list = ["1","2","3","4","5","7"]
new_list = []
for item in string_list:
    new_list.append(int(item))
print(new_list)

string_list = ["1","2","3","4","5","7"]
new_list = list(map(int, string_list))
print(new_list)
