<script>

  import ListItem from "./ListItem.svelte";
  import photos from "../photos";
  import {querystring} from 'svelte-spa-router';
  import { cartItems } from "../stores";

  let queryparams = {};
  let vars = $querystring.split('&');
  for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split('=');
      queryparams[pair[0]] = pair[1];
  }

  let cartItemCount = 0;

  cartItems.subscribe(Items => {
    console.log(Items)
    cartItemCount = 0
    Object.keys(Items).map(key => cartItemCount += Items[key].quantity)
	});  
  
</script>

<div class="fixed inset-x-0 top-0 bg-darkgray w-screen h-10screen my-auto inline-flex">
  <div class="absolute bg-darkgray grid grid-cols-3 gap-0 h-10screen w-screen left-0">
    <div class="m-auto h-10screen text-center text-white tracking-widest text-xl w-30screen">PRINTS</div>
    <div class="m-auto text-center text-white tracking-widest text-xl w-30screen">PHOTO BOOKS</div>
    <div class="m-auto text-center text-white tracking-widest text-xl w-30screen">CALENDARS</div>
  </div>
  <a class="relative text-white bg-darkestgray font-bold py-1screen px-2 my-auto ml-1 rounded text-center cursor-pointer" href="/">&#129128;</a>
</div>

<div class="fixed inset-x-0 top-10screen bg-darkestgray w-full h-80screen my-15 overflow-auto">
  <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkestgray">
    {#each photos as photo}
      <a href="#/items/{photo.type}/{photo.id}">
        <ListItem
          name={photo.name}
          thumb={photo.thumb}
        />
      </a>
    {/each}
  </div>
</div>

<div class="fixed inset-x-0 bottom-0 bg-darkgray grid grid-cols-2 gap-5 h-10screen">

</div>

<a class="absolute bottom-0 right-0 text-white bg-darkestgray font-bold py-1 px-2 m-1 rounded text-center inline-flex cursor-pointer" href="#/cart">
  <div>&#128722;</div>
  <div>{cartItemCount}</div>
</a>
