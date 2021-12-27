<template>
  <div
    class="flex-1 flex items-center justify-center"
    @mouseover="hover = true"
    @mouseleave="hover = false"
    :class="{ 'bg-gray-800 cursor-pointer': hover }"
  >
    <span class="block flex" @click="getPaintings(this.$store, this.url)">
      <template v-if="orientation === 'right'">
        <ArrowRightIcon class='text-gray-700 max-h-40'/>
      </template>
      <template v-if="orientation === 'left'">
        <ArrowLeftIcon class='text-gray-700 max-h-40' />
      </template>
    </span>
  </div>
</template>

<style></style>

<script>
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/solid'
import { getPaintings } from '@store/actions'

export default {
  name: 'GoToPaginate',
  data() {
    return {
      hover: false,
    }
  },
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
