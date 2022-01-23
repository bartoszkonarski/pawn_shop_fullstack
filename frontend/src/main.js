import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routes from './routers'
import VueSession from 'vue-session'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


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
