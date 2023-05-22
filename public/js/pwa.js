// Service Worker for PWA
const staticCache = 'static-cache-v1';
const assets = [
    '/',
    '/privacy',
    '/about',
]

self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(staticCache).then(cache => {
            cache.addAll(assets);
        })
    );
})
self.addEventListener('fetch', evt => {
    evt.respondWith(
        caches.match(evt.request).then(cacheRes => {
            return cacheRes || fetch(evt.request);
        })
    );
})