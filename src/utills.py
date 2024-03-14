import json
import datetime
import pytest


def add_initial_data():
    ####Открытие исходного файла
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def delete_none():
    ####Удаление пустого словаря
    right_operations = []
    for i in range(len(add_initial_data())):
        if "id" in add_initial_data()[i]:
            right_operations.append(add_initial_data()[i])
    return right_operations

def executed_operations_only():
    ####Оставил только успешные операции
    executed_operations = []
    for i in delete_none():
        if i["state"] == "EXECUTED":
            executed_operations.append(i)
    return executed_operations


def crypto(card):
    ####шифровка номеров карт и счетов
    card_vine = ""
    if card.startswith("Visa"):
        card_num = card.split()[-1]
        card_name = card.split()[0] + " " + card.split()[1]
        private_number = card_num[:6] + (len(card_num[6:-4]) * '*') + card_num[-4:]
        chunks, chunk_size = len(private_number), len(private_number)//4
        secret_number = " ".join([private_number[i:i+chunk_size] for i in range(0, chunks, chunk_size)])
        card_vine = card_name + " " + secret_number
        return card_vine
    elif card.startswith("Maestro") or card.startswith("MasterCard") or card.startswith("МИР"):
        card_num = card.split()[-1]
        card_name = card.split()[0]
        private_number = card_num[:6] + (len(card_num[6:-4]) * '*') + card_num[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4
        secret_number = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
        card_vine = card_name + " " + secret_number
        return card_vine
    elif card.startswith("Счет"):
        card_num = card.split()[1]
        card_name = card.split()[0]
        private_number =len(card_num[-3:-1]) * '*' + card_num[16:]
        card_vine = card_name + " " + private_number
        return card_vine


def secret_card():
    ####Создание списка с шифрованными картами и счетами
    anonymus_card = []
    for i in executed_operations_only():
        if  "from" in i.keys() and "to" in i.keys():
            i["from"] = crypto(i["from"])
            i["to"] = crypto(i["to"])
            anonymus_card.append(i)

        if  "from"  not in i.keys() and "to" in i.keys():

            i["to"] = crypto(i["to"])
            anonymus_card.append(i)
    return anonymus_card


def sort_operations():
    ### Сортировка по дате
   operations = secret_card()
   sorted_operations = sorted(operations, key=lambda x: x["date"],reverse=True)
   return sorted_operations



def date_format():
    ###Перевод даты в удобный вид
    operations_with_right_date_format = []
    for i in sort_operations():
        i['date'] = datetime.datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
        i["date"] = i["date"].date()
        i["date"] = i["date"].strftime("%d.%m.%Y")
        operations_with_right_date_format.append(i)
    return operations_with_right_date_format

def slice_operations():
    #Срез
    return date_format()[0:5]










