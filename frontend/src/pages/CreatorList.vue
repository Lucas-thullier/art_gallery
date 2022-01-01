<template class>
  <section class="container mx-auto flex flex-col justify-center items-center">
    <pagination
      v-show="this.creators.length > 0"
      :paginator="paginator"
      :count="count"
      @fetch="getCreators"
      class="self-end"
    />
    <product-list
      v-bind:products="creators"
      v-bind:detailView="'CreatorDetail'"
    />
  </section>
</template>

<script>
import store from '@store'
import { getCreators } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'CreatorList',
  methods: {
    getCreators,
  },
  mounted() {
    this.getCreators(
      store,
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/all/`
    )
  },
  computed: mapState({
    creators: (state) => state.creators.data,
    paginator: (state) => state.creators.paginator,
    count: (state) => state.creators.count,
  }),
}
</script>
