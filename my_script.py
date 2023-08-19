from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from git import Repo
import logging
import time
import configparser

# 로깅 설정
logging.basicConfig(filename='app.log', level=logging.INFO)

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def commit_and_push_changes(repo_path, commit_message="Automatic commit"):
    repo = Repo(repo_path)
    repo.git.add(update=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def start_chat(user_input, headless=False, chrome_driver_path):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("https://www.chatgpt.com/")
    wait = WebDriverWait(driver, 20)
    chat_input = wait.until(EC.presence_of_element_located((By.ID, "chat-input")))
    chat_input.send_keys(user_input)
    chat_input.send_keys(Keys.RETURN)
    time.sleep(2)
    response_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message-text")))
    response = response_element.text
    driver.quit()
    return response

def main():
    config = load_config()
    chrome_driver_path = config['Paths']['chrome_driver_path']
    repo_path = config['Paths']['repo_path'].replace("\\", "\\\\") # 유니코드 에러 해결
    user_input = "Hello, how can I help you?"

    try:
        response = start_chat(user_input, headless=True, chrome_driver_path=chrome_driver_path)
        print("ChatGPT:", response)
        commit_and_push_changes(repo_path, "Updated chat automation code")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
    logging.info("Automation task completed.")
