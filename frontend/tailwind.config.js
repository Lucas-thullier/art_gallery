module.exports = {
  purge: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      maxHeight: {
        184: '46rem',
      },
      height: {
        184: '46rem',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
