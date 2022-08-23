<script>
  import { cartItems } from "../stores";
  import { getContext } from 'svelte';
  const { close } = getContext('simple-modal');
  export let photo = {};
  let selectedType = document.getElementsByClassName('selected type')[0].id;
  let selectedSize = document.getElementsByClassName('selected size')[0].id;
  let selectedPhoto = photo.name;
  let description = `${selectedPhoto} - ${selectedType} - ${selectedSize}`;

  function addToCart(){
    let cartItem = {
      "id":photo.id,
      "description":description
    }
    cartItems.update(cartItems => cartItems.concat(cartItem));
    close();
  }
</script>

<div class="w-full">
    <h1 class="text-center mb-4 mx-auto text-2xl">ADD TO CART?</h1>
    <h1 class="text-center mb-6 mx-auto text-xl">{description}</h1>
    <div class="bg-green-600 text-white px-4 py-2 rounded m-auto text-center w-1/2" on:click={addToCart}>ADD</div>
</div>