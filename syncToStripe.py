test = False

import stripe
import json
import keys

base = ""

if test:
    stripe.api_key = keys.dev_api_key
    base = "http://carsonoffill-dev.s3-website-us-east-1.amazonaws.com"
else:
    stripe.api_key = keys.prod_api_key
    base = "http://carsonoffill.com"

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
            sizeSplit = size.split("x")
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
                newPrint["price"] = response["data"][0]["id"]
                if True:#response["data"][0]["unit_amount"] != int(prices[cat]["sizes"][size]*100):
                    response = stripe.Price.modify(
                        newPrint["price"],
                        active=False,
                        tax_behavior="exclusive"
                    )
                    response = stripe.Price.create(
                        unit_amount=int(prices[cat]["sizes"][size]*100),
                        currency="usd",
                        product=newPrint["product"],
                        tax_behavior="exclusive"
                    )
                    newPrint["price"] = response["id"]

            newStripePrints.append(newPrint)

if test:
    open("src\\test-stripePrints.js", "w").write("export default ["+",\n".join(map(str,newStripePrints)).replace("'",'"')+"];")
else:
    open("src\\stripePrints.js", "w").write("export default ["+",\n".join(map(str,newStripePrints)).replace("'",'"')+"];")