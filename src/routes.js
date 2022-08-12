
// import FundamentalBeliefs from './components/FundamentalBeliefs.svelte'
// import ForMen from './components/ForMen.svelte'
// import Home from './components/Home.svelte'
import About from './components/About.svelte'
import AllArticles from './components/AllArticles.svelte'
import Article from './components/Article.svelte'
import Devotional from './components/Devotional.svelte'

const routes = {
    // '/betterLiving/': BetterLiving,
    // '/forMen/': ForMen,
    // '/fundamentalBeliefs': FundamentalBeliefs,
    '/': About,
    '/allArticles': AllArticles,
    '/Article/:id': Article,
    '/Devotional/': Devotional
};

export default routes;
