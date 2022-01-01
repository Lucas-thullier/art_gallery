<template>
  <section
    class="container sm:px-3 mx-auto flex flex-col justify-center items-center"
  >
    <pagination
      v-show="this.paintings.length > 0"
      :paginator="paginator"
      :count="paintings.length"
      @fetch="fetchData"
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
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      depiction: {},
      paintings: {},
      paginator: {
        previous: {},
        actual: { offset: 0, end: 8 },
        next: {},
      },
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    updatePaginator() {
      this.paginator.previous = {
        offset: this.paginator.actual.offset - 8,
        end: this.paginator.actual.end - 8,
      }

      this.paginator.next = {
        offset: this.paginator.actual.offset + 8,
        end: this.paginator.actual.end + 8,
      }
    },
    updatePage(store, paginator) {
      if (paginator.offset < 0) {
        this.paginator.actual = {
          offset: this.paintings.length - 8,
          end: this.paintings.length,
        }
      } else if (paginator.offset > this.paintings.length - 8) {
        this.paginator.actual = {
          offset: 0,
          end: 8,
        }
      } else {
        this.paginator.actual = paginator
      }

      this.updatePaginator()
    },
    fetchData() {
      const url = `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/${
        this.$route.params.id
      }`

      axios
        .get(url)
        .then((response) => {
          this.depiction = response.data
          this.paintings = this.depiction.paintings
          this.isLoaded = true
          this.updatePaginator()
        })
        .catch((e) => console.error(e))
    },
  },
  computed: {
    renderedPaintings() {
      if (this.paintings.length > 0) {
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
    '$route.params.id': function (from, to, t) {
      if (this.$route?.params?.id) {
        this.fetchData()
      }
    },
  },
}
</script>
