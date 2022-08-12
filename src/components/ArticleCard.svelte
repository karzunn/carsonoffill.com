<script>
  export let title = "My Amazing Journey to the Mountains";
  export let text = `Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora
        reiciendis ad architecto at aut placeat quia, minus dolor praesentium
        officia maxime deserunt porro amet ab debitis deleniti modi soluta
        similique. Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora
        reiciendis ad architecto at aut placeat quia, minus dolor praesentium
        officia maxime deserunt porro amet ab debitis deleniti modi soluta
        similique. Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora
        reiciendis ad architecto at aut placeat quia, minus dolor praesentium
        officia maxime deserunt porro amet ab debitis deleniti modi soluta
        similique.`;
  export let image = "https://ik.imagekit.io/q5edmtudmz/post1_fOFO9VDzENE.jpg";
  export let imgDescription = "mountains";
  export let category = "Nature";
  export let categoryLink = "/";
  export let date = "September 9, 2021";
</script>

<div
  class="group transform transition duration-500 ease-in-out hover:scale-105 w-80 sm:w-72 md:w-80 bg-white shadow-2xl rounded-lg tracking-wide"
>
  <div class="flex-shrink-0">
    <img
      src={image}
      alt={imgDescription}
      class="object-cover w-full group-hover:opacity-75 h-48 rounded-lg rounded-b-none"
    />
  </div>
  <div class="px-4 py-2 mt-2">
    <div class=" h-8">
      <h2 class="text-xl text-gray-800 tracking-normal">
        {title}
      </h2>
      <div class="flex items-center justify text-blue-500 text-xs">
        <a href={categoryLink}>{category}</a>
        <span class="mx-2">{date}</span>
      </div>
    </div>
    <div class=" h-14 font-normal my-4 text-sm text-gray-600 mr-1">
      <p class="h-full overflow-ellipses overflow-hidden">
        {text}
      </p>
    </div>
  </div>
</div>
