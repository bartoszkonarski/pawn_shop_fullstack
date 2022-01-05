import addItem from './components/content/addItem.vue'
import listItem from './components/content/listItem.vue'

export default [
    {path:'/', component: listItem},
    {path:'/add', component: addItem},
]