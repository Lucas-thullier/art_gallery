<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    WIP
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DepictionDetail',
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      depiction: {},
      isLoaded: false,
    }
  },
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/${this.id}`

    axios
      .get(url)
      .then((response) => {
        this.depiction = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
