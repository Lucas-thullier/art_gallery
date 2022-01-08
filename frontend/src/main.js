import { createApp } from 'vue'
import store from '@store'

import App from '@/App.vue'
import router from '@router/index'
import components from '@components/index'
import titleMixin from '@mixins/titleMixin'

import '@/assets/tailwind.css'

const app = createApp(App)

for (const key in components) {
  app.component(key, components[key])
}

app.use(router)
app.use(store)

app.mixin(titleMixin)

app.mount('#app')
