import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import Store from './components/Store.svelte'
import PrintItem from './components/PrintItem.svelte'
import Unavailable from './components/Unavailable.svelte'

const routes = {
    '/': Home,
    '/cart': Cart,
    '/store': Store,
    '/store/:id': PrintItem,
    '/unavailable': Unavailable
};

export default routes;
