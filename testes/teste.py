# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import datetime
def test():
                 
          driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          def timer(driver,by,selector,timeout=10):
                  return WebDriverWait(driver,timeout).until(EC.element_to_be_clickable((by,selector)))
          try:
                  timestamp= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                  driver.get("http://127.0.0.1:5000/")
                  timer(driver,By.NAME,"nome").send_keys("alessandro")
                  timer(driver,By.NAME,"nota").send_keys(6)
                  timer(driver,By.TAG_NAME,"button").click()

                  
                  elemento=driver.find_elements(By.ID,"tela")
                  
                  if elemento :
                    driver.save_screenshot(f"teste_{timestamp}.png")
                  else:
                          driver.save_screenshot(f"erro_{timestamp}.png")

          except Exception as e:
                  print (f"{e}")
                  driver.save_screenshot(f"erro_{timestamp}.png")
if __name__=="__main__":
        test()