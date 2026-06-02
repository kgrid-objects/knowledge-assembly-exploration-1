import { defineConfig } from 'vite'

export default defineConfig({
  root: '.',
  base: './', // for GitHub Pages
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: 'index.html'
    }
  }
})