print("二重否定表現CLEANER")

temp = input("入力してください: ")


x = temp.count("なく")

y = temp.count("ない")


if (x + y) % 2 == 1:
    surch = temp.index("なく")
    output_text = temp[:surch] + temp[temp.rfind("ない")+2:]
    print(output_text + "ない")
else:
    surch = temp.index("なく")

    output_text = temp[:surch] + temp[temp.rfind("ない")+2:]
    print(output_text + "ある")

