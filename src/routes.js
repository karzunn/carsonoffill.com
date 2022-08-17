import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import ItemList from './components/ItemList.svelte'
import Item from './components/Item.svelte'

const routes = {
    '/': Home,
    '/items': ItemList,
    '/items/:id': Item,
    '/cart': Cart
};

export default routes;
