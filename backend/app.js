const api = require("lambda-api")();
const stripe = require('stripe')(stripe_key);
const stripe_key = require('./keys').key;

api.post("/checkout", async (req, res) => {

    const session = await stripe.checkout.sessions.create(req.body);
    res.json(session)

})

exports.lambdaHandler = async (event, context) => {
    return await api.run(event, context);
};



