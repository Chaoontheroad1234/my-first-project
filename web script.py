from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

options = Options()

driver = webdriver.Chrome(options=options)
driver.get("https://www.four-paws.org/campaigns-topics/topics/companion-animals/10-facts-about-cats")

img = driver.find_element(By.TAG_NAME, "img")
img_url =img.get_attribute("src")
print("Image URL:", img_url)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36" 
    }
response = requests.get(img_url, headers=headers)
if response.status_code == 200:
    with open("cat_image.jpg", "wb") as file:
        file.write(response.content)
    print("image saved as cat_image.jpg")
else:
    print("failed to download image", response.status_code)
driver.quit()