# TODO решите задачу
import json


def task() -> float:
    imiafaila = "input.json"
    with open(imiafaila) as f:
        fail = json.load(f)

    summa_znacheniy = sum([item["score"] + item["weight"] for item in fail])
    return round(summa_znacheniy, 3)


print(task())



