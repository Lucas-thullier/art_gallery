import MaterialList from '@pages/MaterialList.vue'
import MaterialDetail from '@pages/MaterialDetail.vue'

export default [
  {
    path: '/material/all',
    component: MaterialList,
    name: 'MaterialList',
    props: true,
  },
  {
    path: '/material/:id',
    component: MaterialDetail,
    name: 'MaterialDetail',
    props: true,
  },
]
