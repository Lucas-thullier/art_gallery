<template class>
  <section class="container mx-auto flex flex-col justify-center items-center">
    <div class="self-center">
      <ul class="list-disc text-left bg-gray-800 p-10 rounded">
        <li
          v-for="(depiction, key) in this.depicts"
          :key="key"
          class="text-white"
        >
          <router-link
            :to="{
              name: 'DepictionDetail',
              params: { url: depiction.url, id: depiction.id },
            }"
          >
            {{ depiction.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
import store from '@store'
import { getDepicts } from '@store/actions'
import { mapState } from 'vuex'

export default {
  name: 'DepictionList',
  methods: {
    getDepicts,
  },
  mounted() {
    this.getDepicts(
      store,
      `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/all/`
    )
  },
  computed: mapState({
    depicts: (state) => state.depicts.data,
    paginator: (state) => state.depicts.paginator,
  }),
}
</script>
