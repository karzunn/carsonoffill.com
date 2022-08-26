// tailwind.config.js
module.exports = {
  purge: {
    enabled: !process.env.ROLLUP_WATCH,
    content: ['./public/index.html', './src/**/*.svelte'],
    options: {
      defaultExtractor: content => [
        ...(content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || []),
        ...(content.match(/(?<=class:)[^=>\/\s]*/g) || []),
      ],
    },
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing: {
        '1screen': '1vh',
        '10screen': '10vh',
        '30screen': '30vh',
      },
      height: {
        '1screen': '1vh',
        '10screen': '10vh',
        '20screen': '20vh',
        '80screen': '80vh'
      },
      fontFamily: {
        'sans': '"Source Sans Pro", Helvetica, sans-serif'
      },
      colors: {
        'black': 'rgb(0 0 0)',
        'gray': 'rgb(50 50 50)',
        'darkgray': 'rgb(35 35 35)',
        'darkestgray': 'rgb(25 25 25)',
        'grayblue': 'rgb(50 100 150)'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}