module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  daisyui: {
    themes: ["corporate"],
  },
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}