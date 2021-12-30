<template class>
  <section class="bg-gray-700 flex flex-row">WIP</section>
</template>

<script>
import store from '@store'
import { getPaintings } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  computed: mapState({
    paintings: (state) => state.paintings.data,
  }),
}
</script>
