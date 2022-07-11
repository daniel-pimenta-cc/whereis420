module.exports = {
  content: [
    './templates/index.html',
    './static/js/*.{js, ts}'
  ],
  theme: {
    fontSize: {
      pix_s1: '12px',
      pix_s2: '24px',
      pix_s3: '36px',
      pix_s4: '48px',
      pix_s5: '60px',
      pix_s6: '72px',
      pix_s7: '84px',
      pix_s8: '96px',
      pix_s9: '108px',
      pix_s10: '120px',
      bitcell_s1: '16px',
      bitcell_s2: '32px',
      bitcell_s3: '48px',
      bitcell_s4: '64px',
      bitcell_s5: '80px',
      bitcell_s6: '96px',
      bitcell_s7: '112px',
      bitcell_s8: '128px'
    },
    extend: {
      fontFamily: {
        'pix': ['Pix Antiqua', 'monospace'],
        'bitcell': ['Bitcell', 'monospace'],
        'modern-dos': ['Modern DOS', 'monospace']
      }
    }
  },
  plugins: []
}