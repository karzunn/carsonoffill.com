<script>

  import ListItem from "./ListItem.svelte";
  import Photos from "../photos";
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
    cartItemCount = Items.length.toString();
  });
  
</script>

<div class="absolute bottom-0 right-0 text-white bg-gray font-bold py-1 px-2 m-1 rounded text-center inline-flex">
  <div>&#128722;</div>
  <div>{cartItemCount}</div>
</div>

<div class="flex justify-center py-16 bg-darkgray h-screen">
  <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10 bg-darkgray">
    {#each Photos as Photo}
      <a href="#/items/{Photo.type}/{Photo.id}">
        <ListItem
          name={Photo.name}
          thumb={Photo.thumb}
        />
      </a>
    {/each}
  </div>
</div>
