from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def start_chat(user_input):
    chrome_driver_path = r"C:\Users\7612112\Downloads\chromedriver_win32\chromedriver.exe"  # 크롬 드라이버 경로 업데이트
    chrome_service = Service()
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://www.chatgpt.com/")

    try:
        # 대기 시간 설정 (최대 10초 기다림)
        wait = WebDriverWait(driver, 20)
        
        # 채팅 입력란 대기 및 찾기
        chat_input = wait.until(EC.presence_of_element_located((By.ID, "chat-input")))
        
        # 채팅 입력
        chat_input.send_keys(user_input)
        chat_input.send_keys(Keys.RETURN)
        
        # 응답 대기
        time.sleep(2)
        response_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message-text")))
        response = response_element.text
        
    finally:
        driver.quit()
    
    return response

def main():
    user_input = "Hello, how can I help you?"  # 사용자 입력 (변경 가능)
    
    response = start_chat(user_input)
    print("ChatGPT:", response)

if __name__ == "__main__":
    main()
