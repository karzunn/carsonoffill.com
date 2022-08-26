<script>
  import { cartItems } from "../stores";
  export let description = "";
  export let price = "";
  export let photo = {};
  export let quantity = 0;
  import { Modal, bind } from 'svelte-simple-modal';
  import RemoveFromCartModal from './RemoveFromCartModal.svelte';
  import { writable } from 'svelte/store';
  export const modal = writable(null);
  const showModal = () => modal.set(bind(RemoveFromCartModal, { description: description }));

  function addItem(){
    cartItems.update(cartItems => {
      cartItems[description].quantity += 1
      return cartItems;
    });
  }

  function removeItem(){
    cartItems.update(cartItems => {
      if (cartItems[description].quantity == 1){
        showModal()
      }
      else{
        cartItems[description].quantity -= 1
      }
      return cartItems;
    });
  }

  cartItems.subscribe(cartItems => localStorage.setItem("cartItems", JSON.stringify(cartItems)));
  
</script>

<Modal show={$modal}></Modal>
<div class="grid grid-cols-4 gap-5 m-3">
  <img
    src={photo.thumb}
    alt={photo.name}
    class="object-contain h-20screen"
  />
  <h1 class="text-white text-center my-auto mx-auto">
    {description}
  </h1>
  <h1 class="text-white text-center my-auto mx-auto">
    ${price}
  </h1>
  <div class="inline-flex my-auto mx-auto">
    <div class="text-white bg-gray font-bold py-1 px-2 mx-3 rounded text-center inline-flex cursor-pointer my-auto" on:click={removeItem}>-</div>
    <h1 class="text-white text-center my-auto">
      {quantity}
    </h1>
    <div class="text-white bg-gray font-bold py-1 px-2 mx-3 rounded text-center inline-flex cursor-pointer my-auto" on:click={addItem}>+</div>
  </div>
</div>
