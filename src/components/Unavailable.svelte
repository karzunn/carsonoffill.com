<script>
    import { history } from "../stores";
    import { goBack, addHistory } from '../functions';

    addHistory();
    history.subscribe(history => localStorage.setItem("history", JSON.stringify(history)));
</script>

<div class="bg-main bg-cover bg-no-repeat bg-center h-screen flex">
    <div class="text-white m-auto">
        <div class="w-full block text-center text-4xl">Unavailable</div>
    </div>
</div>

<div class="text-2xl pb-1 px-10px m-2 absolute top-0 left-0 text-white bg-gray bg-opacity-67 font-bold rounded text-center cursor-pointer" on:click={goBack}>&#8249;</div>