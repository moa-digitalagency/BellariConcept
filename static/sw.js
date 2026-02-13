const CACHE_NAME = 'bellari-pwa-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/static/logo.png'
];

// Install event
self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('PWA: Opened cache');
                return cache.addAll(ASSETS_TO_CACHE);
            })
    );
});

// Activate event - cleanup old caches
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('PWA: Clearing old cache');
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    return self.clients.claim();
});

// Fetch event
self.addEventListener('fetch', event => {
    // Skip cross-origin requests
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }

    // Ignore admin routes and API calls
    if (event.request.url.includes('/admin/') || event.request.method !== 'GET') {
        return;
    }

    // For HTML requests, try network first, then cache
    if (event.request.mode === 'navigate') {
        event.respondWith(
            fetch(event.request)
                .catch(() => {
                    return caches.match(event.request)
                        .then(response => {
                            if (response) {
                                return response;
                            }
                            // Fallback to home page if offline and page not cached
                            return caches.match('/');
                        });
                })
        );
        return;
    }

    // For other assets, try cache first, then network
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    return response;
                }
                return fetch(event.request).then(response => {
                    // Optional: Cache new resources dynamically?
                    // For now, keep it simple and safe.
                    return response;
                });
            })
    );
});
