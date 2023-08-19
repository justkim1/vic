from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome WebDriver 초기화
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 브라우저를 띄우지 않고 실행
driver = webdriver.Chrome(options=chrome_options)

# ChatGPT 사이트 열기
driver.get("https://www.chatgpt.com/")

# 채팅 입력란 찾기
chat_input = driver.find_element_by_id("chat-input")

# 메시지 입력 및 전송
chat_input.send_keys("Hello, how can I help you?")
chat_input.send_keys(Keys.RETURN)

# 조금 기다려서 응답 확인
time.sleep(5)

# 응답 출력
response_element = driver.find_element_by_class_name("message-text")
response = response_element.text
print("ChatGPT:", response)

# 브라우저 닫기
driver.quit()
