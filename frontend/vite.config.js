module.exports = {
  build: {
    outDir: '../static/js',
    emptyOutDir: true, // also necessary
    rollupOptions: {
        input: "js/index.js",
        output: {
        entryFileNames: 'bundle.js', // Set the desired filename here
      },
    }
  }
}
