<script>
  export let thumb = "";
  export let name = "";
</script>

<div class="group transform transition duration-500 ease-in-out hover:scale-105 w-80 sm:w-72 md:w-80 bg-white shadow-2xl tracking-wide mx-auto my-3">
  <img
    src={thumb}
    alt={name}
    class="object-cover w-full group-hover:opacity-75 h-48"
  />
  <div class="absolute bottom-0 left-0 right-0 px-4 py-2 bg-darkgray bg-opacity-75">
    <h1 class="text-white">
      {name}
    </h1>
  </div>
</div>
