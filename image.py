import numpy as np
from PIL import Image

img = Image.open('image.jpg')
arr = np.asarray(img, dtype='uint8')

a = 64 //номер строки, которую нужно вывести
kolnum = [0] * 14 //массив счетчиков для каждого символа

for i in range(0, 128, 1):
    print((arr[a][i] // 20) * 20, end=' ') //вывод символов
    kolnum[arr[a][i] // 20] += 1 //подсчет количества
print()
for i in range(0, 14, 1):
    print(kolnum[i], end =' ') //вывод счетчиков
