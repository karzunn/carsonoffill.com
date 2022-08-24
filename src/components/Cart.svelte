<script>
  import CartListItem from "./CartListItem.svelte";
  import { cartItems } from "../stores";
  import Photos from "../photos";
</script>

<div class="bg-darkgray h-screen w-screen">
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
</div>
