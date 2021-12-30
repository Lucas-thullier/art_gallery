import { createRouter, createWebHashHistory } from 'vue-router'
import CreatorDetail from '@pages/CreatorDetail.vue'
import PaintingDetail from '@pages/PaintingDetail.vue'
import PaintingList from '@pages/PaintingList.vue'
import CreatorList from '@pages/CreatorList.vue'
import PageNotFound from '@pages/PageNotFound.vue'

const routes = [
  { path: '/:pathMatch(.*)*', component: PageNotFound },
  {
    path: '/painting/all',
    component: PaintingList,
    name: 'PaintingList',
    props: true,
  },
  {
    path: '/creator/all',
    component: CreatorList,
    name: 'CreatorList',
    props: true,
  },
  {
    path: '/painting/:id',
    component: PaintingDetail,
    name: 'PaintingDetail',
    props: true,
  },
  {
    path: '/creator/:id',
    component: CreatorDetail,
    name: 'CreatorDetail',
    props: true,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
