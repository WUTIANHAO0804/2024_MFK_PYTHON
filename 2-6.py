import re
input_str = input()
cleaned_str = re.sub(r'[^+\d]', '', input_str)
print(cleaned_str)