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

a = input("Waiting for user input to start...")

wd.execute_script("window.scrollTo(0, 0);")

page_html = wd.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib ViTmJb BUooTd"})

print(len(containers))

len_containers = len(containers)
print("Found %s image containers"%(len_containers))

# //*[@id="islrg"]/div[1]/div[1]
# //*[@id="islrg"]/div[1]/div[3]
thumbPath = """//*[@id="islrg"]/div[1]/div[1]"""
# Get element, in this case it is the thumbnail
thumbnail = wd.find_element(By.XPATH, thumbPath)
# use of actionchain object
action.move_to_element(thumbnail).click().perform()
print("Thumbnail clicked...")

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue

    xPath = wd.find_element(By.XPATH,"""//*[@id="islrg"]/div[1]/div[%s]"""%(i))

    # Grabbing the URL of the small preview image
    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = wd.find_element(By.XPATH, previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src") 

    # click on the image container
    action.move_to_element(xPath).click().perform()

    # Starting a while True loop to wait until we have the URL inside the large image view is different from the preview one
    # timeStarted = time.time()
    # while True:
    #     # timeout_values = [10, 15, 20, 25]  # Adjust the timeout values as needed

    #     # for timeout in timeout_values:
    #     #     # Start a timer
    #     #     start_time = time.time()

    #     fullResPath = """//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]"""
    #     wait = WebDriverWait(wd, 5) # # Wait for the full-resolution image element to become available
    #     imageElement = wait.until(EC.presence_of_element_located((By.XPATH, fullResPath))) # wd.find_element
    #     # //*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    #     # //*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[2]
    #     # //*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]
    #     # end_time = time.time()
    #     # wait_time = end_time - start_time
    #     # print(f"Timeout: {timeout} seconds | Wait time: {wait_time} seconds")
    #     imageURL = imageElement.get_attribute("src")
    #     print("Full res URL: ", imageURL)


        # print("Waiting for the full res image")
        # if imageURL != previewImageURL:
        #     # print()
        #     print("Full res URL: ", imageURL)
        #     break
        # else:
        #     # making a timeout if the full res img can't be loaded
        #     currentTime = time.time()

        #     if currentTime - timeStarted > 10:
        #         print("Timeout! will download lower resolutionm image and move onto the next one")
        #         break
        
        # #download image
        # try:
        #     download_image(imageURL, folder_name, i)
        #     print("Downloaded element s%s out of total. URL: %s" % (i, len_containers))
        # except:
        #     print("Couldn't download image %s, continuing downloading the next image. ")