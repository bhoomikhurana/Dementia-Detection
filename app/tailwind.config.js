/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        customBlue:"#EFF6FF",
        textBlue:"#BFDBFE"
      }
    },
  },
  plugins: [],
}