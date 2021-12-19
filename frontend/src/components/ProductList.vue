<template>
  <div class="max-w-2xl lg:max-w-7xl">
    <div
      class="mt-6 grid grid-cols-1 gap-y-3 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
    >
      <div v-for="product in products" :key="product.id" class="group relative">
        <div
          class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80 lg:aspect-none"
        >
          <img
            :src="product.picture_url"
            :alt="product.imageAlt"
            class="w-full h-full object-center object-cover lg:w-full lg:h-full"
          />
        </div>
        <div class="mt-4 flex justify-between">
          <div>
            <h3 class="text-sm text-white">
              <router-link :to="`/painting/${product.id}`">
                <span aria-hidden="true" class="absolute inset-0" />
                {{ product.name }}
              </router-link>
            </h3>
          </div>
          <p class="mt-1 text-sm text-gray-500">
            <span> {{ product.height }} height </span>
            <span> {{ product.width }} width </span>
          </p>
          <p class="text-sm font-medium text-gray-900"></p>
        </div>
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
