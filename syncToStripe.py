import stripe
stripe.api_key = "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"
import json

prints = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\src\\prints.js", "r").read()
prints = json.loads(prints.replace("export default ","").replace(";",""))

prices = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\src\\prices.js", "r").read()
prices = json.loads(prices.replace("export default ","").replace(";","").replace("//easycanvasprints","").replace("//canvasdiscount",""))["print"]

stripePrints = open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\src\\stripePrints.js", "r").read()
stripePrints = json.loads(stripePrints.replace("export default ","").replace(";",""))
newStripePrints = []

for p in prints:
    for cat in p["sizes"]:
        for size in p["sizes"][cat]:
            newPrint={}
            description = "{} - {} - {}".format(p["name"],cat,size)
            newPrint["description"] = description
            existingPrint = [sp for sp in stripePrints if sp["description"] == description]
            if len(existingPrint) == 0:
                response = stripe.Product.create(name=description,images=["http://carsonoffill-dev.s3-website-us-east-1.amazonaws.com/"+p["thumb"]])
                newPrint["id"] = response["id"]
            else:
                existingPrint = existingPrint[0]
                newPrint["id"] = existingPrint["id"]
            if "price" not in existingPrint:
                response = stripe.Price.create(
                    unit_amount=int(prices[cat]["sizes"][size]*100),
                    currency="usd",
                    product=newPrint["id"],
                )
                newPrint["price"] = response["id"]
            newStripePrints.append(newPrint)

open("C:\\Users\\cgo_1\\Desktop\\Code\\carsonoffill.com\\src\\stripePrints.js", "w").write("export default "+",\n".join(map(str,stripePrints)).replace("'",'"')+";")
