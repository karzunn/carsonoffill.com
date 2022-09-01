import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import ItemList from './components/ItemList.svelte'
import PhotoItem from './components/PhotoItem.svelte'
import Types from './components/Types.svelte'
import PrintCategories from './components/PrintCategories.svelte'

const routes = {
    '/': Home,
    '/store/items': ItemList,
    '/store/items/photos/:id': PhotoItem,
    '/store/cart': Cart,
    '/store/types': Types,
    '/store/printcategories': PrintCategories
};

export default routes;
