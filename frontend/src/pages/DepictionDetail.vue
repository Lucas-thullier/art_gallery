<template>
  <section
    class="container sm:px-3 mx-auto flex flex-col justify-center items-center"
  >
    <pagination
      v-show="this.paintings.length > 0"
      :paginator="paginator"
      :count="parseInt(paintings.length / 8)"
      @fetch="updatePagination"
      class="self-end"
    />
    <div class="flex items-center flex-1 flex-col">
      <h1 class="text-white">{{ this.depiction.name }}</h1>
      <product-list
        v-bind:products="renderedPaintings"
        v-bind:detailView="'PaintingDetail'"
      />
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DepictionDetail',
  title: `${import.meta.env.VITE_APP_FRONTEND_NAME} - Depiction`,
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      depiction: {},
      paintings: {},
      paginator: {
        first: { offset: 0, end: 8 },
        previous: { offset: 0, end: 0 },
        actual: { offset: 0, end: 8 },
        next: { offset: 0, end: 0 },
        last: { offset: 0, end: 0 },
      },
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      const url = `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/${
        this.$route.params.id
      }`
      axios
        .get(url)
        .then((response) => {
          this.depiction = response.data
          this.paintings = this.depiction.paintings
          this.initPaginator()
          this.isLoaded = true
        })
        .catch((e) => console.error(e))
    },
    updatePagination(store, paginator) {
      console.log(this.paginator, paginator)
      this.paginator.actual = paginator
    },
    initPaginator() {
      console.log('count depict: ', this.paintings.length)
      this.paginator.first = { offset: 0, end: 8 }

      this.paginator.previous = {
        offset:
          this.paginator.actual.offset - 8 < 0
            ? this.paintings.length - 1 - 8
            : this.paginator.actual.offset - 8,
        end:
          this.paginator.actual.end - 8 <= 0
            ? this.paintings.length - 1
            : this.paginator.actual.end,
      }

      this.paginator.actual = { offset: 0, end: 8 }

      this.paginator.next = {
        offset:
          this.paginator.actual.offset + 8 > this.paintings.length - 1
            ? 0
            : this.paginator.actual.offset + 8,
        end:
          this.paginator.actual.end + 8 > this.paintings.length
            ? 8
            : this.paginator.actual.end + 8,
      }

      this.paginator.last = {
        offset: this.paintings.length - 1 - 8,
        end: this.paintings.length - 1,
      }
    },
  },
  computed: {
    renderedPaintings() {
      if (this.paintings.length > 0 && this.paginator.actual) {
        return this.paintings.slice(
          this.paginator.actual.offset,
          this.paginator.actual.end
        )
      } else {
        return []
      }
    },
  },
  watch: {
    '$route.params.id': function (from, to) {
      if (this.$route?.params?.id) {
        this.fetchData()
      }
    },
  },
}
</script>
