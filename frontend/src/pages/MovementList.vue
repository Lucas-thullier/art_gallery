<template class>
  <section class="bg-gray-700 flex flex-row">WIP</section>
</template>

<script>
import store from '@store'
import { getMovements } from '@store/actions'
import { mapState } from 'vuex'

getMovements(store, `${import.meta.env.VITE_APP_BACKEND_URL}/api/movement/all/`)

export default {
  name: 'MovementList',
  methods: {
    getMovements,
  },
  computed: mapState({
    movements: (state) => state.movements.data,
    paginator: (state) => state.movements.paginator,
  }),
}
</script>
