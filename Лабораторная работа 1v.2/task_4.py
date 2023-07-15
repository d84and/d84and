users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

unique_users = set(users)
dict_1 = {
          "Общее количество": 0,
         "Уникальные посещения": 0
           }

dict_1["Общее количество"] = len(users)
dict_1["Уникальные посещения"] = len(set(users))
print(dict_1)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
