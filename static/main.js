let shuttingDown = false;
let connecting = false;

function shutdownApp() {
    shuttingDown = true;
}

function connectApp() {
                connecting = true;
}

function markSafeExit() {
                document.cookie = "safeExit=true; path=/";
}

window.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden' && !shuttingDown && !connecting) {
        if (!document.cookie.includes("safeExit=true")) {
            navigator.sendBeacon('/shutdown');
        }
    }
});

window.addEventListener('load', function () {
    // After the page reloads, reset safeExit
    document.cookie = "safeExit=false; path=/";
});

function printPage() {
    window.print();
}

function hideOverlay() {
    const overlay = document.getElementById('loginOverlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}

function showLoading() {
    const loginBox = document.getElementById('loginBox');
    const loadingBox = document.getElementById('loadingBox');
    if (loginBox && loadingBox) {
        loginBox.style.display = 'none';
        loadingBox.style.display = 'flex';
    }
}