<template>
  <section class="flex dark:bg-gray-700 text-white body-font h-93percent">
    <div class="h-full container p-5 mx-auto grid place-items-center">
      <div>
        <h1>
          {{ this.painting.name }}
        </h1>
      </div>
      <img
        class="rounded object-contain max-h-full"
        :src="this.painting.picture_url"
        alt="step"
      />
    </div>

    <div class="dark:bg-gray-800 flex flex-col justify-between basis-1/2">
      <div>
        <span>{{ this.painting.inception_at }}</span>
      </div>
      <div>
        <h2>Potential Creators</h2>
        <span v-for="creator in this.painting.creators" :key="creator.id">
          <router-link
            :to="{
              name: 'CreatorDetail',
              params: { url: creator.url, id: creator.id },
            }"
          >
            {{ creator.name }}
          </router-link>
        </span>
      </div>
      <div>
        <h2>Materials</h2>
        <span
          class="
            bg-gray-100
            inline-block
            text-gray-800 text-xs
            font-semibold
            mr-2
            px-2.5
            py-0.5
            rounded-full
            dark:bg-gray-700 dark:text-gray-300
          "
          v-for="material in this.painting.materials"
          :key="material.id"
        >
          {{ material.name }}
        </span>
      </div>
      <div>
        <h2>Genres</h2>
        <span
          class="
            bg-gray-100
            inline-block
            text-gray-800 text-xs
            font-semibold
            mr-2
            px-2.5
            py-0.5
            rounded-full
            dark:bg-gray-700 dark:text-gray-300
          "
          v-for="genre in this.painting.genre"
          :key="genre.id"
        >
          {{ genre.name }}
        </span>
      </div>
      <div>
        <h2>Movements</h2>
        <span
          class="
            bg-gray-100
            inline-block
            text-gray-800 text-xs
            font-semibold
            mr-2
            px-2.5
            py-0.5
            rounded-full
            dark:bg-gray-700 dark:text-gray-300
          "
          v-for="movement in this.painting.movements"
          :key="movement.id"
        >
          {{ movement.name }}
        </span>
      </div>
      <div>
        <h2>Locations</h2>
        <span
          class="
            bg-gray-100
            inline-block
            text-gray-800 text-xs
            font-semibold
            mr-2
            px-2.5
            py-0.5
            rounded-full
            dark:bg-gray-700 dark:text-gray-300
          "
          v-for="location in this.painting.locations"
          :key="location.id"
        >
          {{ location.name }}
        </span>
      </div>
      <div>
        <h2>Depicts</h2>
        <span
          v-for="depiction in this.painting.depicts"
          :key="depiction.id"
          class="
            bg-gray-100
            inline-block
            text-gray-800 text-xs
            font-semibold
            mr-2
            px-2.5
            py-0.5
            rounded
            dark:bg-gray-700 dark:text-gray-300
          "
        >
          {{ depiction.name }}
        </span>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PaintingDetail',
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      painting: {},
      isLoaded: false,
    }
  },
  mounted() {
    const url =
      this.url ??
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/${this.id}`

    axios
      .get(url)
      .then((response) => {
        console.log(response.data)
        this.painting = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
