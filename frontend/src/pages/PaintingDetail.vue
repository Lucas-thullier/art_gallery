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
    <div class="h-full container p-5 mx-auto grid place-items-center">
      <div>
        <h1>
          {{ this.painting.name }}
        </h1>
      </div>
      <img
        @click="setModal(true)"
        class="rounded object-contain cursor-pointer max-h-full"
        :src="this.painting.picture_url"
        :alt="this.painting.name"
      />
    </div>

    <div class="dark:bg-gray-800 flex flex-col justify-between lg:basis-1/2">
      <div class="border-bottom">
        <span>{{ this.painting.inception_at }}</span>
      </div>
      <div>
        <h2>Creator</h2>
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
      <div class="flex flex-row justify-evenly">
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
      </div>
      <div>
        <h2>Depicts</h2>
        <span
          v-for="(depiction, key) in this.painting.depicts"
          :key="key"
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
          <router-link
            class="flex-1 flex flex-col"
            :to="{
              name: 'DepictionDetail',
              params: {
                url: depiction.url,
                id: depiction.id,
              },
            }"
          >
            {{ depiction.name }}
          </router-link>
        </span>
      </div>
    </div>
    <full-size-painting
      :open="open"
      @setModal="setModal"
      :picture="this.painting.picture_url"
    />
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PaintingDetail',
  title: `${import.meta.env.VITE_APP_FRONTEND_NAME} - Painting`,
  props: {
    url: String,
    id: String,
  },
  data() {
    return {
      painting: {},
      isLoaded: false,
      open: false,
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      const url = `${import.meta.env.VITE_APP_BACKEND_URL}/api/painting/${
        this.$route.params.id
      }/`

      axios
        .get(url)
        .then((response) => {
          this.painting = response.data
          this.isLoaded = true
        })
        .catch((e) => console.error(e))
    },
    setModal(newValue) {
      this.open = newValue
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
