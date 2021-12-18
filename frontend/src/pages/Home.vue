<template>
  <ul>
    <li v-for="painting in paintings" :key="painting.pk">
      <a :href="`#/painting/${painting.pk}`">{{ painting.fields.name }}</a>
    </li>
  </ul>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      paintings: [],
    }
  },
  mounted() {
    axios
      .get('http://localhost:8000/api/painting/all')
      .then((response) => {
        this.paintings.push(...response.data)
      })
      .catch((e) => console.error(e))
  },
}
</script>
