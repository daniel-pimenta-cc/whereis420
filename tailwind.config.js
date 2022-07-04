module.exports = {
  content: [
    './public/index.html',
    './src/**/*.{html,js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      fontFamily: {
        text: ['Text', 'sans-serif'],
        title: ['Audiowide', 'sans-serif']
      },
      animation: {
        'ping-logo': 'ping 3s cubic-bezier(0, 0, 0.2, 1) 1',
        'logoBG': 'logoBG 5s linear infinite'
      }
    },
  },
  plugins: []
}