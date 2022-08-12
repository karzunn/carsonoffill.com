<script>
  import { onMount } from "svelte";
  //this comes from svelte-spa-router
  //gives the current id of the article
  //"id" is also what we named the variable path in routes.js
  export let params = {};

  let loaded = false;
  let article = [];
  onMount(async () => {
    const res = await fetch(
      `https://hgv1budnn8.execute-api.us-east-1.amazonaws.com/category/article/${params.id}`
    );
    article = await res.json();
    loaded = true;
  });
</script>

<div class="sm:mx-16 sm:py-16" style="display: {loaded ? "block" : "none"}">
  <div class=" flex justify-center ">
    <img
      class="object-cover w-full h-48 sm:w-11/12 lg:h-96 lg:w-4/5"
      src={article.image}
      alt={article.imgDescription}
    />
  </div>
  <div class="grid justify-items-center">
    <span class=" text-center mt-8 font-bold text-4xl ">{article.title}</span>
    <div class=" mt-3 flex text-blue-500 text-sm">
      <span>by Richard W. O'Ffill</span>
      <a class="mx-4" href={article.categoryLink}>{article.category}</a>
      <span>{article.date}</span>
    </div>
    <p class="w-11/12 font-normal text-base  lg:w-4/5">
      {@html article.text}
    </p>
  </div>
</div>
