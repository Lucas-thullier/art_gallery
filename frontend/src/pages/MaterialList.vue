<template class>
  <section class="bg-gray-700 flex flex-row">WIP</section>
</template>

<script>
import store from '@store'
import { getMaterials } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'MaterialList',
  methods: {
    getMaterials,
  },
  mounted() {
    this.getMaterials(
      store,
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/material/all/`
    )
  },
  computed: mapState({
    materials: (state) => state.paintings.data,
    paginator: (state) => state.paintings.paginator,
  }),
}
</script>
