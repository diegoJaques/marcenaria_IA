/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'wood': {
          50: '#faf8f5',
          100: '#f5f0e8',
          200: '#e8dcc8',
          300: '#d4bd9a',
          400: '#c19b6b',
          500: '#a67c52',
          600: '#8b6240',
          700: '#6e4e33',
          800: '#563d28',
          900: '#44311f',
        }
      }
    },
  },
  plugins: [],
}
