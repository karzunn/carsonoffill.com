const api = require("lambda-api")();
const stripe_key = process.env.STRIPEKEY;
const stripe = require('stripe')(stripe_key);

api.options('/*', (req,res) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Vary','Origin')
    res.header('Access-Control-Allow-Credentials',true)
    res.header('Access-Control-Expose-Headers','Content-Type, Authorization, Content-Length, X-Requested-With, organization')
    res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With, organization');
    res.status(200).send({});
})

api.post("/checkout", async (req, res) => {
    const session = await stripe.checkout.sessions.create(req.body);
    res.json(session)
})

exports.lambdaHandler = async (event, context) => {
    return await api.run(event, context);
};



