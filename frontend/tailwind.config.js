@"
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'guardian-blue': '#0066FF',
        'guardian-cyan': '#00D9FF',
        'guardian-purple': '#7B2FFF',
        'guardian-dark': '#0A0E27',
      },
    },
  },
  