import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import PrintList from './components/PrintList.svelte'
import PrintItem from './components/PrintItem.svelte'
import Types from './components/Types.svelte'
import ComingSoon from './components/ComingSoon.svelte'
import Unavailable from './components/Unavailable.svelte'

const routes = {
    '/': Home,
    '/store/types': Types,
    '/store/prints': PrintList,
    '/store/prints/:id': PrintItem,
    '/store/cart': Cart,
    '/comingsoon': ComingSoon,
    '/unavailable': Unavailable
};

export default routes;
