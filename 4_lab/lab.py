import os
#os.environ["MY_VAR"] = "Я модифікував змінну"
try:
    print(os.environ.get("MY_VAR"))

    print(os.environ["VAR_2_TEMP"])
except:
    print("Немає таких Енвайрмент змінних")