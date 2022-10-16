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
        '17screen': '17vh',
        '30screen': '30vh',
        '40screen': '40vh',
        '50screen': '50vh',
        '10px': '10px',
      },
      height: {
        '1screen': '1vh',
        '7screen': '7vh',
        '10screen': '10vh',
        '20screen': '20vh',
        '70screen': '70vh',
        '80screen': '80vh',
        '73screen': '73vh',
        '83screen': '83vh',
        '90screen': '90vh'
      },
      width: {
        '40px': '40px'
      },
      fontFamily: {
        'sans': '"Source Sans Pro", Helvetica, sans-serif'
      },
      colors: {
        'black': 'rgb(0 0 0)',
        'gray': 'rgb(50 50 50)',
        'darkgray': 'rgb(35 35 35)',
        'darkergray': 'rgb(25 25 25)',
        'darkestgray': 'rgb(15 15 15)',
        'accent': 'rgb(230 115 0)',
        'brand': 'rgb(60 100 120)'
      },
      backgroundImage: {
        'main': "linear-gradient( rgba(0, 0, 0, 0.67), rgba(0, 0, 0, 0.67) ), url('/images/ValleyLastLight.jpg')"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}