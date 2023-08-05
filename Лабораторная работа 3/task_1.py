# TODO Напишите функцию для поиска индекса товара
def nayty_predmet_pozicii(predmety, predmet):
    for nomer_pozicii, tekyshiy_predmet in enumerate(predmety):
        if tekyshiy_predmet == predmet:
            return nomer_pozicii

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = nayty_predmet_pozicii(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
