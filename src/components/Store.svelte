<script>

  import StoreListItem from "./StoreListItem.svelte";
  import allPrints from "../prints";
  import calendars from "../calendars";
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

  let type = queryparams.type ? queryparams.type : "print"
  let category = queryparams.category ? queryparams.category : "earth"

  let availableTypes = ["print","calendar"];
  let types = ["print","photobook","calendar"];
  if (!types.includes(type)) {
    window.location.href = '/#/unavailable';
  }

  let categories = ["earth","space","math"];
  if (!categories.includes(category) && type=="print") {
    window.location.href = '/#/unavailable';
  }

  addHistory();
  window.onhashchange = () => { addHistory() };
  history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));

  let prints = allPrints.filter(photo => photo.category == category);

  function selectCategory(e) {
    category = e.target.id;
    prints = allPrints.filter(photo => photo.category == category);
    window.location.href = `/#/store?type=print&category=${category}`
  }

  function selectType(e) {
    type = e.target.id;
    window.location.href = `/#/store?type=${type}`
  }
  
</script>

<div class="bg-darkgray h-screen">

  <div class="fixed inset-x-0 top-0 bg-darkgray w-screen h-10screen my-auto inline-flex">
    <a class="text-2xl pb-1 relative text-white bg-darkestgray font-bold my-auto ml-1 w-40px rounded text-center cursor-pointer" href="/">&#8249;</a>
    {#key category}
    <div on:click={selectType} id="photobook" class="relative w-1/3 my-auto mx-auto text-center text-white {type != "photobook" ? "opacity-25" : ""} tracking-widest text-sm lg:text-2xl cursor-pointer">PHOTOBOOKS</div>
    <div on:click={selectType} id="print" class="relative w-1/3 my-auto mx-auto text-center text-white {type != "print" ? "opacity-25" : ""} tracking-widest text-sm lg:text-2xl cursor-pointer">PRINTS</div>
    <div on:click={selectType} id="calendar" class="relative w-1/3 my-auto mx-auto text-center text-white {type != "calendar" ? "opacity-25" : ""} tracking-widest text-sm lg:text-2xl cursor-pointer">CALENDARS</div>
    {/key}
    <a class="relative right-0 text-white bg-darkestgray bg-opacity-75 font-bold py-1 my-auto mr-1 w-40px justify-center rounded text-center inline-flex cursor-pointer" href="#/cart">
      <div>&#128722;</div>
      <div>{cartItemCount}</div>
    </a>
  </div>

  <div class="fixed inset-x-0 top-10screen bg-darkergray w-screen h-7screen my-auto inline-flex {type != "print" ? "hidden" : ""}">
    {#key category}
    <div on:click={selectCategory} id="earth" class="relative w-1/3 my-auto mx-auto text-center text-white {category != "earth" ? "opacity-25" : ""} tracking-widest text-sm lg:text-xl cursor-pointer">EARTH</div>
    <div on:click={selectCategory} id="space" class="relative w-1/3 my-auto mx-auto text-center text-white {category != "space" ? "opacity-25" : ""} tracking-widest text-sm lg:text-xl cursor-pointer">SPACE</div>
    <div on:click={selectCategory} id="math" class="relative w-1/3 my-auto mx-auto text-center text-white {category != "math" ? "opacity-25" : ""} tracking-widest text-sm lg:text-xl cursor-pointer">MATH</div>
    {/key}
  </div>

  <div class="fixed inset-x-0 {type == "print" ? "top-17screen lg:h-83screen h-73screen" : "top-10screen lg:h-90screen h-80screen hidden"} bg-darkestgray w-full my-15 overflow-auto">
    <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkestgray">
      {#key category}
      {#each prints as print}
        <a href="#/store/print/{print.id}">
          <StoreListItem
            name={print.name}
            thumb={print.thumb}
          />
        </a>
      {/each}
      {/key}
    </div>
  </div>

  <div class="fixed inset-x-0 {type == "calendar" ? "top-10screen lg:h-90screen h-80screen" : "top-10screen lg:h-90screen h-80screen hidden"} bg-darkestgray w-full my-15 overflow-auto">
    <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkestgray">
      {#key category}
      {#each calendars as calendar}
        <a href="#/store/calendar/{calendar.id}">
          <StoreListItem
            name={calendar.name}
            thumb={calendar.thumb}
          />
        </a>
      {/each}
      {/key}
    </div>
  </div>

  <div class="flex fixed inset-x-0 {!availableTypes.includes(type) ? "top-10screen lg:h-90screen h-80screen" : "top-17screen lg:h-83screen h-73screen hidden"} bg-darkestgray w-full my-15 overflow-auto">
    <div class="m-auto text-xl text-white">
      Coming Soon!
    </div>
  </div>

</div>