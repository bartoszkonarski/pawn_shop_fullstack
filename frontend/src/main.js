import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routes from './routers'
import VueSession from 'vue-session'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import specific icons */
import { faBasketShopping } from '@fortawesome/free-solid-svg-icons'
import { faHexagonPlus } from '@fortawesome/free-solid-svg-icons'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* add icons to the library */
library.add(faBasketShopping)

// Przypał bo to nie działa jak dodaje się 2 różne

let a = faHexagonPlus;
let b = faBasketShopping;
console.log(a,b);

/* add font awesome icon component */

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

Vue.use(VueRouter);
Vue.use(VueSession);

const router = new VueRouter({
  routes: Routes
});

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router: router,
}).$mount('#app')
