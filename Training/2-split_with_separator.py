import re

x = "class.function(38f22813-2753-4d42-b37c-57a17f1e4f88), {'first_name': 'John', 'age' : 89}"
y = re.split(r"[.(,) ]", x)
print(f"split list:-->{y}")

arg_list = y[2:-1]
print(f"arg list:-->{arg_list}")
h = ""
for arg in arg_list:
    if arg == "":
        h = h + " "
    else:
        h = h + arg
print(f"#{h}#")
