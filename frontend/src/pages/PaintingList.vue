<template :is="PaintingList">
  <section class="container sm:px-3 mx-auto flex flex-col justify-center items-center">
    <pagination
      v-show="this.paintings.length > 0"
      :paginator="paginator"
      :count="count"
      @fetch="getPaintings"
      class="self-end"
    />
    <product-list
      :products="paintings"
      :paginator="paginator"
      :count="count"
      v-bind:detailView="'PaintingDetail'"
    />
  </section>
</template>

<script>
import store from '@store'
import { getPaintings } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'PaintingList',
  title: `${import.meta.env.VITE_APP_FRONTEND_NAME} - Paintings`,
  methods: {
    getPaintings,
  },
  mounted() {
    this.getPaintings(
      store,
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/all/`
    )
  },
  computed: mapState({
    paintings: (state) => state.paintings.data,
    paginator: (state) => state.paintings.paginator,
    count: (state) => state.paintings.count,
  }),
}
</script>
