import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import Navbar from './components/Navbar'
import ProductList from './components/ProductList'
import '@/assets/tailwind.css'

const app = createApp(App)
app.component('navbar', Navbar)
app.component('product-list', ProductList)
app.use(router)
app.mount('#app')
