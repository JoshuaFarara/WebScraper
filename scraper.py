from selenium import webdriver
import requests

# Set the path to chromedriver.exe
PATH = "C:\\Users\\User\\Desktop\\WebScraper\\chromedriver.exe"

# Create ChromeOptions and set any desired options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Optional: run Chrome in headless mode
chrome_options.add_experimental_option("detach", True)

# Initialize the webdriver with the options
wd = webdriver.Chrome(options=chrome_options)

image_url = "https://4kwallpapers.com/images/wallpapers/windows-11-dark-mode-abstract-background-black-background-3840x2160-8710.jpg"

def download_image(dowload_path, url, file_name):
    image_content = requests.get(url).content