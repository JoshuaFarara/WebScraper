from selenium import webdriver
import requests
import io
from PIL import Image
import time

# Set the path to chromedriver.exe
PATH = "C:\\Users\\User\\Desktop\\WebScraper\\chromedriver.exe"

# Create ChromeOptions and set any desired options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Optional: run Chrome in headless mode
chrome_options.add_experimental_option("detach", True)

# Initialize the webdriver with the options
wd = webdriver.Chrome(options=chrome_options)


def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?sca_esv=566330112&rlz=1C1CHBF_enUS791US791&q=black+and+white+backgrounds+3840x2160&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiFz8iBrbWBAxVilGoFHXQDBK8Q0pQJegQICxAB&biw=1920&bih=931&dpr=1"
    wd.get(url)

    image_urls = set()

    while len(image_urls) < max_images: 
        pass


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content # get the content of the image, get request to the url of the image that we want
        image_file = io.BytesIO(image_content) # stores the file as a binary datatype on cpu
        image = Image.open(image_file) # converts the binary data to pil image
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("success")
    except Exception as e:
        print('FAILED -', e)


    
# download_image("", image_url, "test.jpg")
get_images_from_google(wd, 2, 10)
wd.quit()
