import os
import re
from data.mypath import base_path

full_path = os.path.join(base_path, "names.txt")
with open(full_path, "r", encoding="utf-8") as file:
    content = file.read()


def func_names(names):

    list_1 = []
    pattern = r"\s+"  # шаблон для разделения по пробелам
    words = re.split(pattern, names)
    for item in words:
        if "." in item:
            word = item.replace(".", "")
            list_1.append(word)

        elif "," in item:
            word = item.replace(",", "")
            list_1.append(word)

        elif "!" in item:
            word = item.replace("!", "")
            list_1.append(word)

        elif item.isdigit():
            continue

        elif item:
            list_1.append(item)

        else:
            del item
    for i in list_1:
        if i == "":
            list_1.remove(i)
    return list_1


result = func_names(content)
print(result)
