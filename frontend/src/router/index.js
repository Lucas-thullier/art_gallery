import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Detail from '../pages/Detail.vue'
import PageNotFound from '../pages/PageNotFound.vue'

const routes = [
  { path: '/:pathMatch(.*)*', component: PageNotFound },
  { path: '/', component: Home },
  { path: '/painting/:id', component: Detail },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
