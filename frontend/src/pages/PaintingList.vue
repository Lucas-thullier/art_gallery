<template class>
  <section class="bg-gray-700 flex flex-row">
    <go-to-paginate
      v-bind:orientation="'left'"
      v-bind:paginator="paginator"
      @fetch="getPaintings"
    />
    <product-list
      v-bind:products="paintings"
      v-bind:detailView="'PaintingDetail'"
    />
    <go-to-paginate
      v-bind:orientation="'right'"
      v-bind:paginator="paginator"
      @fetch="getPaintings"
    />
  </section>
</template>

<script>
import store from '@store'
import { getPaintings } from '@store/actions'
import { mapState } from 'vuex'

getPaintings(store, `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/all/`)

export default {
  name: 'PaintingList',
  methods: {
    getPaintings,
  },
  computed: mapState({
    paintings: (state) => state.paintings.data,
    paginator: (state) => state.paintings.paginator,
  }),
}
</script>
