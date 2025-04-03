# Import necessary packages
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up webdriver using Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Function to handle shadow-root popup
def bmw_homepage_popup_shadow_root():
    driver.get('https://www.bmw.ca/')  # Open the URL
    driver.maximize_window()  # Maximize window

    try:
        # Wait until the shadow host is present
        host = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'epaas-consent-drawer-shell'))
        )

        # Access the shadow DOM
        shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)

        # Find the accept button inside the shadow DOM
        accept_button = shadow_root.find_element(By.CSS_SELECTOR, 'button.accept-button')

        # Click the accept button
        accept_button.click()
        print('Shadow-root popup handled successfully.')

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        time.sleep(3)  # Optional: Wait to observe the result
        driver.quit()

# if __name__ == "__main__":
#    bmw_homepage_popup_shadow_root()

bmw_homepage_popup_shadow_root()


