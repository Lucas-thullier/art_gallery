<template>
  <div class="flex items-center justify-center flex-1 flex-col">
    <div
      class="
        mt-6
        grid grid-cols-1
        gap-y-3 gap-x-6
        sm:grid-cols-2
        lg:grid-cols-4
        xl:gap-x-8
      "
    >
      <div v-for="product in products" :key="product.id" class="group relative">
        <router-link
          :to="{
            name: detailView,
            params: { url: product.url, id: product.id },
          }"
        >
          <img
            :src="this.picture_url(product)"
            :alt="product.imageAlt"
            @error="setFallbackImageUrl"
            class="
              object-scale-down
              w-full
              h-80
              rounded-md
              overflow-hidden
              group-hover:opacity-75
              lg:h-80
            "
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
import picture from '@assets/placeholder_profil_picture.jpg'

export default {
  props: {
    products: Array,
    detailView: String,
    paginator: Object,
    count: Number,
  },
  methods: {
    setFallbackImageUrl(event) {
      event.target.src = picture
    },
    picture_url(product) {
      if (product.picture_url) {
        return product.picture_url
      } else if (product.paintings && product.paintings[0]) {
        return product.paintings[0].picture_url
      } else {
        return picture
      }
    },
  },
}
</script>
