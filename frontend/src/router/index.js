import { createRouter, createWebHashHistory } from 'vue-router'
import PageNotFound from '@pages/PageNotFound.vue'
import paintingRoutes from '@router/paintingRoutes.js'
import creatorRoutes from '@router/creatorRoutes.js'
import movementRoutes from '@router/movementRoutes.js'
import depictionRoutes from '@router/depictionRoutes.js'
import materialRoutes from '@router/materialRoutes.js'

const routes = [
  { path: '/:pathMatch(.*)*', component: PageNotFound },
  ...paintingRoutes,
  ...creatorRoutes,
  ...movementRoutes,
  ...depictionRoutes,
  ...materialRoutes,
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
