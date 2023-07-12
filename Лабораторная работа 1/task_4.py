users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = {'user1', 'user2', 'user3', 'user1', 'user4', 'user2'}

dict = {'Общее количество':'Уникальные посещения'}
dict['Общее количество'] = (len(users))
dict['Уникальные посещения'] = (len(unique_users))
print(dict)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений)unique_users = {'user1', 'user2', 'user3', 'user1', 'user4', 'user2'}


# Начальные значения могут быть равн  0 если будут отсутствовать все пользователи