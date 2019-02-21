# Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
# a) використовуючи функцію map
# b) використовуючи функцію map та lambda

def miles_to_kms(num_miles):
    return round(num_miles * 1.6, 2)
mile_list = [25, 67, 15, 10, 100]
kilometer_dist = list(map(miles_to_kms, mile_list))
print(kilometer_dist)

mile_list = [25, 67, 15, 10, 100]
kilometer_dist = list(map(lambda x: round(x * 1.6, 2), mile_list))
print(kilometer_dist)
