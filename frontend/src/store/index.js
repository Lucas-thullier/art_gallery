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
  materials: {
    data: [],
    count: 0,
    paginator: {
      first: `${import.meta.env.VITE_APP_BACKEND_URL}/api/materials/all?page=1`,
      next: '',
      previous: '',
      last: `${import.meta.env.VITE_APP_BACKEND_URL}/api/materials/all?page=last`,
    },
    ListView: 'MaterialList',
    detailView: 'MaterialDetail',
  },
  depicts: {
    data: [],
    count: 0,
    paginator: {
      first: `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/all?page=1`,
      next: '',
      previous: '',
      last: `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/all?page=last`,
    },
    ListView: 'DepictionList',
    detailView: 'DepictionDetail',
  },
  movements: {
    data: [],
    count: 0,
    paginator: {
      first: `${import.meta.env.VITE_APP_BACKEND_URL}/api/movement/all?page=1`,
      next: '',
      previous: '',
      last: `${import.meta.env.VITE_APP_BACKEND_URL}/api/movement/all?page=last`,
    },
    ListView: 'MovementList',
    detailView: 'MovementDetail',
  },
}

export default createStore({
  state,
  getters,
  actions,
  mutations,
})
