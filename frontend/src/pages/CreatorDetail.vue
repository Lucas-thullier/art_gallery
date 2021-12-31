<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    <div
      @wheel="scrollTroughtPaintings"
      id="painting-slider"
      ref="paintingSlider"
      class="h-full container p-5 mx-auto flex flex-row items-center"
    >
      <div class="min-w-full h-full flex">
        <router-link
          class="flex-1 flex flex-col"
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
            class="rounded object-contain h-93percent"
            :src="actualDisplayedPainting.picture_url"
            :alt="actualDisplayedPainting.name"
          />
        </router-link>
      </div>
    </div>

    <div class="dark:bg-gray-800 flex flex-col justify-between basis-1/2">
      <div class="flex flex-row items-center justify-between p-2">
        <h1>
          {{ this.creator.name }}
        </h1>
        <img
          class="h-24 w-24 rounded-full"
          @error="setFallbackImageUrl"
          :src="this.creator.picture_url"
          :alt="this.creator.name"
        />
      </div>
      <aside class="overflow-y-auto text-left" id="creator-data">
        <div
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
        </div>
      </aside>
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
  </section>
</template>

<script>
import axios from 'axios'
import picture from '@assets/placeholder_profil_picture.jpg'

export default {
  name: 'CreatorDetail',
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
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/${this.id}/`

    const detailsUrl = `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/${
      this.id
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
}
</script>
