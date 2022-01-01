<template>
  <nav
    class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px pt-4"
    aria-label="Pagination"
  >
    <div
      @click="
        this.paginator.previous
          ? this.$emit('fetch', this.$store, this.paginator.previous)
          : this.$emit('fetch', this.$store, this.paginator.last)
      "
      class="
        relative
        inline-flex
        items-center
        px-2
        py-2
        rounded-l-md
        border border-gray-300
        bg-gray:700
        text-sm
        font-medium
        text-gray-300
        hover:bg-gray-600
        cursor-pointer
      "
    >
      <span class="sr-only">Previous</span>
      <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
    </div>
    <!-- Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" -->
    <div
      @click="
        this.paginator.first
          ? this.$emit('fetch', this.$store, this.paginator.first)
          : null
      "
      aria-current="page"
      class="
        z-10
        bg-gray-700
        border border-gray-300
        text-gray-300
        relative
        inline-flex
        items-center
        px-4
        py-2
        text-sm
        hover:bg-gray-600
        cursor-pointer
        font-medium
      "
    >
      1
    </div>

    <span
      class="
        relative
        inline-flex
        items-center
        px-4
        py-2
        border border-gray-300
        bg-gray:700
        text-sm
        font-medium
        hover:bg-gray-600
        cursor-pointer
        text-gray-200
      "
    >
      ...
    </span>
    <div
      @click="
        this.paginator.last
          ? this.$emit('fetch', this.$store, this.paginator.last)
          : null
      "
      aria-current="page"
      class="
        z-10
        bg-gray-700
        border border-gray-300
        text-gray-300
        relative
        inline-flex
        items-center
        px-4
        py-2
        text-sm
        cursor-pointer
        hover:bg-gray-600
        font-medium
      "
    >
      {{ this.count }}
    </div>
    <div
      @click="
        this.paginator.next
          ? this.$emit('fetch', this.$store, this.paginator.next)
          : this.$emit('fetch', this.$store, this.paginator.first)
      "
      class="
        z-10
        bg-gray-700
        border border-gray-300
        text-gray-300
        relative
        inline-flex
        items-center
        px-2
        py-2
        text-sm
        font-medium
        cursor-pointer
        hover:bg-gray-600
        rounded-r-md
      "
    >
      <span class="sr-only">Next</span>
      <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
    </div>
  </nav>
</template>

<script>
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/solid'

export default {
  props: {
    paginator: Object,
    count: Number,
  },
  components: {
    ChevronLeftIcon,
    ChevronRightIcon,
  },
}
</script>
