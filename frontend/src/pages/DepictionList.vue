<template class>
  <section class="bg-gray-700 flex flex-row justify-between">
    <go-to-paginate
      v-bind:orientation="'left'"
      v-bind:paginator="paginator"
      @fetch="getDepicts"
    />
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
    <go-to-paginate
      v-bind:orientation="'right'"
      v-bind:paginator="paginator"
      @fetch="getDepicts"
    />
  </section>
</template>

<script>
import store from '@store'
import { getDepicts } from '@store/actions'
import { mapState } from 'vuex'

getDepicts(store, `${import.meta.env.VITE_APP_BACKEND_URL}/api/depiction/all/`)

export default {
  name: 'DepictionList',
  methods: {
    getDepicts,
  },
  computed: mapState({
    depicts: (state) => state.depicts.data,
    paginator: (state) => state.depicts.paginator,
  }),
}
</script>
