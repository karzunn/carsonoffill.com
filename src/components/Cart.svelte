<script>
  
  import { loadStripe } from '@stripe/stripe-js';
  import CartListItem from "./CartListItem.svelte";
  import { cartItems, history } from "../stores";
  import prints from "../prints";
  import productsProd from "../stripePrints";
  import productsDev from "../test-stripePrints";
  import { get } from 'svelte/store';
  import { querystring } from 'svelte-spa-router';
  import { goBack } from '../functions';
  import { baseUrlDev,baseUrlProd,stripeKeyDev,stripeKeyProd,env } from "../constants";
  import { addHistory } from "../functions";

  let stripeKey;
  let baseUrl;
  let products;

  if (env == "prod") {
    stripeKey = stripeKeyProd;
    baseUrl = baseUrlProd;
    products = productsProd;
  }
  if (env == "dev") {
    stripeKey = stripeKeyDev;
    baseUrl = baseUrlDev;
    products = productsDev;
  }

  let cartTotal = 0;
  let stripe;

  let queryparams = {};
  let vars = $querystring.split('&');
  for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split('=');
      queryparams[pair[0]] = pair[1];
  }

  if (queryparams.empty == "true") {
    cartItems.update(cartItems=>{return {}})
  }

  addHistory();
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  async function checkout() {
    let items = get(cartItems);
    stripe = await loadStripe(stripeKey);
    await stripe.redirectToCheckout({
      successUrl: `${baseUrl}/#/cart?empty=true`,
      cancelUrl: `${baseUrl}/#/cart`,
      lineItems: Object.keys(items).map(key=>{
        let item = products.filter(product=>product.description == key)[0]
        return {price:item.price,quantity:items[key].quantity}
      }),
      mode: 'payment',
      shippingAddressCollection: { allowedCountries: ["US"] }
    })
  }

  cartItems.subscribe(Items => {
    cartTotal = 0
    Object.keys(Items).map(key => cartTotal += Items[key].price * Items[key].quantity)
  });

</script>

<div class="bg-darkgray h-screen w-full">

  <div class="fixed inset-x-0 top-10screen bg-darkgray w-full lg:h-80screen h-70screen my-15 overflow-auto">
    {#each Object.keys($cartItems) as cartItemKey}
      <CartListItem
        thumb={prints.filter(d=>d.id == $cartItems[cartItemKey].id)[0].thumb}
        name={prints.filter(d=>d.id == $cartItems[cartItemKey].id)[0].name}
        description={cartItemKey}
        price={$cartItems[cartItemKey].price}
        quantity={$cartItems[cartItemKey].quantity}
      />
    {/each}
  </div>

  <div class="fixed inset-x-0 top-0 bg-gray w-full h-10screen my-auto inline-flex">
    <div class="text-2xl pb-1 px-10px relative text-white bg-darkgray font-bold my-auto ml-1 rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>
    <h1 class="relative my-auto mx-auto text-center text-white tracking-widest text-2xl">CART</h1>
    <div class="text-2xl pb-1 px-10px relative my-auto ml-1 invisible">&#8249;</div>
  </div>

  <div class="fixed inset-x-0 bottom-0 bg-gray grid grid-cols-2 gap-5 h-10screen">
    <h1 class="text-white text-center mr-3 ml-auto my-auto">
      Total: ${cartTotal.toFixed(2)}
    </h1>
    <div on:click={checkout} class="bg-accent text-white font-semibold py-2 px-4 rounded my-auto text-center cursor-pointer ml-3 mr-auto">
      Checkout
    </div>
  </div>
</div>
