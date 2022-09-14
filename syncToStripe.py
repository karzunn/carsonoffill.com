test = False

import stripe
import json

base = ""

if test:
    stripe.api_key = "sk_test_51LVKz5A8Ti7QZNbk73gaMw7c2RL10pr5AkEC539YRkPOPBTRTDdTfgXebU41reiSU0DLKrzOhvQdWFOSLcKCmV2e00k40KMQsH"
    base = "http://carsonoffill-dev.s3-website-us-east-1.amazonaws.com"
else:
    stripe.api_key = "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"
    base = "http://carsonoffill.com"

import json

prints = open("src\\prints.js", "r").read()
prints = json.loads(prints.replace("export default ","").replace(";",""))

prices = open("src\\prices.js", "r").read()
prices = json.loads(prices.replace("export default ","").replace(";","").replace("//easycanvasprints","").replace("//canvasdiscount",""))["print"]

if test:
    stripePrints = open("src\\test-stripePrints.js", "r").read()
    stripePrints = json.loads(stripePrints.replace("export default ","").replace(";",""))
    newStripePrints = []
else:
    stripePrints = open("src\\stripePrints.js", "r").read()
    stripePrints = json.loads(stripePrints.replace("export default ","").replace(";",""))
    newStripePrints = []

for p in prints:
    for cat in p["sizes"]:
        for size in p["sizes"][cat]:
            newPrint={}
            newPrint["description"] = "{} - {} - {}".format(p["name"],cat,size)
            existingPrint = [sp for sp in stripePrints if sp["description"] == newPrint["description"]]
            if len(existingPrint) == 0:
                response = stripe.Product.search(
                    query='name~"{}"'.format(newPrint["description"]),
                )
                if len(response["data"]) != 0:
                    newPrint["product"] = response["data"][0]["id"]
                else:
                    response = stripe.Product.create(
                        name=newPrint["description"],
                        images=["{}/{}".format(base,p["thumb"])]
                    )
                    newPrint["product"] = response["id"]
                response = stripe.Price.search(
                    query='product:"{}"'.format(newPrint["product"]),
                )
                if len(response["data"]) != 0:
                    newPrint["price"] = response["data"][0]["id"]
                else:
                    response = stripe.Price.create(
                        unit_amount=int(prices[cat]["sizes"][size]*100),
                        currency="usd",
                        product=newPrint["product"],
                    )
                    newPrint["price"] = response["id"]
            else:
                newPrint = existingPrint[0]
                response = stripe.Product.modify(
                    newPrint["product"],
                    name=newPrint["description"],
                    images=["{}/{}".format(base,p["thumb"])]
                )
                response = stripe.Price.search(
                    query='product:"{}"'.format(newPrint["product"]),
                )
                if response["data"][0]["unit_amount"] != int(prices[cat]["sizes"][size]*100):
                    response = stripe.Price.modify(
                        newPrint["price"],
                        active=False
                    )
                    response = stripe.Price.create(
                        unit_amount=int(prices[cat]["sizes"][size]*100),
                        currency="usd",
                        product=newPrint["product"],
                    )
                    newPrint["price"] = response["id"]
                newPrint["price"] = response["data"][0]["id"]


            newStripePrints.append(newPrint)

if test:
    open("src\\test-stripePrints.js", "w").write("export default ["+",\n".join(map(str,newStripePrints)).replace("'",'"')+"];")
else:
    open("src\\stripePrints.js", "w").write("export default ["+",\n".join(map(str,newStripePrints)).replace("'",'"')+"];")