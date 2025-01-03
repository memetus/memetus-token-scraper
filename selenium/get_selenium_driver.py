from config.selenium_config import get_chart_queries, get_target_area_queries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time

browser = webdriver.Chrome()

def click_element_by_xpath(driver, xpath, element_name, wait_time=10):
  time.sleep(20)
  try:
      element = WebDriverWait(driver, wait_time).until(
          EC.element_to_be_clickable((By.XPATH, xpath))
      )
      element.click()
      time.sleep(50) 
  except TimeoutException:
      print(f"{element_name} Cannot find element")
  except ElementClickInterceptedException:
      print(f"{element_name} Cannot click on element")
  except Exception as e:
      print(f"{element_name} Unknown error occured: {e}")

def capture_screenshot(driver):
  time.sleep(20)
  driver.save_screenshot('screenshot.png')

  for query in get_target_area_queries():
    element = driver.find_element(By.CSS_SELECTOR, query['element_query'])
    location = element.location  
    size = element.size  

    device_pixel_ratio = driver.execute_script("return window.devicePixelRatio;")

    x = int(location['x'] * device_pixel_ratio)
    y = int(location['y'] * device_pixel_ratio)
    width = int(size['width'] * device_pixel_ratio)
    height = int(size['height'] * device_pixel_ratio)
    image = Image.open('screenshot.png')
    cropped_image = image.crop((x, y, x + width, y + height))

    cropped_image.save(query['file_name'])

def get_chart_image(driver, url, queries):
  driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[4]/div[1]/div/div[1]/div/iframe'))
  for query in get_chart_queries():
    click_element_by_xpath(driver, query['element_query'], query['element_name'])

def setup_browser_options(download_path: str):
  option = Options()
  download_dir = download_path

  option.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  
    "download.prompt_for_download": False,       
    "download.directory_upgrade": True,          
    "safebrowsing.enabled": True                 
  })

  option.add_argument('--start-maximized')
  return option

def create_selenium_driver():
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=setup_browser_options())
  return driver

def get_selenium_driver():
  driver = None
  try:
    driver = create_selenium_driver()
    return driver
  except Exception as e:
    print(f'Error: {e}')
