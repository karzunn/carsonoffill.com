<script>
  
  import CartListItem from "./CartListItem.svelte";
  import { cartItems, history } from "../stores";
  import printProductsProd from "../stripePrints";
  import printProductsDev from "../test-stripePrints";
  import calendarProductsProd from "../stripeCalendars";
  import calendarProductsDev from "../test-stripeCalendars";
  import { get } from 'svelte/store';
  import { querystring } from 'svelte-spa-router';
  import { goBack } from '../functions';
  import { baseUrlDev,baseUrlProd,backendUrlDev,backendUrlProd,env } from "../constants";
  import { addHistory } from "../functions";

  let baseUrl;
  let products = [];
  let backendUrl;

  if (env == "prod") {
    baseUrl = baseUrlProd;
    products.push(...printProductsProd);
    products.push(...calendarProductsProd);
    backendUrl = backendUrlProd;
  }
  if (env == "dev") {
    baseUrl = baseUrlDev;
    products.push(...printProductsDev);
    products.push(...calendarProductsDev);
    backendUrl = backendUrlDev;
  }

  let cartTotal = 0;

  let queryparams = {};
  let vars = $querystring.split('&');
  for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split('=');
      queryparams[pair[0]] = pair[1];
  }

  addHistory();
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  async function checkout() {
    let items = get(cartItems);
    let response = await fetch(`${backendUrl}/checkout`,{
      method:"POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        success_url: `${baseUrl}/#/thankyou?empty=true`,
        cancel_url: `${baseUrl}/#/cart`,
        line_items: Object.keys(items).map(key=>{
          let item = products.filter(product=>product.description == key)[0]
          return {price:item.price,quantity:items[key].quantity}
        }),
        automatic_tax: {  enabled: true }, //Overridden later in the backend for safety
        mode: 'payment', //Overridden later in the backend for safety
        shipping_address_collection: { allowed_countries: ["US"] } //Overridden later in the backend for safety
      })
    })
    let session = await response.json();
    window.location.href = session.url;
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
        thumb={$cartItems[cartItemKey].thumb}
        name={$cartItems[cartItemKey].name}
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
