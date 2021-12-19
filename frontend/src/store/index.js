import { createStore } from 'vuex'
import * as getters from '@store/getters'
import * as actions from '@store/actions'
import mutations from '@store/mutations'

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
