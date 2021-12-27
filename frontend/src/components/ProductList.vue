<template>
  <div class="max-w-2xl lg:max-w-7xl flex items-center">
    <div
      class="mt-6 grid grid-cols-1 gap-y-3 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
    >
      <div v-for="product in products" :key="product.id" class="group relative">
        <router-link :to="`/painting/${product.id}`">
          <img
            :src="product.picture_url"
            :alt="product.imageAlt"
            class="object-scale-down w-full h-80 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80"
          />

          <div class="mt-4 flex justify-between">
            <h1 class="text-sm flex-1 text-white">
              {{ product.name }}
            </h1>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    products: Array,
  },
}
</script>
