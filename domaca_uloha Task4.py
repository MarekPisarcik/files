


with open("subor.txt", "w") as f:
    data = f.write(
        """
        Toto je novy textovy subor vytvoreny pomocou kodu v pythone. \n
        Subor bol vytvoreny pomocou kodu. \n
        Data: 1211151464618 \n
        Data2: ldvmvkmdflvmkdfmvkfmvldfmflvmdfvmlfdvfdmvriirgrgie \n
        """
    )
maximalna_dlzka = 0
with open("subor.txt", "r") as f:
    for line in f:
        if len(line) > maximalna_dlzka:
            maximalna_dlzka = len(line)

print(maximalna_dlzka)