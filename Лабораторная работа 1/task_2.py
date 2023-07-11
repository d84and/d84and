# TODO Найдите количество книг, которое можно разместить на дискете
odin_kb = 1024  # Размер одного килобита
disk_1 = 1.44   # Размер диска
kolicestvo_bit = (odin_kb ** 2)*disk_1  # Расчет количества бит
stranici_knigi = 100  # Количество страниц в книге по заданию
chislo_strok = 50   #  Число строк на странице
kolichestvo_simvolov = 25   #  Количество символов
odin_simvol = 4  # Количество байт для хранения одного символа
bayt_v_stroke = kolichestvo_simvolov * odin_simvol
bayt_na_stronice = bayt_v_stroke * chislo_strok
bayt_v_knige = bayt_na_stronice * stranici_knigi
kolichestvo_knig = kolicestvo_bit / bayt_v_knige
kolichestvo_knig = round(kolichestvo_knig)
print("Количество книг, помещающихся на дискету:", kolichestvo_knig)
