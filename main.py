from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tkinter import messagebox

market_list =["https://www.mediamarkt.com.tr/","https://www.vatanbilgisayar.com/"]

driver= webdriver.Chrome()
driver.maximize_window()

driver.get(market_list[0])
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"query")))

price1=driver.find_element(By.NAME,"query")

price1.send_keys("iphone 14 128")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[2]/div/form/button/span")))

button=driver.find_element(By.XPATH,"/html/body/header/div/div/div[2]/div/form/button/span")
button.click()

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"mm-products")))
product= driver.find_element(By.CLASS_NAME,"mm-products")
priceiphone14 =product.text.splitlines()

print(f"iphone 14 128gb mediamarket değeri {priceiphone14[2]} ")

driver.close()

driver2= webdriver.Chrome()
driver2.maximize_window()

driver2.get(market_list[1])
WebDriverWait(driver2,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"search__input")))

price2=driver2.find_element(By.CLASS_NAME,"search__input")

price2.send_keys("iphone 14 128")
WebDriverWait(driver2,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/header/nav/div[2]/div[1]/div/div/div[2]/div[2]/div/div/button")))

button2=driver2.find_element(By.XPATH,"/html/body/header/nav/div[2]/div[1]/div/div/div[2]/div[2]/div/div/button")
button2.click()

WebDriverWait(driver2,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"product-list__content")))
product2= driver2.find_element(By.CLASS_NAME,"product-list__content")
price14v= product2.text.splitlines()
print(f"iphone 14 128gb vatan değeri {price14v[3]}")
driver2.close()

messagebox.showinfo("iphone 14 128gb değeri",f"vatanda {price14v[3]} \nmedimarkette {priceiphone14[2]}" )






