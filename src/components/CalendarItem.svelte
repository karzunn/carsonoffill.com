<script>
	import { Modal, bind } from 'svelte-simple-modal';
  import AddToCartModal from './AddToCartModal.svelte';
  import { onMount } from 'svelte';
  import calendars from "../calendars";
  import prices from "../prices";
  import { cartItems, history } from "../stores";
  import { writable } from 'svelte/store';
  import { goBack, addHistory } from '../functions';
  export const modal = writable(null);
  export let params = {};

  window.scrollTo(0, 0);

  let calendar = calendars.filter(d=>d.id == params.id)[0]
  if (!calendar) {
    calendar = calendars[0];
    window.location.href = '/#/unavailable';
  }
  addHistory();
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  const showModal = () => modal.set(bind(AddToCartModal, { item: calendar }));

  function calcPrice(){
    let priceDisplay = document.getElementById('price');
    let selectedSize = document.getElementsByClassName('selected size')[0].id;
    let price = prices[calendar.type].sizes[selectedSize];
    priceDisplay.innerHTML = "$" + price.toString() + "*";
  }

  let selectedPrintSize = false;

  function selectSize(e){
    let addToCartButton = document.getElementById('addToCart');
    let freeShipping = document.getElementById('freeShipping');
    let priceDisplay = document.getElementById('price');
    let selectSizeMessage = document.getElementById('selectSizeMessage');
    let types = document.querySelectorAll('.size');
    for (let i=0;i<types.length;i++){
        types[i].classList.remove("selected"); types[i].classList.add("opacity-25");
    };
    let selected = e ? e.target : types[0];
    selectedPrintSize = selected.id;
    selected.classList.add("selected"); selected.classList.remove("opacity-25");
    addToCartButton.style.display = "block";
    priceDisplay.style.display = "block";
    freeShipping.style.display = "block";
    selectSizeMessage.style.display = "none";
    calcPrice();
  }

  function generateSizes(){
    let sizesContainer = document.getElementById("sizes");
    sizesContainer.innerHTML = "";
    let sizes = calendar.sizes;
    for (let size of sizes){
      let sizeElement = document.createElement("div");
      sizeElement.className = "lg:text-base text-xs bg-brand text-white py-2 px-4 rounded my-4 lg:mr-4 mx-2 text-center size opacity-25 cursor-pointer";
      sizeElement.id = size;
      sizeElement.onclick = selectSize;
      sizeElement.innerHTML = size
      sizesContainer.appendChild(sizeElement);
    }
  }

  let cartItemCount = 0;

  cartItems.subscribe(Items => {
    cartItemCount = 0
    Object.keys(Items).map(key => cartItemCount += Items[key].quantity)
	});

  onMount(async () => {
    generateSizes();
	});
</script>

<div id="body" class="w-screen h-screen bg-darkgray">

  <div class="grid lg:grid-cols-3 grid-cols-1 gap-4 justify-center bg-darkgray text-white">

    <div class="justify-center w-full col-span-1 lg:col-span-2">
      <img
        class="object-contain lg:h-screen h-40screen w-full justify-center bg-black"
        src={calendar.image}
        alt={calendar.name}
        id="imageContainer"
      />
      <div class="absolute bg-black bg-opacity-75" id="topCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="bottomCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="leftCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="rightCrop"></div>
    </div>

    <a class="fixed top-0 right-0 text-white bg-gray font-bold w-40px m-2 py-1 justify-center rounded text-center inline-flex cursor-pointer" href="#/cart">
      <div>&#128722;</div>
      <div>{cartItemCount}</div>
    </a>

    <div class="fixed text-2xl pb-1 w-40px m-2 top-0 left-0 text-white bg-gray bg-opacity-75 font-bold rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>

    <div class="w-full tracking-widest lg:h-screen">
      <h1 class="lg:text-left lg:mt-8 text-center lg:text-4xl text-xl">{calendar.name.toUpperCase()}</h1>
      <p class="lg:text-left lg:mt-8 mt-4 text-center lg:text-l text-sm">{calendar.description}</p>
      <h2 class="lg:text-left lg:mt-8 mt-4 text-center lg:text-2xl text-xs">SIZE</h2>
      <div class="flex flex-wrap w-full lg:w-fit justify-center lg:justify-start" id="sizes">
      </div>
      <div class="inline-flex mt-1 lg:mt-8 w-full justify-center lg:justify-start">
        <Modal show={$modal}>
          <div class="bg-accent text-white font-semibold px-4 py-2 rounded mr-2 mb-4 text-center cursor-pointer lg:text-base text-sm" style="display: none;" id="addToCart" on:click={showModal}>ADD TO CART</div>
        </Modal>
        <div class="px-4 mb-4 text-center lg:text-2xl text-base my-auto" style="display: none;" id="price"></div>
        <div class="px-4 mb-4 text-center lg:text-2xl text-base my-auto" id="selectSizeMessage">Please select a size</div>
      </div>
      <div class="text-sm my-0 text-white lg:text-left text-center" style="display: none;" id="freeShipping">Shipping Included*</div>
    </div>

  </div>

</div>
