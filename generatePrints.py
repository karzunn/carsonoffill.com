from bs4 import BeautifulSoup
from PIL import Image

image_types = ["Earth","Space","Math"]
allPrints = []
index=0

for image_type in image_types:

    html = open("public\\{}.html".format(image_type), "r").read()
    parsed_html = BeautifulSoup(html,'html.parser')
    photos=parsed_html.body.findAll('article', attrs={'class':'thumb'})
    for photo in photos:
        image = Image.open("public\\{}".format(photo.a['href']))
        square = image.height == image.width
        template={
        "id":str(index),
        "type":"print",
        "name":photo.h2.text,
        "thumb":photo.a.img['src'],
        "image":photo.a['href'],
        "category":image_type.lower(),
        "sizes":{
            "canvas":["8x8","12x12","20x20"] if square else ["12x18","16x24"],
            "foam board":["11x14"],
            "paper":["11x14"]
            }
        }
        allPrints.append(template)
        index+=1

open("src\\prints.js", "w").write("export default ["+",\n".join(map(str,allPrints)).replace("'",'"')+"];")