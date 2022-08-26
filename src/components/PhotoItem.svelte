<script>
	import { Modal, bind } from 'svelte-simple-modal';
  import AddToCartModal from './AddToCartModal.svelte';
  import { onMount } from 'svelte';
  import photos from "../photos";
  import prices from "../prices";
  import { cartItems } from "../stores";
  import { writable } from 'svelte/store';
  export const modal = writable(null);
  export let params = {};
  let photo = photos.filter(d=>d.id == params.id)[0]
  if (!photo)
  {
    window.history.go(-1);
    window.location.reload();
  }
  window.scrollTo(0,0);
  const showModal = () => modal.set(bind(AddToCartModal, { photo: photo }));

  function calcPrice(){
      let selectedType = document.getElementsByClassName('selected type')[0].id;
      let selectedSize = document.getElementsByClassName('selected size')[0].id;
      let price = prices[selectedType].sizes[selectedSize];
      document.getElementById("price").innerHTML = "$" + price.toString();
  }

  function selectType(e){
      let types = document.querySelectorAll('.type');
      for (let i=0;i<types.length;i++){
          types[i].classList.remove("selected"); types[i].classList.add("opacity-25");
      };
      let selected = e ? e.target : types[0];
      selected.classList.add("selected"); selected.classList.remove("opacity-25");
      if (e)
      {
          generateSizes();
          selectSize();
          calcPrice();
      }
  }

  function selectSize(e){
      let types = document.querySelectorAll('.size');
      for (let i=0;i<types.length;i++){
          types[i].classList.remove("selected"); types[i].classList.add("opacity-25");
      };
      let selected = e ? e.target : types[0];
      selected.classList.add("selected"); selected.classList.remove("opacity-25");
      calcPrice();
  }

  function generateTypes(){
      let typesContainer = document.getElementById("types");
      let types = Object.keys(photo.sizes);
      for (let type of types){
          let typeElement = document.createElement("div");
          typeElement.className = "bg-grayblue text-white py-2 px-4 rounded my-4 mr-4 type opacity-25 cursor-pointer";
          typeElement.id = type;
          typeElement.onclick = selectType;
          typeElement.innerHTML = type.toUpperCase();
          typesContainer.appendChild(typeElement);
      }
  }

  function generateSizes(){
      let selectedType = document.getElementsByClassName('selected type')[0].id;
      let sizesContainer = document.getElementById("sizes");
      sizesContainer.innerHTML = "";
      let sizes = photo.sizes[selectedType];
      for (let size of sizes){
          let sizeElement = document.createElement("div");
          sizeElement.className = "bg-grayblue text-white py-2 px-4 rounded my-4 mr-4 text-center size opacity-25 cursor-pointer";
          sizeElement.id = size;
          sizeElement.onclick = selectSize;
          sizeElement.innerHTML = size;
          sizesContainer.appendChild(sizeElement);
      }
  }

  let cartItemCount = 0;

  cartItems.subscribe(Items => {
    cartItemCount = 0
    Object.keys(Items).map(key => cartItemCount += Items[key].quantity)
	});

  onMount(async () => {
    generateTypes();
    selectType();
    generateSizes();
    selectSize();
	});
</script>

<a class="absolute top-0 left-0 text-white bg-gray font-bold py-1 px-2 m-1 rounded text-center cursor-pointer" href="#/items">&#129128;</a>
<a class="absolute bottom-0 right-0 text-white bg-gray font-bold py-1 px-2 m-1 rounded text-center inline-flex cursor-pointer" href="#/cart">
  <div>&#128722;</div>
  <div>{cartItemCount}</div>
</a>

<div class="grid grid-cols-3 gap-4 justify-center bg-darkgray text-white">

  <div class="justify-center w-full col-span-2">
    <img
      class="object-contain h-screen w-full justify-center bg-black"
      src={photo.image}
      alt={photo.name}
    />
  </div>

  <div class="w-full justify-left tracking-widest">
    <h1 class="text-left mt-8 text-4xl">{photo.name.toUpperCase()}</h1>
    <h2 class="text-left mt-8 text-2xl ">TYPE</h2>
    <div class="flex flex-wrap" id="types">
    </div>
    <h2 class="text-left mt-8 text-2xl">SIZE</h2>
    <div class="flex flex-wrap" id="sizes">
    </div>
    <div class="inline-flex mt-16 w-full">
      <Modal show={$modal}>
        <div class="bg-green-600 text-white px-4 py-2 rounded mr-2 text-center cursor-pointer" id="addToCart" on:click={showModal}>ADD TO CART</div>
      </Modal>
      <div class="px-4 text-center text-2xl my-auto" id="price"></div>
    </div>
  </div>

</div>
