<template>
  <div class="flex-1 flex justify-center items-center">
    <span @click="getPaintings(this.$store, this.url)">
      <template v-if="orientation === 'right'">
        <ArrowRightIcon />
      </template>
      <template v-if="orientation === 'left'">
        <ArrowLeftIcon />
      </template>
    </span>
  </div>
</template>

<script>
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/solid'
import { getPaintings } from '@store/actions'

export default {
  name: 'GoToPaginate',
  props: {
    orientation: String,
  },
  components: { ArrowLeftIcon, ArrowRightIcon },
  methods: {
    getPaintings,
  },
  computed: {
    url() {
      if (this.orientation === 'right') {
        return this.$store.state.paintings.paginator.next
      } else if (this.orientation === 'left') {
        return this.$store.state.paintings.paginator.previous
      } else {
        return ''
      }
    },
  },
}
</script>
