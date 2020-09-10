
import urllib.request
x=input("Enter the URL to download image from.\n")
x=str(x)
y=input("Enter file name\n")
y=str(y)
def download_web_image(url):
    name= y + ".jpg"
    urllib.request.urlretrieve(url,name)

download_web_image(x)
