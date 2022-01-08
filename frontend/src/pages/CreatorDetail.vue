<template>
  <section
    class="
      flex flex-col
      lg:flex-row
      dark:bg-gray-700
      text-white
      body-font
      h-93percent
    "
  >
    <router-link
      @wheel="scrollTroughtPaintings"
      id="painting-slider"
      ref="paintingSlider"
      class="h-full container p-5 mx-auto grid place-items-center"
      :to="{
        name: 'PaintingDetail',
        params: {
          url: actualDisplayedPainting.url,
          id: actualDisplayedPainting.id,
        },
      }"
    >
      <span>
        {{ actualDisplayedPainting.name }}
      </span>
      <img
        class="rounded object-contain max-h-full"
        :src="actualDisplayedPainting.picture_url"
        :alt="actualDisplayedPainting.name"
      />
    </router-link>

    <aside class="dark:bg-gray-800 flex flex-col justify-between basis-1/2">
      <div class="flex flex-row items-center justify-between p-2">
        <h1>
          {{ this.creator.name }}
        </h1>
        <img
          class="h-24 w-24 rounded-full object-fill"
          @error="setFallbackImageUrl"
          :src="this.creator.picture_url"
          :alt="this.creator.name"
        />
      </div>
      <ul class="flex-1 text-left overflow-y-auto">
        <li
          @click=";(this.actualPainting = key), computePaginator()"
          v-for="(painting, key) in this.allPaintings"
          :class="{
            'transition ease-in-out hover:cursor-pointer hover:bg-gray-700': true,
            'bg-gray-700': key == this.actualPainting,
          }"
        >
          <span>
            {{ painting.name }}
          </span>
          <span> - </span>
          <span>
            {{ painting.inception_at }}
          </span>
        </li>
      </ul>
      <div class="overflow-y-auto text-left" id="creator-data">
        <div class="flex flex-row justify-between px-3 py-2">
          <div>
            <h2>Main Depicts</h2>
            <div
              v-for="(depiction, key) in this.creatorDetails['depicts']?.slice(
                0,
                3
              )"
              :key="key"
            >
              <span>
                {{ depiction.name }}
              </span>
              <span> - </span>
              <span>
                {{ depiction.total }}
              </span>
            </div>
          </div>
          <div>
            <h2>Main Movements</h2>
            <div
              v-for="(movement, key) in this.creatorDetails['movements']?.slice(
                0,
                3
              )"
              :key="key"
            >
              <span>
                {{ movement.name }}
              </span>
              <span> - </span>
              <span>
                {{ movement.total }}
              </span>
            </div>
          </div>
          <div>
            <h2>Main Materials</h2>
            <div
              v-for="(material, key) in this.creatorDetails['materials']?.slice(
                0,
                3
              )"
              :key="key"
            >
              <span>
                {{ material.name }}
              </span>
              <span> - </span>
              <span>
                {{ material.total }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </aside>
  </section>
</template>

<script>
import axios from 'axios'
import picture from '@assets/placeholder_profil_picture.jpg'

export default {
  name: 'CreatorDetail',
  title: `${import.meta.env.VITE_APP_FRONTEND_NAME} - Creator`,
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      creator: {},
      creatorDetails: {},
      actualPainting: 0,
      paginator: null,
      isLoaded: false,
      allPaintings: {},
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    setFallbackImageUrl(event) {
      event.target.src = picture
    },
    computePaginator() {
      const maxIndex = this.allPaintings.length - 1
      const paginator = {
        prev: null,
        actual: this.actualPainting,
        next: null,
      }

      if (this.actualPainting - 1 < 0) {
        paginator.prev = maxIndex
      } else {
        paginator.prev = this.actualPainting - 1
      }

      if (this.actualPainting + 1 > maxIndex) {
        paginator.next = 0
      } else {
        paginator.next = this.actualPainting + 1
      }

      this.paginator = paginator
    },
    scrollTroughtPaintings(event) {
      const isScrollDown = event.deltaY > 0
      if (isScrollDown) {
        this.actualPainting = this.paginator.next
      } else {
        this.actualPainting = this.paginator.prev
      }

      this.computePaginator()
    },
    fetchData() {
      const url = `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/${
        this.$route.params.id
      }/`

      const detailsUrl = `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/${
        this.$route.params.id
      }/detailed`

      axios
        .get(url)
        .then((response) => {
          this.creator = response.data
          this.allPaintings = response.data.paintings
          this.computePaginator()
          this.isLoaded = true
        })
        .catch((e) => console.error(e))

      axios
        .get(detailsUrl)
        .then((response) => {
          this.creatorDetails = response.data
        })
        .catch((e) => console.error(e))
    },
  },
  computed: {
    actualDisplayedPainting() {
      if (this.paginator) {
        return this.allPaintings[this.paginator.actual]
      } else {
        return { name: '', id: '0', url: '' }
      }
    },
  },
  watch: {
    '$route.params.id': function () {
      if (this.$route?.params?.id) {
        this.fetchData()
      }
    },
  },
}
</script>
