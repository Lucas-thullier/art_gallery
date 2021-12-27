<template>
  <section class="flex bg-gray-700 text-white body-font h-93percent">
    <div
      class="h-full container p-5 mx-auto grid place-items-center"
    >
      <img
        class="rounded object-contain max-h-full"
        :src="this.painting.picture_url"
        alt="step"
      />
    </div>
    <div class="bg-gray-800 rounded basis-1/2">
      {{ this.painting.name }}
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Detail',
  data() {
    return {
      painting: {},
      isLoaded: false,
    }
  },
  mounted() {
    axios
      .get(
        `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/${this.$route.params.id}`
      )
      .then((response) => {
        this.painting = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
