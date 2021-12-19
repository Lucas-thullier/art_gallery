import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Detail from '../pages/Detail.vue'
// import About from '../pages/About.vue'

const routes = [
  { path: '/', component: Home },
  // { path: '/painting/:id', component: About },
  { path: '/painting/:id', component: Detail },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
