<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    WIP
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovementDetail',
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      movement: {},
      isLoaded: false,
    }
  },
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/movement/${this.id}`

    axios
      .get(url)
      .then((response) => {
        this.movement = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
