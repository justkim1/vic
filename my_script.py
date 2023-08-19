
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from git import Repo
import logging
import time

# 로깅 설정
logging.basicConfig(filename='app.log', level=logging.INFO)

def commit_and_push_changes(repo_path, commit_message="Automatic commit"):
    repo = Repo(repo_path)
    repo.git.add(update=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def start_chat(user_input, headless=False):
    chrome_driver_path = r"C:\Users\7612112\Downloads\chromedriver_win32\chromedriver.exe"
    chrome_service = Service()
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless") # 헤드리스 모드 옵션 추가
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get("https://www.chatgpt.com/")

    
try:
    # ... 기존 코드 ...
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    raise

        wait = WebDriverWait(driver, 20)
        chat_input = wait.until(EC.presence_of_element_located((By.ID, "chat-input")))
        chat_input.send_keys(user_input)
        chat_input.send_keys(Keys.RETURN)
        time.sleep(2)
        response_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message-text")))
        response = response_element.text
    finally:
        driver.quit()

    return response

def main():
    user_input = "Hello, how can I help you?"
    response = start_chat(user_input, headless=True)
    print("ChatGPT:", response)

    # GitHub 연동
    repo_path = "C:\Users\7612112\Documents\GitHub\vic" # 로컬 GitHub 저장소 경로
    commit_and_push_changes(repo_path, "Updated chat automation code")

if __name__ == "__main__":
    main()
    logging.info("Automation task completed.") # 로깅 추가
