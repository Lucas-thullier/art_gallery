const path = require('path')
const vueSrc = './src'
module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, vueSrc),
        '@components': path.resolve(__dirname, vueSrc + '/components'),
        '@pages': path.resolve(__dirname, vueSrc + '/pages'),
        '@router': path.resolve(__dirname, vueSrc + '/router'),
        '@store': path.resolve(__dirname, vueSrc + '/store'),
        '@assets': path.resolve(__dirname, vueSrc + '/assets'),
      },
      extensions: ['.js', '.vue', '.json'],
    },
  },
}
