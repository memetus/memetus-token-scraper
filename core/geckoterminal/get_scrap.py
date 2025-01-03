import sys
from selenium.get_selenium_driver import capture_screenshot, get_chart_image, get_selenium_driver
from utils.error.argv_error import handle_geckoterminal_argv_error

def get_scrap_chart(driver, url: str):
  get_chart_image(driver, url)

def get_scrap_price_text(driver, url: str):
  capture_screenshot(driver, url)

def get_scrap_token(type: str, url: str):
  if type == 'price-text':
    get_scrap_price_text(url)
  elif type == 'chart':
    get_scrap_chart(url)

def main(argv):
  driver = None
  url = None
  if (len(argv) < 3):
    handle_geckoterminal_argv_error(1, [])
  elif (len(argv) > 3):
    handle_geckoterminal_argv_error(2, [])
  else:
    try:
      url = f"https://www.geckoterminal.com/solana/pools/{argv[2]}"
      driver = get_selenium_driver()
      get_scrap_token(argv[1], url)

    except Exception as e:
      print(e)
    finally:
      if driver:
        driver.quit()

if __name__ == "__main__":
  main(sys.argv)