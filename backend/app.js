const api = require("lambda-api")();
const stripe_key = process.env.STRIPEKEY;
const stripe = require('stripe')(stripe_key);

api.use((req, res, next) => {
    res.cors({headers:'*'})
    next();
});

api.options('/*', (req,res) => {
    res.status(200).send({});
})

api.post("/checkout", async (req, res) => {
    let payload = typeof req.body == "string" ? JSON.parse(req.body) : req.body;
    payload.mode = "payment";
    payload.automatic_tax = { enabled: true };
    payload.shipping_address_collection = { allowed_countries: ["US"] };
    const session = await stripe.checkout.sessions.create(payload);
    res.json(session);
})

exports.lambdaHandler = async (event, context) => {
    return await api.run(event, context);
};



