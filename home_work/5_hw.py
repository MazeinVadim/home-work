from selenium import webdriver
from selenium.webdriver.common.by import By


def open_saucedemo():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print('Сайт успешно открыт')
#   Находим текстовое поле с именем пользователя
    username_filed = driver.find_element(By.ID, "user-name")
#   Нахлдим текстовое поле с паролем
    password_filed = driver.find_element(By.ID, "password")
#   Находим кнопку отправки
    login_button = driver.find_element(By.ID, "login-button")

#   Если все элементы найдены:
    if username_filed and password_filed and login_button:
        print("Элементы найдены")
    else:
        print("Один или несколько элементов не найдены!")

#   Закрываем браузер
    driver.quit()

if __name__ == '__main__':
    driver = open_saucedemo()



