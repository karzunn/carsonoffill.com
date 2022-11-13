import Cart from './components/Cart.svelte'
import Home from './components/Home.svelte'
import Store from './components/Store.svelte'
import PrintItem from './components/PrintItem.svelte'
import CalendarItem from './components/CalendarItem.svelte'
import Unavailable from './components/Unavailable.svelte'
import ThankYou from './components/ThankYou.svelte'

const routes = {
    '/': Home,
    '/cart': Cart,
    '/store': Store,
    '/store/print/:id': PrintItem,
    '/store/calendar/:id': CalendarItem,
    '/unavailable': Unavailable,
    '/thankyou': ThankYou
};

export default routes;
