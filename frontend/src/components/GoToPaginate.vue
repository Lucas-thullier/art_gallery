<template>
  <div
    class="flex-1 flex items-center justify-center max-w-sm space-between"
    @click="this.$emit('fetch', this.$store, this.url)"
    @mouseover="hover = true"
    @mouseleave="hover = false"
    :class="{ 'bg-gray-800 cursor-pointer': hover }"
  >
    <span class="block flex">
      <template v-if="orientation === 'right'">
        <ArrowRightIcon class="text-gray-700 max-h-40" />
      </template>
      <template v-if="orientation === 'left'">
        <ArrowLeftIcon class="text-gray-700 max-h-40" />
      </template>
    </span>
  </div>
</template>

<style></style>

<script>
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/solid'

export default {
  name: 'GoToPaginate',
  data() {
    return {
      hover: false,
    }
  },
  props: {
    orientation: String,
    paginator: Object,
  },
  components: { ArrowLeftIcon, ArrowRightIcon },
  computed: {
    url() {
      if (this.orientation === 'right') {
        if (this.paginator.next == null) {
          return this.paginator.first
        } else {
          return this.paginator.next
        }
      } else if (this.orientation === 'left') {
        if (this.paginator.previous == null) {
          return this.paginator.last
        } else {
          return this.paginator.previous
        }
      }
    },
  },
}
</script>
