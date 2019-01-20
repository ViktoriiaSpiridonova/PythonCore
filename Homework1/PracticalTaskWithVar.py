# Змінній   var_int надайте значення 10,
                # var_float - значення 8.4, 
                 # var_str - "No".
# 1.	Змініть значення, збережене у змінній var_int, збільшивши його в 3.5 рази, результат зв'яжіть зі змінною big_int.
# 2.	Змініть значення, збережене у змінній var_float, зменшивши його на одиницю, результат зв'яжіть з тією ж змінною.
# 3.	Розділіть var_int на var_float, а потім big_int на var_float. Результат даних виразів не прив'язуйте до жодних змінних.
# 4.	Змініть значення змінної var_str на "NoNoYesYesYes". При формуванні нового значення використовуйте операції конкатенації (+) 
# і повторення рядка (*).

var_int = 10
var_float = 8.4
var_str = "No"
big_int = var_int*3.5
print(big_int)
print(var_float-1)
print(var_int/var_float)
print(big_int/var_float)
var_str = (var_str*2 + ("Yes")*3)
print(var_str)
