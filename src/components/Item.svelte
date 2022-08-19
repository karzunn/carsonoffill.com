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

<div class="grid grid-cols-2 gap-4 justify-center">

  <div class="justify-left">
    <img
      class="object-contain m-4 h-90vh"
      src={article.image}
      alt={article.name}
    />
  </div>

  <div>
    <h1 class="text-center mt-8 font-bold text-4xl">{article.name}</h1>
  </div>

</div>
