<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    <div
      @wheel="reverseScrollAxis"
      id="painting-slider"
      ref="paintingSlider"
      class="
        h-full
        container
        p-5
        mx-auto
        flex flex-row
        items-center
        overflow-x-scroll
        snap-mandatory snap-x
      "
      dir="ltr"
    >
      <div
        class="min-w-full h-full flex mx-4 snap-center"
        v-for="(painting, key) in this.creator.paintings"
        :id="`painting-${key}`"
        :key="key"
      >
        <router-link
          class="flex-1 flex flex-col"
          :to="{
            name: 'PaintingDetail',
            params: { url: painting.url, id: painting.id },
          }"
        >
          <span>
            {{ painting.name }}
          </span>
          <img
            class="rounded object-contain h-93percent"
            :src="painting.picture_url"
            :alt="painting.name"
          />
        </router-link>
      </div>
    </div>

    <div class="dark:bg-gray-800 flex flex-col justify-between basis-1/2">
      <div>
        <img
          class="h-24 w-24 rounded-full"
          @error="setFallbackImageUrl"
          :src="this.creator.picture_url"
          :alt="this.creator.name"
        />
        <h1>
          {{ this.creator.name }}
        </h1>
      </div>
    </div>
  </section>
</template>

<script>
// @assets/logo.png
import axios from 'axios'
import picture from '@assets/placeholder_profil_picture.jpg'

export default {
  name: 'Detail',
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      creator: {},
      actualPainting: 0,
      isLoaded: false,
    }
  },
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/creator/${this.id}/`

    axios
      .get(url)
      .then((response) => {
        console.log(response.data)
        this.creator = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
  methods: {
    setFallbackImageUrl(event) {
      event.target.src = picture
    },
    reverseScrollAxis(event) {
      if (event.deltaY > 0) {
        if (
          this.actualPainting !=
          this.$refs.paintingSlider.children.length - 1
        ) {
          this.actualPainting += 1
        } else {
          this.actualPainting = 0
        }
      } else {
        if (this.actualPainting - 1 < 0) {
          this.actualPainting = this.$refs.paintingSlider.children.length - 1
        } else {
          this.actualPainting -= 1
        }
      }
      this.$refs.paintingSlider
        .querySelector(`#painting-${this.actualPainting}`)
        .scrollIntoView({ behavior: 'smooth' })
    },
    // reverseScrollAxis(event) {
    //   let diff = 0
    //   let ticking = false

    //   const wheelEvent =
    //     'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel'

    //   this.$refs.paintingSlider.addEventListener(wheelEvent, (e) => {
    //     diff = e.deltaY
    //     if (!ticking) {
    //       this.$refs.paintingSlider.scrollLeft += diff
    //       ticking = false
    //     }
    //     ticking = true
    //   })
    // },
    normalScrollAxis(event) {
      // console.log(event)
    },
  },
}
</script>
