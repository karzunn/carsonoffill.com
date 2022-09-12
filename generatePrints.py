from bs4 import BeautifulSoup

allPrints = []

#Earth
html = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\public\\Earth.html", "r").read()
parsed_html = BeautifulSoup(html,'html.parser')
photos=parsed_html.body.findAll('article', attrs={'class':'thumb'})
index=0
for photo in photos:
    template={
    "id":str(index),
    "type":"print",
    "name":photo.h2.text,
    "thumb":photo.a.img['src'],
    "image":photo.a['href'],
    "category":"earth",
    "sizes":{
        "canvas":["12x18","16x24"],
        "foam board":["11x14"],
        "paper":["11x14"]
        }
    }
    allPrints.append(template)
    index+=1

#Space
html = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\public\\space.html", "r").read()
parsed_html = BeautifulSoup(html,'html.parser')
photos=parsed_html.body.findAll('article', attrs={'class':'thumb'})
for photo in photos:
    template={
    "id":str(index),
    "type":"print",
    "name":photo.h2.text,
    "thumb":photo.a.img['src'],
    "image":photo.a['href'],
    "category":"space",
    "sizes":{
        "canvas":["12x18","16x24"],
        "foam board":["11x14"],
        "paper":["11x14"]
        }
    }
    allPrints.append(template)
    index+=1

#math
html = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\public\\Math.html", "r").read()
parsed_html = BeautifulSoup(html,'html.parser')
photos=parsed_html.body.findAll('article', attrs={'class':'thumb'})
for photo in photos:
    template={
    "id":str(index),
    "type":"print",
    "name":photo.h2.text,
    "thumb":photo.a.img['src'],
    "image":photo.a['href'],
    "category":"math",
    "sizes":{
        "canvas":["12x18","16x24"],
        "foam board":["11x14"],
        "paper":["11x14"]
        }
    }
    allPrints.append(template)
    index+=1

print(",\n".join(map(str,allPrints)).replace("'",'"'))