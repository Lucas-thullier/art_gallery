import PaintingList from '@pages/PaintingList.vue'
import PaintingDetail from '@pages/PaintingDetail.vue'

export default [
  {
    path: '/painting/all',
    component: PaintingList,
    name: 'PaintingList',
    props: true,
  },
  {
    path: '/painting/:id',
    component: PaintingDetail,
    name: 'PaintingDetail',
    props: true,
  },
]
