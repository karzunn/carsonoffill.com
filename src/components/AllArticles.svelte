<script>
  import ArticleCard from "./ArticleCard.svelte";
  import { onMount } from "svelte";

  let articles = [];
  onMount(async () => {
    const res = await fetch(
      "https://hgv1budnn8.execute-api.us-east-1.amazonaws.com/category/article"
    );
    let data = await res.json();
    articles = data.items;
  });
</script>

<div class=" flex  justify-center py-16">
  <div class=" grid  lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10">
    {#each articles as item}
      <a href="#/Article/{item.id}">
        <ArticleCard
          title={item.title}
          text={item.previewText}
          image={item.image}
          imgDescription={item.imgDescription}
          category={item.category}
          date={item.date}
        />
      </a>
    {/each}
  </div>
</div>
