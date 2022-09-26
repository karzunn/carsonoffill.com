<script>

  import PrintListItem from "./PrintListItem.svelte";
  import allPrints from "../prints";
  import {querystring} from 'svelte-spa-router';
  import { cartItems } from "../stores";
  import { history } from "../stores";
  import { addHistory } from "../functions";

  let cartItemCount = 0;

  cartItems.subscribe(Items => {
    cartItemCount = 0
    Object.keys(Items).map(key => cartItemCount += Items[key].quantity)
	});

  let queryparams = {};
  let vars = $querystring.split('&');
  for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split('=');
      queryparams[pair[0]] = pair[1];
  }

  let category = queryparams.category
  let categories = ["earth","space","math"];
  if (!categories.includes(category)) {
    window.location.href = '/#/unavailable';
  }

  addHistory();
  window.onhashchange = () => { addHistory() };
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  let photos = allPrints.filter(photo => photo.category == category);

  function selectCategory(e) {
    category = e.target.id;
    photos = allPrints.filter(photo => photo.category == category);
    window.location.href = `/#/store/prints?category=${category}`
  }
  
</script>

<div class="bg-darkgray h-screen">

  <div class="fixed inset-x-0 top-0 bg-darkgray w-screen h-10screen my-auto inline-flex">
    <a class="text-2xl pb-1 px-10px relative text-white bg-darkestgray font-bold my-auto ml-1 rounded text-center cursor-pointer" href="/#/store/types">&#8249;</a>
    {#key category}
    <div on:click={selectCategory} id="earth" class="relative my-auto mx-auto text-center text-white {category != "earth" ? "opacity-25" : ""} tracking-widest text-xl lg:text-2xl cursor-pointer">EARTH</div>
    <div on:click={selectCategory} id="space" class="relative my-auto mx-auto text-center text-white {category != "space" ? "opacity-25" : ""} tracking-widest text-xl lg:text-2xl cursor-pointer">SPACE</div>
    <div on:click={selectCategory} id="math" class="relative my-auto mx-auto text-center text-white {category != "math" ? "opacity-25" : ""} tracking-widest text-xl lg:text-2xl cursor-pointer">MATH</div>
    {/key}
    <div class="text-2xl pb-1 px-10px relative my-auto ml-1 invisible">&#8249;</div>
    <a class="relative right-0 text-white bg-darkestgray bg-opacity-75 font-bold py-1 px-2 my-auto mr-1 rounded text-center inline-flex cursor-pointer" href="#/store/cart">
      <div>&#128722;</div>
      <div>{cartItemCount}</div>
    </a>
  </div>

  <div class="fixed inset-x-0 top-10screen bg-darkestgray w-full lg:h-90screen h-80screen my-15 overflow-auto">
    <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkestgray">
      {#key category}
      {#each photos as photo}
        <a href="#/store/prints/{photo.id}">
          <PrintListItem
            name={photo.name}
            thumb={photo.thumb}
          />
        </a>
      {/each}
      {/key}
    </div>
  </div>

</div>