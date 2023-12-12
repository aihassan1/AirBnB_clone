dic = {"x": 5}
# Notice the difference here
# First code
"""
val = dic["v"]

Output:
Traceback (most recent call last):
  File "0-dict.py", line 2, in <module>
    val = dic["g"]
KeyError: 'g'
"""
# Second code
val = dic.get("v")
print(val)
