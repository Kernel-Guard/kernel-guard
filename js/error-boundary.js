/**
 * KernelGuard Global Error Boundary
 * ----------------------------------
 * Catches uncaught JS errors and unhandled promise rejections,
 * displays a professional recovery screen, detects crash loops,
 * and provides a Report & Restart mechanism.
 *
 * Integration: Sentry-ready — uncomment the Sentry.captureException()
 * calls and add the Sentry SDK script to go live with crash reporting.
 */

(function () {
    const CRASH_STORAGE_KEY = 'kg-crash-count';
    const CRASH_TIME_KEY = 'kg-crash-time';
    const CRASH_LOOP_THRESHOLD = 3;       // crashes within window = loop
    const CRASH_LOOP_WINDOW_MS = 30000;   // 30 second window

    // ── Crash Loop Detection ──
    function getCrashCount() {
        const lastTime = parseInt(sessionStorage.getItem(CRASH_TIME_KEY) || '0', 10);
        const count = parseInt(sessionStorage.getItem(CRASH_STORAGE_KEY) || '0', 10);
        // Reset if outside the crash window
        if (Date.now() - lastTime > CRASH_LOOP_WINDOW_MS) return 0;
        return count;
    }

    function incrementCrashCount() {
        const count = getCrashCount() + 1;
        sessionStorage.setItem(CRASH_STORAGE_KEY, count.toString());
        sessionStorage.setItem(CRASH_TIME_KEY, Date.now().toString());
        return count;
    }

    function resetCrashCount() {
        sessionStorage.removeItem(CRASH_STORAGE_KEY);
        sessionStorage.removeItem(CRASH_TIME_KEY);
    }

    // ── Recovery Screen ──
    function showRecoveryScreen(error, source) {
        const crashCount = incrementCrashCount();
        const isLoop = crashCount >= CRASH_LOOP_THRESHOLD;

        // Report to Sentry (uncomment when SDK is added)
        // if (typeof Sentry !== 'undefined') {
        //     Sentry.captureException(error, { tags: { source: source } });
        // }

        const errorName = error?.name || 'Error';
        const errorMessage = error?.message || 'An unexpected error occurred.';
        const errorStack = error?.stack || 'No stack trace available.';
        const timestamp = new Date().toISOString();

        // Remove existing overlay if present
        const existing = document.getElementById('kg-error-boundary');
        if (existing) existing.remove();

        const overlay = document.createElement('div');
        overlay.id = 'kg-error-boundary';
        overlay.innerHTML = `
            <style>
                #kg-error-boundary {
                    position: fixed;
                    inset: 0;
                    z-index: 99999;
                    background: #0D1117;
                    color: #E6EDF3;
                    font-family: 'IBM Plex Sans', -apple-system, sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 32px;
                    animation: kgFadeIn 0.3s ease;
                }
                @keyframes kgFadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                .kg-err-container {
                    max-width: 560px;
                    width: 100%;
                }
                .kg-err-icon {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 64px;
                    height: 64px;
                    background: #21262D;
                    border: 1px solid #30363D;
                    margin-bottom: 32px;
                }
                .kg-err-title {
                    font-size: 28px;
                    font-weight: 300;
                    margin-bottom: 12px;
                    letter-spacing: -0.3px;
                }
                .kg-err-desc {
                    font-size: 15px;
                    color: #8B949E;
                    line-height: 1.6;
                    margin-bottom: 32px;
                }
                .kg-err-loop-warning {
                    background: #2A1500;
                    border-left: 3px solid #FF832B;
                    padding: 12px 16px;
                    font-size: 13px;
                    color: #FF832B;
                    margin-bottom: 24px;
                    display: ${isLoop ? 'block' : 'none'};
                }
                .kg-err-actions {
                    display: flex;
                    gap: 12px;
                    margin-bottom: 32px;
                }
                .kg-err-btn {
                    padding: 12px 24px;
                    font-size: 14px;
                    font-family: inherit;
                    cursor: pointer;
                    border: none;
                    transition: background 0.15s;
                }
                .kg-err-btn-primary {
                    background: #0043CE;
                    color: #fff;
                }
                .kg-err-btn-primary:hover {
                    background: #0353E9;
                }
                .kg-err-btn-secondary {
                    background: #21262D;
                    color: #E6EDF3;
                    border: 1px solid #30363D;
                }
                .kg-err-btn-secondary:hover {
                    background: #30363D;
                }
                .kg-err-details-toggle {
                    font-size: 12px;
                    font-family: 'IBM Plex Mono', monospace;
                    color: #8B949E;
                    background: none;
                    border: none;
                    cursor: pointer;
                    padding: 0;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    margin-bottom: 12px;
                }
                .kg-err-details-toggle:hover {
                    color: #E6EDF3;
                }
                .kg-err-details-toggle .chevron {
                    transition: transform 0.2s;
                }
                .kg-err-details-toggle.open .chevron {
                    transform: rotate(90deg);
                }
                .kg-err-details {
                    display: none;
                    background: #010409;
                    border: 1px solid #30363D;
                    padding: 16px;
                    font-family: 'IBM Plex Mono', monospace;
                    font-size: 11px;
                    color: #8B949E;
                    line-height: 1.6;
                    max-height: 200px;
                    overflow-y: auto;
                    white-space: pre-wrap;
                    word-break: break-all;
                }
                .kg-err-details.open {
                    display: block;
                }
                .kg-err-meta {
                    font-size: 11px;
                    color: #6E7681;
                    font-family: 'IBM Plex Mono', monospace;
                    margin-top: 24px;
                    padding-top: 16px;
                    border-top: 1px solid #21262D;
                }
            </style>
            <div class="kg-err-container">
                <div class="kg-err-icon">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#FF8389" stroke-width="1.5">
                        <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/>
                        <line x1="12" y1="9" x2="12" y2="13"/>
                        <line x1="12" y1="17" x2="12.01" y2="17"/>
                    </svg>
                </div>
                
                <h1 class="kg-err-title">Something went wrong</h1>
                <p class="kg-err-desc">
                    An unexpected runtime error has occurred. This incident has been logged. 
                    You can try reloading the page, or if the issue persists, use "Report & Restart" 
                    to clear the application cache and recover.
                </p>

                <div class="kg-err-loop-warning">
                    ⚠ Crash loop detected (${crashCount} errors in ${CRASH_LOOP_WINDOW_MS / 1000}s). 
                    Application cache will be cleared automatically on restart.
                </div>

                <div class="kg-err-actions">
                    <button class="kg-err-btn kg-err-btn-primary" id="kg-err-restart">
                        ${isLoop ? '🔄 Clear Cache & Restart' : '↻ Reload Page'}
                    </button>
                    <button class="kg-err-btn kg-err-btn-secondary" id="kg-err-report">
                        Report & Restart
                    </button>
                </div>

                <button class="kg-err-details-toggle" id="kg-err-toggle">
                    <svg class="chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
                    Technical Details
                </button>
                <div class="kg-err-details" id="kg-err-details-panel">Error Type:    ${errorName}
Source:        ${source}
Message:       ${errorMessage}
Timestamp:     ${timestamp}
User Agent:    ${navigator.userAgent}
URL:           ${window.location.href}
Crash Count:   ${crashCount}

─── Stack Trace ───
${errorStack}</div>

                <div class="kg-err-meta">
                    KernelGuard Error Boundary v1.0 · Incident ID: ${Date.now().toString(36).toUpperCase()}
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        // Toggle technical details
        document.getElementById('kg-err-toggle').addEventListener('click', function () {
            this.classList.toggle('open');
            document.getElementById('kg-err-details-panel').classList.toggle('open');
        });

        // Reload button
        document.getElementById('kg-err-restart').addEventListener('click', function () {
            if (isLoop) {
                clearCacheAndRestart();
            } else {
                window.location.reload();
            }
        });

        // Report & Restart button
        document.getElementById('kg-err-report').addEventListener('click', function () {
            // Report to Sentry before restarting
            // if (typeof Sentry !== 'undefined') {
            //     Sentry.captureException(error, {
            //         tags: { source: source, crashCount: crashCount },
            //         extra: { userAgent: navigator.userAgent, url: window.location.href }
            //     });
            // }
            console.log('[KernelGuard] Error report submitted:', {
                error: errorName,
                message: errorMessage,
                stack: errorStack,
                timestamp: timestamp,
                crashCount: crashCount
            });
            clearCacheAndRestart();
        });
    }

    // ── Clear Cache & Restart ──
    function clearCacheAndRestart() {
        // Clear all storage
        resetCrashCount();
        localStorage.clear();
        sessionStorage.clear();

        // Clear service worker caches if available
        if ('caches' in window) {
            caches.keys().then(function (names) {
                for (var name of names) {
                    caches.delete(name);
                }
            });
        }

        // Unregister service workers
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.getRegistrations().then(function (registrations) {
                for (var reg of registrations) {
                    reg.unregister();
                }
            });
        }

        // Reload after a brief delay to let cleanup finish
        setTimeout(function () {
            window.location.reload();
        }, 300);
    }

    // ── Global Error Handlers ──

    // Catch synchronous errors
    window.onerror = function (message, source, lineno, colno, error) {
        showRecoveryScreen(
            error || new Error(message),
            'window.onerror · ' + (source || 'unknown') + ':' + lineno + ':' + colno
        );
        return true; // Prevent default browser error handling
    };

    // Catch unhandled promise rejections
    window.addEventListener('unhandledrejection', function (event) {
        const error = event.reason instanceof Error
            ? event.reason
            : new Error(String(event.reason));
        showRecoveryScreen(error, 'Unhandled Promise Rejection');
        event.preventDefault();
    });

    // Reset crash count on successful page load (no error within 5s = stable)
    window.addEventListener('load', function () {
        setTimeout(function () {
            resetCrashCount();
        }, 5000);
    });

    console.log('[KernelGuard] Error Boundary active.');
})();
