<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    WIP
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MaterialDetail',
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      material: {},
      isLoaded: false,
    }
  },
  mounted() {
    const url = `${import.meta.env.VITE_APP_BACKEND_URL}/api/material/${
      this.$route.params.id
    }`

    axios
      .get(url)
      .then((response) => {
        this.material = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
