import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import Navbar from './components/Navbar'
import '@/assets/tailwind.css'

const app = createApp(App)
app.component('navbar', Navbar)
app.use(router)
app.mount('#app')
