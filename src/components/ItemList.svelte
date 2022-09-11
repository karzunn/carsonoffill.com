<script>

  import ListItem from "./ListItem.svelte";
  import allPhotos from "../photos";
  import {querystring} from 'svelte-spa-router';
  import { cartItems } from "../stores";

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
    window.history.go(-1);
    window.location.reload();
  }

  let photos = allPhotos.filter(photo => photo.category == category);
  
</script>

<div class="fixed inset-x-0 top-0 bg-darkgray w-screen h-10screen my-auto inline-flex">
  <a class="relative text-white bg-darkestgray font-bold py-1screen px-2 my-auto ml-1 rounded text-center cursor-pointer" href="/#/store/printcategories">&#129128;</a>
  <h1 class="relative my-auto mx-auto text-center text-white tracking-widest text-2xl">{category.toUpperCase()}</h1>
</div>

<div class="fixed inset-x-0 top-10screen bg-darkestgray w-full h-90screen my-15 overflow-auto">
  <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkestgray">
    {#each photos as photo}
      <a href="#/store/items/{photo.type}/{photo.id}">
        <ListItem
          name={photo.name}
          thumb={photo.thumb}
        />
      </a>
    {/each}
  </div>
</div>

<a class="absolute bottom-0 right-0 text-white bg-darkestgray bg-opacity-75 font-bold py-1 px-2 m-1 rounded text-center inline-flex cursor-pointer" href="#/store/cart">
  <div>&#128722;</div>
  <div>{cartItemCount}</div>
</a>
