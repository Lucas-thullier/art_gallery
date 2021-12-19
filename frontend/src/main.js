import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import components from './components/index'

import '@/assets/tailwind.css'

const app = createApp(App)

for (const key in components) {
  app.component(key, components[key])
}


app.use(router)
app.mount('#app')
