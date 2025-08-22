import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://translate.yandex.ru/translate")
url = driver.current_url
print("URL страницы: ", url)
assert url =="https://translate.yandex.ru/translate" , "Ошибка URL"

current_title = driver.title
print("Текущий заголовок: ", current_title)
assert current_title =="Переводчик сайтов онлайн на русский и другие языки – Яндекс Переводчик" , "Ошибка title"

print(driver.page_source)
time.sleep(5)