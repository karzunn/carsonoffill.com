<script>
  import { onMount } from "svelte";
  //this comes from svelte-spa-router
  //gives the current id of the article
  //"id" is also what we named the variable path in routes.js
  // export let params = {};

  let loaded = false;
  let devotional = [];
  let currentDate;
  let devotionalId;
  let devotionalName = "InHisSteps";

  function daysIntoYear(date) {
    return (
      (Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()) -
        Date.UTC(date.getFullYear(), 0, 0)) /
      24 /
      60 /
      60 /
      1000
    );
  }
  
  onMount(async () => {
    currentDate = daysIntoYear(new Date());
    devotionalId = devotionalName.concat(currentDate);
    const res = await fetch(
      `https://hgv1budnn8.execute-api.us-east-1.amazonaws.com/category/book/${devotionalId}`
    );
    devotional = await res.json();
    loaded = true
  });
</script>

<!-- <div class="sm:mx-16 sm:py-16">
  <div class=" flex justify-center ">
    <span>{devotional.date}</span>
    <img
      class="object-cover w-full h-48 sm:w-11/12 lg:h-96 lg:w-4/5"
      src={article.image}
      alt={article.imgDescription}
    />
  </div>
  <div class="grid justify-items-center">
    <span class=" text-center mt-8 font-bold text-4xl ">{devotional.title}</span
    >
    <div class=" mt-3 flex text-blue-500 text-sm">
      <span>by Richard W. O'Ffill</span>
      <a class="mx-4" href={article.categoryLink}>{article.category}</a>
      <span>{devotional.date}</span>
    </div>
    <p class="w-11/12 font-normal text-base  lg:w-3/4">
      {@html devotional.text}
    </p>
  </div>
</div> -->

<div
  class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12"
  style="background-image: url('https://picsum.photos/id/1018/1000')"
>
  <div class="relative p-10 lg:w-2/3 sm:mx-auto">
    <div
      class="relative px-4  bg-white shadow-lg sm:rounded-3xl sm:px-14 sm:py-10 bg-clip-padding bg-opacity-60 border border-gray-200"
      style="backdrop-filter: blur(20px);"
    >
      <div class="mx-auto" style="display: {loaded ? "block" : "none"}">
        <div class="flex justify-between items-end">
          <span class=" text-center font-bold text-4xl "
            >{devotional.title}</span
          >
          <span>{devotional.date}</span>
        </div>

        <div>
          <span class=" text-base font-normal "
            >Based On: {devotional.basedOn}</span
          >
        </div>
        <p class="my-4 text-base font-normal ">
          "{devotional.verseText}" ({devotional.verse})
        </p>

        <p class=" text-base font-normal ">
          {devotional.text}
        </p>
      </div>
    </div>
  </div>
</div>
