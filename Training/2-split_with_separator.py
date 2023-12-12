import re

x = "class.function()"
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
