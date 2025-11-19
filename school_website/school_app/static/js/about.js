// ========================================
// ABOUT PAGE 2025 - NEXT LEVEL JS (FIXED)
// Counter + Parallax + Smooth Performance
// ========================================

document.addEventListener("DOMContentLoaded", function () {

    // ===== COUNTER ANIMATION - FIXED & SMOOTH =====
    const counters = document.querySelectorAll('.counter');
    let counterStarted = false;

    const startCounter = () => {
        if (counterStarted) return;
        counterStarted = true;

        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2500; // 2.5 seconds animation
            const startTime = performance.now();

            const updateCounter = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const currentCount = Math.floor(progress * target);

                counter.innerText = currentCount + (target === 100 ? '%' : '+');

                if (progress < 1) {
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.innerText = target + (target === 100 ? '%' : '+');
                }
            };

            requestAnimationFrame(updateCounter);
        });
    };

    // Trigger counter when stats section is in view
    const statsSection = document.querySelector('.stats-row') || document.querySelector('.about-content');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startCounter();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        observer.observe(statsSection);
    }

    // ===== PARALLAX EFFECT - SMOOTH & FIXED =====
    const parallaxHero = document.querySelector('.about-hero.parallax');
    if (parallaxHero) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            parallaxHero.style.backgroundPositionY = rate + 'px';
        });
    }

    // ===== EXTRA: Smooth reveal on scroll for cards =====
    const revealElements = document.querySelectorAll('.glass-card, .principal-message, .feature-card');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(50px)';
        el.style.transition = 'all 0.8s ease';
        revealObserver.observe(el);
    });
});