import addItem from './components/content/addItem.vue'
import listItem from './components/content/listItem.vue'
import summary from './components/content/summary.vue'
import login from './components/content/login.vue'

export default [
    {path:'/', component: listItem},
    {path:'/add', component: addItem},
    {path:'/log', component: login},
    {path:'/summary', component: summary},
]