# TODO Напишите функцию find_common_participants
def find_common_participants(stroka_1, stroka_2, razdelitel="!"):
    common = [x for x in stroka_1 if x in stroka_2]
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
new_common = participants_first_group.split("|")
new_common_1 = participants_second_group.split("|")
print(new_common)
print(new_common_1)
common_1 = [j for j in new_common if j in new_common_1]
result = find_common_participants(participants_first_group, participants_second_group)
print(result)

new_common = participants_first_group.split("|")
new_common_1 = participants_second_group.split("|")
#print(new_common)
#print(new_common_1)
common_1 = [j for j in new_common if j in new_common_1]
print(common_1)
# TODO Провеьте работу функции с разделителем отличным от запятой
