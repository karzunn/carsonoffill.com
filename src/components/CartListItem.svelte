<script>
  import { cartItems } from "../stores";
  export let description = "";
  export let price = "";
  export let photo = {};
  
</script>

<div class="grid grid-cols-4 gap-5 m-3">
  <img
    src={photo.thumb}
    alt={photo.name}
    class="object-contain h-20screen"
  />
  <h1 class="text-white text-center">
    {description}
  </h1>
  <h1 class="text-white text-center">
    {price}
  </h1>
  <h1 class="text-white text-center">
    {`Q`}
  </h1>
</div>
