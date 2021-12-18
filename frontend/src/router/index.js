import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/painting/:id', component: About },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
