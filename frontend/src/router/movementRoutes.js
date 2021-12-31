import MovementList from '@pages/MovementList.vue'
import MovementDetail from '@pages/MovementDetail.vue'

export default [
  {
    path: '/movement/all',
    component: MovementList,
    name: 'MovementList',
    props: true,
  },
  {
    path: '/movement/:id',
    component: MovementDetail,
    name: 'MovementDetail',
    props: true,
  },
]
