document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector('#navbar-main');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile menu close on click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            const collapse = document.querySelector('#navbar-collapse');
            if (collapse.classList.contains('show')) {
                new bootstrap.Collapse(collapse).hide();
            }
        });
    });
});