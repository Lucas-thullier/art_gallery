import DepictionList from '@pages/DepictionList.vue'
import DepictionDetail from '@pages/DepictionDetail.vue'

export default [
  {
    path: '/depiction/all',
    component: DepictionList,
    name: 'DepictionList',
    props: true,
  },
  {
    path: '/depiction/:id',
    component: DepictionDetail,
    name: 'DepictionDetail',
    props: true,
  },
]
