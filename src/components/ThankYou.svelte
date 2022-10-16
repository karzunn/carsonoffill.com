<script>
    import { cartItems } from "../stores";

    cartItems.update(cartItems=>{return {}});
</script>

<div class="bg-main bg-cover bg-no-repeat bg-center h-screen flex">
    <div class="text-white my-auto mx-10screen font-extralight w-screen">
        <div class="w-full block text-center text-4xl my-10screen mx-auto">ORDER RECEIVED</div>
        <div class="w-full block text-center text-2xl my-10screen mx-auto">Thank you for your order! A confirmation email should be sent shortly. <br> As soon as your order ships, you will receive a tracking number as well.</div>
        <div class="w-full block text-center text-xl my-10screen mx-auto">Thanks again! -Carson O'Ffill</div>
    </div>
</div>

<a class="text-2xl pb-1 px-10px m-2 absolute top-0 left-0 text-white bg-gray bg-opacity-75 font-bold rounded text-center cursor-pointer" href="/">&#8249;</a>