<template>
  <section class="flex bg-gray-700 text-white body-font">
    <div class="h-full container px-5 py-16 mx-auto grid grid-cols-3 gap-x-6">
      <div class="col-span-2">
        <div
          class="grid bg-gray-800 place-items-center min-h-full min-w-full bg-inherit aspect-w-1 aspect-h-1 rounded-md overflow-hidden"
        >
          <img
            class="object-center rounded object-cover max-h-184"
            :src="this.painting.picture_url"
            alt="step"
          />
        </div>
      </div>
      <div class="bg-gray-800 rounded">
        {{ this.painting.name }}
      </div>
      <!-- <div class="lg:w-2/5 md:w-1/2 md:pr-10 md:py-6">
          <div class="flex relative pb-12">
            <div class="flex-grow pl-4">
              <h2
                class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider"
              >
                STEP 1
              </h2>
              <p class="leading-relaxed">
                VHS cornhole pop-up, try-hard 8-bit iceland helvetica. Kinfolk
                bespoke try-hard cliche palo santo offal.
              </p>
            </div>
          </div>
          <div class="flex relative pb-12">
            <div class="flex-grow pl-4">
              <h2
                class="font-medium title-font text-sm text-gray-900 tracking-wider"
              >
                STEP 2
              </h2>
              <p class="leading-relaxed">
                Vice migas literally kitsch +1 pok pok. Truffaut hot chicken
                slow-carb health goth, vape typewriter.
              </p>
            </div>
          </div>
          <div class="flex relative pb-12">
            <div class="flex-grow pl-4">
              <h2
                class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider"
              >
                STEP 3
              </h2>
              <p class="leading-relaxed">
                Coloring book nar whal glossier master cleanse umami. Salvia +1
                master cleanse blog taiyaki.
              </p>
            </div>
          </div>
          <div class="flex relative pb-12">
            <div class="flex-grow pl-4">
              <h2
                class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider"
              >
                STEP 4
              </h2>
              <p class="leading-relaxed">
                VHS cornhole pop-up, try-hard 8-bit iceland helvetica. Kinfolk
                bespoke try-hard cliche palo santo offal.
              </p>
            </div>
          </div>
          <div class="flex relative">
            <div class="flex-grow pl-4">
              <h2
                class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider"
              >
                FINISH
              </h2>
              <p class="leading-relaxed">
                Pitchfork ugh tattooed scenester echo park gastropub whatever
                cold-pressed retro.
              </p>
            </div>
          </div>
        </div> -->
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Detail',
  data() {
    return {
      painting: {},
      isLoaded: false,
    }
  },
  mounted() {
    axios
      .get(
        `${process.env.VUE_APP_BACKEND_URL}/api/painting/${this.$route.params.id}`
      )
      .then((response) => {
        this.painting = response.data
        this.isLoaded = true
      })
      .catch((e) => console.error(e))
  },
}
</script>
