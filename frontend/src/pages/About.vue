<template>
  <div :if="isLoaded">
    {{ this.painting.fields?.name }}
  </div>
  <img :if="isLoaded" :src="this.painting.fields?.picture_url" />
</template>

<script>
import axios from 'axios'

export default {
  name: 'About',
  data() {
    return {
      painting: {},
      isLoaded: false
    }
  },
  mounted() {
    axios
      .get(`http://localhost:8000/api/painting/${this.$route.params.id}`)
      .then((response) => {
        this.painting = response.data[0]
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
