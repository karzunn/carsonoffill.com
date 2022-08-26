<script>
  
  import CartListItem from "./CartListItem.svelte";
  import { cartItems } from "../stores";
  import Photos from "../photos";

  let cartTotal = 0;

  cartItems.subscribe(Items => {
    cartTotal = 0
    Object.keys(Items).map(key => cartTotal += Items[key].price * Items[key].quantity)
  });

</script>

<div class="bg-darkgray h-screen w-full">

  <div class="fixed inset-x-0 top-10screen bg-darkgray w-full h-80screen my-15 overflow-auto">
    {#each Object.keys($cartItems) as cartItemKey}
      <CartListItem
        photo={Photos.filter(d=>d.id == $cartItems[cartItemKey].id)[0]}
        description={cartItemKey}
        price={$cartItems[cartItemKey].price}
        quantity={$cartItems[cartItemKey].quantity}
      />
    {/each}
  </div>

  <div class="fixed inset-x-0 top-0 bg-gray w-full h-10screen my-auto inline-flex">
    <a class="relative text-white bg-darkgray font-bold py-1screen px-2 my-auto ml-1 rounded text-center cursor-pointer" href="#/items">&#129128;</a>
    <h1 class="relative my-auto mx-auto text-center text-white tracking-widest text-2xl">STORE</h1>
  </div>

  <div class="fixed inset-x-0 bottom-0 bg-gray grid grid-cols-2 gap-5 h-10screen">
    <h1 class="text-white text-center mr-3 ml-auto my-auto">
      Total: ${cartTotal.toFixed(2)}
    </h1>
    <div class="bg-green-600 text-white py-2 rounded my-auto text-center cursor-pointer ml-3 mr-auto w-1/3">
      Proceed to Checkout
    </div>
  </div>
</div>
