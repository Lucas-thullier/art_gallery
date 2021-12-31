import CreatorList from '@pages/CreatorList.vue'
import CreatorDetail from '@pages/CreatorDetail.vue'

export default [
  {
    path: '/creator/all',
    component: CreatorList,
    name: 'CreatorList',
    props: true,
  },
  {
    path: '/creator/:id',
    component: CreatorDetail,
    name: 'CreatorDetail',
    props: true,
  },
]
