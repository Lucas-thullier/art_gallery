<template>
  <div class="flex-1 flex justify-center items-center">
    <span v-if="orientation === 'right'">
      <ArrowRightIcon />
    </span>
    <span v-if="orientation === 'left'">
      <ArrowLeftIcon />
    </span>
  </div>
</template>

<script>
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/solid'

export default {
  name: 'GoToPaginate',
  props: {
    orientation: String,
  },
  components: { ArrowLeftIcon, ArrowRightIcon },
}
</script>
