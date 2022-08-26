<script>
  import { cartItems } from "../stores";
  import { getContext } from 'svelte';
  import prices from "../prices";
  const { close } = getContext('simple-modal');
  export let photo = {};
  let selectedType = document.getElementsByClassName('selected type')[0].id;
  let selectedSize = document.getElementsByClassName('selected size')[0].id;
  let selectedPhoto = photo.name;
  let description = `${selectedPhoto} - ${selectedType} - ${selectedSize}`;
  let price = prices[selectedType].sizes[selectedSize];

  function addToCart(){
    cartItems.update(cartItems => {
      if (cartItems[description]){
        cartItems[description].quantity += 1
      }
      else{
        cartItems[description] = {
          "id":photo.id,
          "price":price,
          "quantity":1
        }
      }
      return cartItems;
    });
    close();
  }

  cartItems.subscribe(cartItems => localStorage.setItem("cartItems", JSON.stringify(cartItems)));
</script>

<div class="w-full">
    <h1 class="text-center mb-4 mx-auto text-2xl font-bold">ADD TO CART?</h1>
    <h1 class="text-center mb-6 mx-auto text-xl">{description}</h1>
    <div class="bg-green-600 text-white px-4 py-2 rounded m-auto text-center w-1/2 cursor-pointer" on:click={addToCart}>ADD</div>
</div>