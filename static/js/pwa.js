// PWA Registration and Install Logic
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/sw.js')
            .then(registration => {
                console.log('PWA: SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('PWA: SW registration failed: ', registrationError);
            });
    });
}

let deferredPrompt;
const installPrompt = document.getElementById('pwa-install-prompt');
const installBtn = document.getElementById('pwa-install-btn');
const closeBtn = document.getElementById('pwa-close-btn');
const iosPrompt = document.getElementById('pwa-ios-prompt');
const iosCloseBtn = document.getElementById('pwa-ios-close-btn');

// Check if iOS
const isIos = () => {
    const userAgent = window.navigator.userAgent.toLowerCase();
    return /iphone|ipad|ipod/.test(userAgent);
}

// Check if standalone
const isInStandaloneMode = () => ('standalone' in window.navigator) && (window.navigator.standalone);

if (isIos() && !isInStandaloneMode()) {
    // Show iOS instructions after a delay, maybe check local storage if already shown
    if (!localStorage.getItem('pwa_ios_prompt_shown')) {
        setTimeout(() => {
            if(iosPrompt) iosPrompt.classList.remove('hidden');
        }, 3000);
    }
}

if (iosCloseBtn) {
    iosCloseBtn.addEventListener('click', () => {
        iosPrompt.classList.add('hidden');
        localStorage.setItem('pwa_ios_prompt_shown', 'true');
    });
}

window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Update UI to notify the user they can add to home screen
    if (installPrompt) installPrompt.classList.remove('hidden');
});

if (installBtn) {
    installBtn.addEventListener('click', () => {
        // Hide our user interface that shows our A2HS button
        installPrompt.classList.add('hidden');
        // Show the prompt
        if (deferredPrompt) {
            deferredPrompt.prompt();
            // Wait for the user to respond to the prompt
            deferredPrompt.userChoice.then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('PWA: User accepted the A2HS prompt');
                } else {
                    console.log('PWA: User dismissed the A2HS prompt');
                }
                deferredPrompt = null;
            });
        }
    });
}

if (closeBtn) {
    closeBtn.addEventListener('click', () => {
        installPrompt.classList.add('hidden');
    });
}
