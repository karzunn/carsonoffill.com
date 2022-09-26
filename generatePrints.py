from bs4 import BeautifulSoup
from PIL import Image
import json

ppi_map = {"canvas":180,"paper":240}

image_types = ["Earth","Space","Math"]
allPrints = []
index=0

def getMainImage(image_type,name):
    return Image.open("C:\\Users\\cgo_1\\Desktop\\PhotographyStore\\{}\\{}".format(image_type,name))

def sizeWorks(height,width,size,material):
    sizeSplit = size.split("x")
    longest = width if height < width else height
    shortest = width if height > width else height
    longestInches = int(sizeSplit[1]) if int(sizeSplit[0]) < int(sizeSplit[1]) else int(sizeSplit[0])
    shortestInches = int(sizeSplit[1]) if int(sizeSplit[0]) > int(sizeSplit[1]) else int(sizeSplit[0])
    longestPossibleInches = longest/ppi_map[material]
    shortestPossibleInches = shortest/ppi_map[material]
    if longestPossibleInches >= longestInches and shortestPossibleInches >= shortestInches:
        return True
    return False

def generateSizes(height,width,prices):
    template = {}
    for t in prices:
        template[t] = []
        for size in prices[t]["sizes"]:
            if sizeWorks(height,width,size,t):
                template[t].append(size)
    return template


prices = open("src\\prices.js", "r").read()
prices = json.loads(prices.replace("export default ","").replace(";","").replace("//easycanvasprints","").replace("//canvasdiscount",""))["print"]

for image_type in image_types:

    html = open("public\\{}.html".format(image_type), "r").read()
    parsed_html = BeautifulSoup(html,'html.parser')
    photos=parsed_html.body.findAll('article', attrs={'class':'thumb'})
    for photo in photos:
        image = getMainImage(image_type,photo.a['href'].split("/")[-1])
        square = image.height == image.width
        template={
        "id":str(index),
        "type":"print",
        "name":photo.h2.text,
        "thumb":photo.a.img['src'],
        "image":photo.a['href'],
        "category":image_type.lower(),
        "sizes": generateSizes(image.height,image.width,prices)
        }
        allPrints.append(template)
        index+=1

open("src\\prints.js", "w").write("export default ["+",\n".join(map(str,allPrints)).replace("'",'"')+"];")