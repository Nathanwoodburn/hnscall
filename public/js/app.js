// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener("load", function() {
        navigator.serviceWorker
          .register("../js/pwa.js")
          .then(res => console.log("service worker registered"))
          .catch(err => console.log("service worker not registered", err))
      })
}