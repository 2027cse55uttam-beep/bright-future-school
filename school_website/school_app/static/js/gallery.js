// GALLERY PAGE 2025 - NEXT LEVEL JS
document.addEventListener('DOMContentLoaded', function () {

    // Lightbox Premium Settings
    lightbox.option({
        resizeDuration: 500,
        wrapAround: true,
        disableScrolling: false,
        fitImagesInViewport: true,
        positionFromTop: 100,
        albumLabel: "Image %1 of %2"
    });

    // Staggered Masonry Reveal
    const items = document.querySelectorAll('.gallery-item');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 80);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    items.forEach(item => observer.observe(item));

    // Parallax Hero
    window.addEventListener('scroll', () => {
        const hero = document.querySelector('.gallery-hero');
        if (hero) {
            const scrolled = window.pageYOffset;
            hero.style.backgroundPositionY = scrolled * 0.5 + 'px';
        }
    });
});