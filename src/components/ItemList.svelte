<script>

  import ListItem from "./ListItem.svelte";
  import Items from "../items";
  import {querystring} from 'svelte-spa-router';

  let queryparams = {};
  let vars = $querystring.split('&');
  for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split('=');
      queryparams[pair[0]] = pair[1];
  }
  
</script>

<div class=" flex  justify-center py-16">
  <div class=" grid  lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10">
    {#each Items as item}
      <a href="#/items/{item.id}">
        <ListItem
          name={item.name}
          thumb={item.thumb}
        />
      </a>
    {/each}
  </div>
</div>
