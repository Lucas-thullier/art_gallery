<template class>
  <section class="bg-gray-700 flex flex-row">
    <go-to-paginate
      v-bind:orientation="'left'"
      v-bind:paginator="paginator"
      @fetch="getCreators"
    />
    <product-list
      v-bind:products="creators"
      v-bind:detailView="'CreatorDetail'"
    />
    <go-to-paginate
      v-bind:orientation="'right'"
      v-bind:paginator="paginator"
      @fetch="getCreators"
    />
  </section>
</template>

<script>
import store from '@store'
import { getCreators } from '@store/actions'
import { mapState } from 'vuex'

getCreators(store, `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/all/`)

export default {
  name: 'CreatorList',
  methods: {
    getCreators,
  },
  computed: mapState({
    creators: (state) => state.creators.data,
    paginator: (state) => state.creators.paginator,
  }),
}
</script>
