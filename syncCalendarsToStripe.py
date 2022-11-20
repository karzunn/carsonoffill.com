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

calendars = open("src\\calendars.js", "r").read()
calendars = json.loads(calendars.replace("export default ","").replace(";",""))

prices = open("src\\prices.js", "r").read()
prices = json.loads(prices.replace("export default ","").replace(";","").replace("//easycanvasprints","").replace("//canvasdiscount",""))["calendar"]

if test:
    stripeCalendars = open("src\\test-stripeCalendars.js", "r").read()
    stripeCalendars = json.loads(stripeCalendars.replace("export default ","").replace(";",""))
    newStripeCalendars = []
else:
    stripeCalendars = open("src\\stripeCalendars.js", "r").read()
    stripeCalendars = json.loads(stripeCalendars.replace("export default ","").replace(";",""))
    newStripeCalendars = []

for c in calendars:
    for size in c["sizes"]:
        newCalendar={}
        newCalendar["description"] = "{} - {} - {}".format(c["name"],"calendar",size)
        existingCalendar = [sc for sc in stripeCalendars if sc["description"] == newCalendar["description"]]
        if len(existingCalendar) == 0:
            response = stripe.Product.search(
                query='name~"{}"'.format(newCalendar["description"]),
            )
            if len(response["data"]) != 0:
                newCalendar["product"] = response["data"][0]["id"]
            else:
                response = stripe.Product.create(
                    name=newCalendar["description"],
                    images=["{}/{}".format(base,c["thumb"])]
                )
                newCalendar["product"] = response["id"]
            response = stripe.Price.search(
                query='product:"{}"'.format(newCalendar["product"]),
            )
            if len(response["data"]) != 0:
                newCalendar["price"] = response["data"][0]["id"]
            else:
                response = stripe.Price.create(
                    unit_amount=int(prices["sizes"][size]*100),
                    currency="usd",
                    product=newCalendar["product"],
                    tax_behavior="exclusive"
                )
                newCalendar["price"] = response["id"]
        else:
            newCalendar = existingCalendar[0]
            response = stripe.Product.modify(
                newCalendar["product"],
                name=newCalendar["description"],
                images=["{}/{}".format(base,c["thumb"])]
            )
            response = stripe.Price.search(
                query='product:"{}"'.format(newCalendar["product"]),
            )
            newCalendar["price"] = response["data"][0]["id"]
            if response["data"][0]["unit_amount"] != int(prices["sizes"][size]*100):
                response = stripe.Price.modify(
                    newCalendar["price"],
                    active=False,
                    tax_behavior="exclusive"
                )
                response = stripe.Price.create(
                    unit_amount=int(prices["sizes"][size]*100),
                    currency="usd",
                    product=newCalendar["product"],
                    tax_behavior="exclusive"
                )
                newCalendar["price"] = response["id"]

        newStripeCalendars.append(newCalendar)

if test:
    open("src\\test-stripeCalendars.js", "w").write("export default ["+",\n".join(map(str,newStripeCalendars)).replace("'",'"')+"];")
else:
    open("src\\stripeCalendars.js", "w").write("export default ["+",\n".join(map(str,newStripeCalendars)).replace("'",'"')+"];")