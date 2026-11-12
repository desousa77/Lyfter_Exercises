def sort_string(string):
   words = string.split("-")
   sorted_words = sorted(words)
   result = "-".join(sorted_words)
   return result

print(sort_string("python-variable-funcion-computadora-monitor"))