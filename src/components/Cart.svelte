<script>
  import CartListItem from "./CartListItem.svelte";
  import { cartItems } from "../stores";
  import Photos from "../photos";
</script>

<div class="bg-darkgray min-h-screen h-full w-full">
  <h1 class="bg-gray text-center text-white w-full tracking-widest text-2xl py-3">MY CART</h1>
  <div class="bg-darkgray w-full">
    {#each $cartItems as cartItem}
      <CartListItem
        photo={Photos.filter(d=>d.id == cartItem.id)[0]}
        description={cartItem.description}
        price={cartItem.price}
      />
    {/each}
  </div>
  <div class="fixed inset-x-0 bottom-0 bg-gray grid grid-cols-4 gap-5">
    <div></div>
    <div></div>
    <h1 class="text-white text-center m-auto">
      Total: $100
    </h1>
    <div class="bg-green-600 text-white py-2 rounded m-3 text-center cursor-pointer">
      Proceed to Checkout
    </div>
  </div>
</div>
