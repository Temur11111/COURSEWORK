from utills import slice_operations


for i in slice_operations():
    if "from" in i.keys() and "to" in i.keys():
        print(f"""{i["date"]} {i["description"]}
{i["from"]} -> {i["to"]} 
{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}
**************************************************************************""")

    elif "from" not in i.keys() and "to" in i.keys():
        print(f"""{i["date"]} {i["description"]}
{i["to"]} 
{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}
**************************************************************************""")