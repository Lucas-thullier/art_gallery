<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    <go-to-paginate
      v-bind:orientation="'left'"
      v-bind:paginator="this.paginator"
      @fetch="updatePage"
    />
    <div>
      <h1>{{ this.depiction.name }}</h1>
      <product-list
        v-bind:products="renderedPaintings"
        v-bind:detailView="'PaintingDetail'"
      />
    </div>
    <go-to-paginate
      v-bind:orientation="'right'"
      v-bind:paginator="this.paginator"
      @fetch="updatePage"
    />
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
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/${this.id}`

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
}
</script>
