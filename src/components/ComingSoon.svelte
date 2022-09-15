<script>
    import { history } from "../stores";
    import { goBack } from '../functions';

    history.update(history => history.concat(window.location.hash));
</script>

<div class="bg-main bg-cover bg-no-repeat bg-center h-screen flex">
    <div class="text-white m-auto">
        <div class="w-full block text-center text-4xl">Coming Soon!</div>
    </div>
</div>

<div class="text-2xl pb-1 px-10px m-2 absolute top-0 left-0 text-white bg-gray bg-opacity-67 font-bold rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>