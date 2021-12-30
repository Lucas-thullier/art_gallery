<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    <div class="h-full container p-5 mx-auto grid place-items-center">
      <div>
        <h1>
          {{ this.painting.name }}
        </h1>
      </div>
      <img
        class="rounded object-contain max-h-full"
        :src="this.painting.picture_url"
        alt="step"
      />
    </div>

    <div class="dark:bg-gray-800 flex flex-col justify-between basis-1/2">
      WIP
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Detail',
  props: {
    url: String,
  },
  data() {
    return {
      painting: {},
      isLoaded: false,
    }
  },
  mounted() {
    axios
      .get(this.url)
      .then((response) => {
        this.painting = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
