import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import ItemList from './components/ItemList.svelte'
import PhotoItem from './components/PhotoItem.svelte'

const routes = {
    '/': Home,
    '/items': ItemList,
    '/items/photos/:id': PhotoItem,
    '/cart': Cart
};

export default routes;
