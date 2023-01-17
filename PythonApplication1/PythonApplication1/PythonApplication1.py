import Functional

# 1. вызваный метод удаляет из текста все слова, содержащие ""абв"".
text = 'абведите эту картинку и абвяжите всё'
print(Functional.deleteWord(text, 'абв'), "\n")


# RLE алгоритм: сжатие.
forEncoding = "AAABCCCCDDDDDDDDDDDDDDDDE"
print(Functional.encode(forEncoding), "\n")


# RLE алгоритм: восстановление.
forDecoding = Functional.encode(forEncoding)
print(Functional.decode(forDecoding), "\n")
