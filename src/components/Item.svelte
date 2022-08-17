<script>
  import articles from "../items";
  export let params = {};
  let article = articles.filter(d=>d.id == params.id)[0]
  if (!article)
  {
    window.history.go(-1);
    window.location.reload();
  }
  window.scrollTo(0,0); 
</script>

<div class="sm:mx-16 sm:py-16">
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
