import numpy as np
import matplotlib.pyplot as plt
# Параметры нормального распределения

# mean = 0 # Среднее значение
#
# std_dev = 1 # Стандартное отклонение
#
# num_samples = 1000 # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
#
# data = np.random.normal(mean, std_dev, num_samples)

# plt.hist(data, bins=100)
#
# plt.xlabel("Значение")
# plt.ylabel("Количество")
# plt.title("Нормальное распределение")
# plt.show()
# ra1 = np.random.rand(5) # массив из 5 случайных чисел
# ra2 = np.random.rand(5) # массив из 5 случайных чисел
#
#
# plt.scatter(ra1, ra2)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Диаграмма рассеяния")
# plt.show()

# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Firefox()
url = "https://www.divan.ru/kursk/category/divany-i-kresla"
driver.get(url)
parsed_data = []
Prices = []

for element in driver.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl.find ('_Ud0k') == 0:
        link = ''
        price = ''
        name = ''
        link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        for element1 in element.find_elements(By.TAG_NAME, "div"):
            cl2 = element1.get_attribute("class")
            if cl2 == 'pY3d2':
                price = element1.find_element(By.TAG_NAME, "span").text
                # price = element1.text.split('\n', 1)
            if cl2 == 'lsooF':
                # name = element1.text
                name = element1.find_element(By.TAG_NAME, "span").text
        parsed_data.append([name, price, link])
        Prices.append(int(price.replace('руб.','').replace(' ','')))

driver.quit()

df = pd.DataFrame(Prices)
print("Средняя цена: ",df.mean())

print(parsed_data)
# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

plt.hist(df, bins=10)

plt.xlabel("Количество")
plt.ylabel("Цена")
plt.title("Гистограмма цен")

plt.show()