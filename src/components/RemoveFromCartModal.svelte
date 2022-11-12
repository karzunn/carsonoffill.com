<script>
  import { cartItems } from "../stores";
  import { getContext } from 'svelte';
  const { close } = getContext('simple-modal');
  export let description = "";

  function popFromCart(){
    cartItems.update(cartItems => {
      delete cartItems[description]
      return cartItems;
    });
    close();
  }

  cartItems.subscribe(cartItems => localStorage.setItem("cartItems", JSON.stringify(cartItems)));
</script>

<div class="w-full">
    <h1 class="text-center mb-4 mx-auto text-2xl font-bold">REMOVE FROM CART?</h1>
    <h1 class="text-center mb-6 mx-auto text-xl">{description}</h1>
    <div class="bg-accent text-white px-4 py-2 rounded m-auto text-center w-1/2 cursor-pointer" on:click={popFromCart}>REMOVE</div>
</div>