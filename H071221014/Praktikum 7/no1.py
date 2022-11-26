import re
s = input("")

pola = r"(\A([A-z]|[0|2|4|6|8]){40})(\s|1|3|5|7|9){5}"
hasil = re.fullmatch(pola, s)
if hasil:
    print("true")
else:
    print("false")
