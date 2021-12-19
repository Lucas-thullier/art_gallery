<template class>
  <section class="bg-gray-700 flex flex-row">
    <go-to-paginate v-bind:orientation="'left'"></go-to-paginate>
    <product-list v-bind:products="this.paintingsData.paintings"></product-list>
    <go-to-paginate v-bind:orientation="'right'"></go-to-paginate>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      paintingsData: {
        paintings: [],
        count: 0,
        paginator: {
          next: '',
          previous: '',
        },
      },
      paintingsCount: 0,
    }
  },
  mounted() {
    axios
      .get('http://localhost:8000/api/painting/all')
      .then((response) => {
        this.paintingsData.paintings.push(...response.data.results)
      })
      .catch((e) => console.error(e))
  },
}
</script>
