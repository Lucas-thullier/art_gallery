<template>
  <div class="bg-white">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <!-- 
      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900">
        En avant
      </h2>-->
      <div
        class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
      >
        <div
          v-for="product in products"
          :key="product.pk"
          class="group relative"
        >
          <div
            class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80 lg:aspect-none"
          >
            <img
              :src="product.fields.picture_url"
              :alt="product.imageAlt"
              class="w-full h-full object-center object-cover lg:w-full lg:h-full"
            />
          </div>
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm text-gray-700">
                <router-link :to="`/painting/${product.pk}`">
                  <span aria-hidden="true" class="absolute inset-0" />
                  {{ product.fields.name }}
                </router-link>
              </h3>
            </div>
            <p class="mt-1 text-sm text-gray-500">
              <span> {{ product.fields.height }} height </span>
              <span> {{ product.fields.width }} width </span>
            </p>
            <p class="text-sm font-medium text-gray-900"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// const products = [
//   {
//     id: 1,
//     name: 'Basic Tee',
//     href: '#',
//     imageSrc:
//       'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
//     imageAlt: "Front of men's Basic Tee in black.",
//     price: '$35',
//     color: 'Black',
//   },
//   // More products...
// ]

export default {
  setup() {
    return {
      // products,
    }
  },
  props: {
    products: Array,
  },
}
</script>
