<template class>
  <section class="bg-gray-700 flex flex-row">WIP</section>
</template>

<script>
import store from '@store'
import { getMovements } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'MovementList',
  methods: {
    getMovements,
  },
  mounted() {
    getMovements(
      store,
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/movement/all/`
    )
  },
  computed: mapState({
    movements: (state) => state.movements.data,
    paginator: (state) => state.movements.paginator,
  }),
}
</script>
