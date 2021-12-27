<template class>
  <section class="bg-gray-700 flex flex-row">
    <go-to-paginate v-bind:orientation="'left'" />
    <product-list v-bind:products="paintings" />
    <go-to-paginate v-bind:orientation="'right'" />
  </section>
</template>

<script>
import store from '@store'
import { getPaintings } from '@store/actions'
import { mapState } from 'vuex'

getPaintings(store, `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/all/`)

export default {
  name: 'Home',
  computed: mapState({
    paintings: (state) => state.paintings.data,
  }),
}
</script>
