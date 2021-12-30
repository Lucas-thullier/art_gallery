import { createStore } from 'vuex'
import * as getters from '@store/getters'
import * as actions from '@store/actions'
import mutations from '@store/mutations'

const state = {
  paintings: {
    data: [],
    count: 0,
    paginator: {
      first: `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/all?page=1`,
      next: '',
      previous: '',
      last: `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/all?page=last`,
    },
    ListView: 'PaintingList',
    detailView: 'PaintingDetail',
  },
  creators: {
    data: [],
    count: 0,
    paginator: {
      first: `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/all?page=1`,
      next: '',
      previous: '',
      last: `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/all?page=last`,
    },
    ListView: 'CreatorList',
    detailView: 'CreatorDetail',
  },
}

export default createStore({
  state,
  getters,
  actions,
  mutations,
})
