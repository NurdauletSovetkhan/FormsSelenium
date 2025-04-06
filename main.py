import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

form_url = "" #URL
driver.get(form_url)
time.sleep(2)

def fill_checkboxes(block, index):
    time.sleep(.2)
    options = block.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
    total = len(options)
    print(f"Вопрос {index+1}: найдено чекбоксов — {total}")

    if total == 0:
        print(f"Вопрос {index+1}: чекбоксы не найдены")
        return

    count = min(3, total)
    selected_indexes = []

    while len(selected_indexes) < count:
        rand_index = random.randint(0, total - 1)
        if rand_index not in selected_indexes:
            selected_indexes.append(rand_index)

    for i in selected_indexes:
        opt = options[i]
        driver.execute_script("arguments[0].scrollIntoView(true);", opt)
        time.sleep(0.3)
        opt.click()
        print(f"Вариант {i+1} выбран")

def answer_current_page():
    question_blocks = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')
    print(f"Вопросов найдено: {len(question_blocks)}")

    for index, block in enumerate(question_blocks):
        time.sleep(0.3)
        radio_options = block.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
        print(f"Вопрос {index+1}: найдено radio — {len(radio_options)}")
        checkbox_options = block.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')

        if radio_options:
            choice = random.choice(radio_options)
            driver.execute_script("arguments[0].scrollIntoView(true);", choice)
            time.sleep(0.3)
            choice.click()
            print(f"Вопрос {index+1}: выбран radio")

        elif checkbox_options:
            fill_checkboxes(block, index)

        else:
            print(f"Вопрос {index+1}: неизвестный тип")

def go_to_next_page():
    try:
        next_button = driver.find_element(By.XPATH, '//span[text()="Далее" or text()="Submit"]/ancestor::div[@role="button"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(0.5)
        next_button.click()
        print("Перешли на следующий раздел")
    except Exception as e:
        print(f"Ошибка при переходе на следующий раздел: {e}")

def submit_form():
    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
        for btn in buttons[::-1]:
            if "Отправить" in btn.text or "Submit" in btn.text:
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                btn.click()
                print("Форма отправлена!")
                return
        print("Кнопка 'Отправить' не найдена!")
    except Exception as e:
        print(f"Ошибка при отправке формы: {e}")

while True:
    try:
        answer_current_page()

        buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
        submit_button_found = False
        for btn in buttons[::-1]:
            if "Отправить" in btn.text or "Submit" in btn.text:
                submit_button_found = True
                break

        if submit_button_found:
            print("Кнопка 'Отправить' найдена, завершаем!")
            submit_form()
            time.sleep(2)
            driver.get(form_url)
            time.sleep(2)
        else:
            print("Кнопка 'Отправить' не найдена, переходим к следующему разделу.")
            go_to_next_page()

        time.sleep(2)

    except Exception as e:
        print(f"Ошибка в основном цикле: {e}")
        break

time.sleep(5)
driver.quit()