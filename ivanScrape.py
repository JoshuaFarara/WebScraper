import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


def download_image(url, folder_name, num):

    #write image to file
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), 'wb') as file:
            file.write(response.content)

folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

# chromeDriverPath= r'C:\Users\User\Documents\MyPythonScripts\Drivers\chromedriver.exe'
# driver = webdriver.Chrome(chromeDriverPath)

# Create ChromeOptions and set any desired options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Optional: run Chrome in headless mode
chrome_options.add_experimental_option("detach", True)

# Initialize the webdriver with the options
wd = webdriver.Chrome(options=chrome_options)
action = ActionChains(wd) # create action chain object

# URL to be searched, get the URL
search_URL = "https://www.google.com/search?q=car&source=Inms&tbm=isch"
wd.get(search_URL)

# add an auttomatic scroll to bottom feature using scrollto(), time.sleep()

a = input("Waiting for user input to start...")

wd.execute_script("window.scrollTo(0, 0);")

page_html = wd.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib ViTmJb BUooTd"})
# thumbnail_elements = []
# for container in containers:
#     thumbnail = container.find('div')
#     if thumbnail:
#         thumbnail_elements.append(thumbnail)

print(len(containers))
# print(len(thumbnail_elements))
# print(thumbnail_elements)

# len_containers = len(containers)
# print("Found %s image containers"%(len_containers))


# for i in range(1, len_containers+1):
#     if i % 25 == 0:
#         continue
for num, thumbnail in enumerate(containers, start=1):
    if num % 25 == 0:
        continue
    try:
        # xPath = wd.find_element(By.XPATH,"""//*[@id="islrg"]/div[1]/div[%s]"""%(i))
        # action.move_to_element(xPath).click().perform()
        thumbPath = """//*[@id="islrg"]/div[1]/div[%s]""" %(num)
        # Get element, in this case it is the thumbnail
        nail = wd.find_element(By.XPATH, thumbPath)
        # use of actionchain object
        action.move_to_element(nail).click().perform()
        # print("Thumbnail clicked...")
         # Click on the current thumbnail
        # action.move_to_element(thumbnail).click().perform()
        print(f"Thumbnail {num} clicked...")

        time.sleep(2)

        fullResPath = """//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]"""
        # fullResolutionImage = '//img[@class="n3VNCb n3VNCb"]'
        fullResElement = wd.find_element(By.XPATH, fullResPath) # wd.find_element
        # fullResElement = wd.find_element(By.XPATH, fullResolutionImage) # wd.find_element
        fullResImage = fullResElement.get_attribute("src")
      
        print("Full res URL: ", fullResImage)

        # thumbPath = """//*[@id="islrg"]/div[1]/div[1]"""
        # # Get element, in this case it is the thumbnail
        # thumbnail = wd.find_element(By.XPATH, thumbPath)
        # # use of actionchain object
        # action.move_to_element(thumbnail).click().perform()
        # print("Thumbnail clicked...")
        # Close the full-resolution image view by clicking on the X button
        # close_button = wd.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[3]/span[1]/div[1]/span')
        # action.move_to_element(close_button).click().perform()
        # action.move_to_element(nail).click().perform()


    except Exception as e:
        print(f'Error: {str(a)}')

wd.quit()