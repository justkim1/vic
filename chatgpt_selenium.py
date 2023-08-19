from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def start_chat(user_input):
    chrome_driver_path = "path_to_chromedriver.exe"  # Update with actual path
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.chatgpt.com/")  # Open ChatGPT website

    chat_input = driver.find_element_by_id("chat-input")  # Locate chat input box
    chat_input.send_keys(user_input)
    chat_input.send_keys(Keys.RETURN)
    
    time.sleep(2)  # Wait for response to load
    response_element = driver.find_element_by_class_name("message-text")
    response = response_element.text

    driver.quit()  # Close the browser
    return response
# 코드는 위의 'chatgpt_selenium.py' 코드와 동일합니다.
