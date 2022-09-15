<script>
	import { Modal, bind } from 'svelte-simple-modal';
  import AddToCartModal from './AddToCartModal.svelte';
  import { onMount } from 'svelte';
  import prints from "../prints";
  import prices from "../prices";
  import { cartItems, history } from "../stores";
  import { writable } from 'svelte/store';
  import { goBack } from '../functions';
  export const modal = writable(null);
  export let params = {};

  window.scrollTo(0, 0);

  let print = prints.filter(d=>d.id == params.id)[0]
  if (!print) {
    print = prints[0];
    window.location.href = '/#/unavailable';
  }
  history.update(history => history.concat(window.location.hash));

  const showModal = () => modal.set(bind(AddToCartModal, { item: print }));

  function calcPrice(){
    let selectedType = document.getElementsByClassName('selected type')[0].id;
    let selectedSize = document.getElementsByClassName('selected size')[0].id;
    let price = prices[print.type][selectedType].sizes[selectedSize];
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
    let types = Object.keys(print.sizes);
    for (let type of types){
      let typeElement = document.createElement("div");
      typeElement.className = "lg:text-base text-xs bg-brand text-white py-2 px-4 rounded my-4 lg:mr-4 mx-2 type opacity-25 cursor-pointer";
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
    let sizes = print.sizes[selectedType];
    for (let size of sizes){
      let sizeElement = document.createElement("div");
      sizeElement.className = "lg:text-base text-xs bg-brand text-white py-2 px-4 rounded my-4 lg:mr-4 mx-2 text-center size opacity-25 cursor-pointer";
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

<div class="w-screen h-screen bg-darkgray">

  <div class="fixed text-2xl pb-1 px-10px m-2 top-0 left-0 text-white bg-gray bg-opacity-75 font-bold rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>
  <a class="fixed bottom-0 right-0 text-white bg-gray font-bold py-1 px-2 m-1 rounded text-center inline-flex cursor-pointer" href="#/store/cart">
    <div>&#128722;</div>
    <div>{cartItemCount}</div>
  </a>

  <div class="grid lg:grid-cols-3 grid-cols-1 gap-4 justify-center bg-darkgray text-white">

    <div class="justify-center w-full col-span-1 lg:col-span-2">
      <img
        class="object-contain lg:h-screen h-40screen w-full justify-center bg-black"
        src={print.image}
        alt={print.name}
      />
    </div>

    <div class="w-full tracking-widest lg:h-screen">
      <h1 class="lg:text-left lg:mt-8 text-center lg:text-4xl text-xl">{print.name.toUpperCase()}</h1>
      <h2 class="lg:text-left lg:mt-8 text-center mt-2 lg:text-2xl text-xs">TYPE</h2>
      <div class="flex flex-wrap w-full lg:w-fit justify-center lg:justify-start" id="types">
      </div>
      <h2 class="lg:text-left lg:mt-8 text-center lg:text-2xl text-xs">SIZE</h2>
      <div class="flex flex-wrap w-full lg:w-fit justify-center lg:justify-start" id="sizes">
      </div>
      <div class="inline-flex mt-2 mb-4 lg:mt-16 w-full justify-center lg:justify-start">
        <Modal show={$modal}>
          <div class="bg-accent text-white font-semibold px-4 py-2 rounded mr-2 text-center cursor-pointer lg:text-base text-sm" id="addToCart" on:click={showModal}>ADD TO CART</div>
        </Modal>
        <div class="px-4 text-center lg:text-2xl text-base my-auto" id="price"></div>
      </div>
    </div>

  </div>

</div>
