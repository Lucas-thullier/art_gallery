import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

const vueSrc = './src'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, vueSrc),
      '@components': path.resolve(__dirname, vueSrc + '/components'),
      '@pages': path.resolve(__dirname, vueSrc + '/pages'),
      '@router': path.resolve(__dirname, vueSrc + '/router'),
      '@store': path.resolve(__dirname, vueSrc + '/store'),
      '@assets': path.resolve(__dirname, vueSrc + '/assets'),
      '@mixins': path.resolve(__dirname, vueSrc + '/mixins'),
    },
    extensions: ['.js', '.vue', '.json'],
  },
})
