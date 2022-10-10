<script>
	import { Modal, bind } from 'svelte-simple-modal';
  import AddToCartModal from './AddToCartModal.svelte';
  import { onMount } from 'svelte';
  import prints from "../prints";
  import prices from "../prices";
  import { cartItems, history } from "../stores";
  import { writable } from 'svelte/store';
  import { goBack, addHistory } from '../functions';
  export const modal = writable(null);
  export let params = {};

  function updateCrop() {
    let body = document.getElementById("body");
    let imageContainer = document.getElementById("imageContainer");
    let topCrop = document.getElementById("topCrop");
    let bottomCrop = document.getElementById("bottomCrop");
    let leftCrop = document.getElementById("leftCrop");
    let rightCrop = document.getElementById("rightCrop");
    let imageWidth;
    let imageHeight;
    let screenLandscape = imageContainer.offsetHeight == body.offsetHeight;
    let imageAspectRatio = imageContainer.naturalWidth / imageContainer.naturalHeight;
    let containerAspectRatio = imageContainer.offsetWidth / imageContainer.offsetHeight;
    let goalHeight = Number(selectedPrintSize.split("x")[1]);
    let goalWidth = Number(selectedPrintSize.split("x")[0]);

    if (imageAspectRatio > containerAspectRatio) {
      imageHeight = imageContainer.offsetWidth / imageAspectRatio;
      imageWidth = imageContainer.offsetWidth;
    }
    else {
      imageHeight = imageContainer.offsetHeight;
      imageWidth = imageContainer.offsetHeight * imageAspectRatio;
    }

    let verticalOffset = (imageContainer.offsetHeight - imageHeight) / 2;
    let horizontalOffset = (imageContainer.offsetWidth - imageWidth) / 2;

    let verticalRemove = (imageHeight - (goalHeight * imageWidth) / goalWidth) / 2;
    verticalRemove = verticalRemove < 0 ? 0 : (verticalRemove + verticalOffset);
    let horizontalRemove = (imageWidth - (imageHeight*goalWidth) / goalHeight) / 2;
    horizontalRemove = horizontalRemove < 0 ? 0 : (horizontalRemove + horizontalOffset);

    if (screenLandscape) {
      bottomCrop.style.bottom = `0px`;
    }
    else {
      bottomCrop.style.top = `${imageContainer.offsetHeight-verticalRemove}px`;
    }
    bottomCrop.style.height = `${verticalRemove}px`;
    bottomCrop.style.width = `${imageContainer.offsetWidth}px`;

    topCrop.style.top = `0px`;
    topCrop.style.height = `${verticalRemove}px`;
    topCrop.style.width = `${imageContainer.offsetWidth}px`;

    leftCrop.style.top = `0px`;
    leftCrop.style.left = `0px`;
    leftCrop.style.height = `${imageContainer.offsetHeight}px`;
    leftCrop.style.width = `${horizontalRemove}px`;

    rightCrop.style.top = `0px`;
    rightCrop.style.right = `${screenLandscape ? (body.offsetWidth - imageContainer.offsetWidth) : 0}px`;
    rightCrop.style.height = `${imageContainer.offsetHeight}px`;
    rightCrop.style.width = `${horizontalRemove}px`;
  }

  window.scrollTo(0, 0);

  let print = prints.filter(d=>d.id == params.id)[0]
  if (!print) {
    print = prints[0];
    window.location.href = '/#/unavailable';
  }
  addHistory();
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  const showModal = () => modal.set(bind(AddToCartModal, { item: print }));

  function calcPrice(){
    let priceDisplay = document.getElementById('price');
    let selectedType = document.getElementsByClassName('selected type')[0].id;
    let selectedSize = document.getElementsByClassName('selected size')[0].id;
    let price = prices[print.type][selectedType].sizes[selectedSize];
    priceDisplay.innerHTML = "$" + price.toString();
  }

  function selectType(e){
    let addToCartButton = document.getElementById('addToCart');
    let priceDisplay = document.getElementById('price');
    let selectSizeMessage = document.getElementById('selectSizeMessage');
    let topCrop = document.getElementById("topCrop");
    let bottomCrop = document.getElementById("bottomCrop");
    let leftCrop = document.getElementById("leftCrop");
    let rightCrop = document.getElementById("rightCrop");
    let types = document.querySelectorAll('.type');
    for (let i=0;i<types.length;i++){
      types[i].classList.remove("selected"); types[i].classList.add("opacity-25");
    };
    let selected = e ? e.target : types[0];
    selected.classList.add("selected"); selected.classList.remove("opacity-25");
    if (e)
    {
      generateSizes();
    }
    addToCartButton.style.display = "none";
    priceDisplay.style.display = "none";
    selectSizeMessage.style.display = "block";
    topCrop.style.height = "0px";
    bottomCrop.style.height = "0px";
    leftCrop.style.height = "0px";
    rightCrop.style.height = "0px";
  }

  let selectedPrintSize = false;

  function selectSize(e){
    let addToCartButton = document.getElementById('addToCart');
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
    selectSizeMessage.style.display = "none";
    calcPrice();
    updateCrop();
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
    let sizesContainer = document.getElementById("sizes");
    let selectedType = document.getElementsByClassName('selected type')[0].id;
    sizesContainer.innerHTML = "";
    let sizes = print.sizes[selectedType];
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
    generateTypes();
    selectType();
    generateSizes();
    window.addEventListener('resize', updateCrop);
	});
</script>

<div id="body" class="w-screen h-screen bg-darkgray">

  <div class="grid lg:grid-cols-3 grid-cols-1 gap-4 justify-center bg-darkgray text-white">

    <div class="justify-center w-full col-span-1 lg:col-span-2">
      <img
        class="object-contain lg:h-screen h-40screen w-full justify-center bg-black"
        src={print.image}
        alt={print.name}
        id="imageContainer"
      />
      <div class="absolute bg-black bg-opacity-75" id="topCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="bottomCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="leftCrop"></div>
      <div class="absolute bg-black bg-opacity-75" id="rightCrop"></div>
    </div>

    <a class="fixed top-0 right-0 text-white bg-gray font-bold py-1 px-2 m-2 rounded text-center inline-flex cursor-pointer" href="#/cart">
      <div>&#128722;</div>
      <div>{cartItemCount}</div>
    </a>

    <div class="fixed text-2xl pb-1 px-10px m-2 top-0 left-0 text-white bg-gray bg-opacity-75 font-bold rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>

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
          <div class="bg-accent text-white font-semibold px-4 py-2 rounded mr-2 text-center cursor-pointer lg:text-base text-sm" style="display: none;" id="addToCart" on:click={showModal}>ADD TO CART</div>
        </Modal>
        <div class="px-4 text-center lg:text-2xl text-base my-auto" style="display: none;" id="price"></div>
        <div class="px-4 text-center lg:text-2xl text-base my-auto" id="selectSizeMessage">Please select a size</div>
      </div>
    </div>

  </div>

</div>
