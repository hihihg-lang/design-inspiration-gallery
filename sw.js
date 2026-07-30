const CACHE_NAME = 'design-gallery-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/palette.html',
  '/philosophy.html',
  '/reference.html',
  '/color-mixer.html',
  '/zh/index.html',
  '/zh/palette.html',
  '/zh/philosophy.html',
  '/zh/reference.html',
  '/zh/color-mixer.html',
  '/manifest.json'
];

// Install
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
  self.skipWaiting();
});

// Activate
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Fetch
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cached) => {
      const fetchPromise = fetch(event.request).then((response) => {
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, clone);
          });
        }
        return response;
      }).catch(() => {
        return cached || new Response('Offline', { status: 503 });
      });

      return cached || fetchPromise;
    })
  );
});