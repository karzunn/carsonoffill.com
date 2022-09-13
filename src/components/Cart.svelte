<script>
  
  import {loadStripe} from '@stripe/stripe-js';
  import CartListItem from "./CartListItem.svelte";
  import { cartItems } from "../stores";
  import prints from "../prints";

  let cartTotal = 0;
  let stripe;

  async function checkout() {
    stripe = await loadStripe('pk_live_51LVKz5A8Ti7QZNbk5BXTOQWtokfkojk4vLivJgZ9wqFnANeLLkAIWIMcRVKlPwEfL5lu3U8AHg7Dlw4AG0N98Mj6004PICG4g8');
    await stripe.redirectToCheckout({
      successUrl: 'https://carsonoffill.com/#/store/cart?empty=true',
      cancelUrl: 'https://carsonoffill.com/#/store/cart',
      lineItems: [
        {price: 'price_1LhNSpA8Ti7QZNbkcSBST6iA', quantity: 2},
      ],
      mode: 'payment',
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
    <div class="text-2xl pb-1 px-10px relative text-white bg-darkgray font-bold my-auto ml-1 rounded text-center cursor-pointer" onclick="history.go(-1); event.preventDefault();">&#8249;</div>
    <h1 class="relative my-auto mx-auto text-center text-white tracking-widest text-2xl">CART</h1>
    <div class="text-2xl pb-1 px-10px relative my-auto ml-1 invisible">&#8249;</div>
  </div>

  <div class="fixed inset-x-0 bottom-0 bg-gray grid grid-cols-2 gap-5 h-10screen">
    <h1 class="text-white text-center mr-3 ml-auto my-auto">
      Total: ${cartTotal.toFixed(2)}
    </h1>
    <div on:click={checkout} class="bg-green-600 text-white py-2 px-4 rounded my-auto text-center cursor-pointer ml-3 mr-auto">
      Checkout
    </div>
  </div>
</div>
