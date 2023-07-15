money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

i = money_capital
j = spend
months = 0
while  i > 0 and j < 8500:
    i = i + salary - spend
    j = j * (1 + increase )
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
