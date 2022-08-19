<script>
  export let thumb = "";
  export let name = "";
</script>

<div class="group transform transition duration-500 ease-in-out hover:scale-105 w-80 sm:w-72 md:w-80 bg-white shadow-2xl rounded-lg tracking-wide">
    <div class="flex-shrink-0">
      <img
        src={thumb}
        alt={name}
        class="object-cover w-full group-hover:opacity-75 h-48 rounded-lg rounded-b-none"
      />
    </div>
    <div class="px-4 py-2 mt-2">
      <div class=" h-8">
        <h2 class="text-lg text-gray-800 text-center tracking-normal">
          {name}
        </h2>
    </div>
  </div>
</div>
