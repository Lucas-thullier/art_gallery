import { createStore } from 'vuex'
import * as getters from './getters'
import * as actions from './actions'
import mutations from './mutations'

const state = {
  paintings: {
    data: [],
    count: 0,
    paginator: {
      next: '',
      previous: '',
    },
  },
}

export default createStore({
  state,
  getters,
  actions,
  mutations,
})
