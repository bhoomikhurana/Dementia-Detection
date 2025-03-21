/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        customBlue: "#EFF6FF",
        textBlue: "#007FFF",
      },
      boxShadow: {
        custom: "0 4px 30px rgba(0, 0, 0, 0.1)", // Add custom shadow here
      },
    },
  },
  plugins: [],
};
