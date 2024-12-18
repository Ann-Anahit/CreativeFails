document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const dropdownButtons = document.querySelectorAll('.account-btn-container .button');

    // Toggle nav links visibility on hamburger click
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('open');
    });

    // Toggle dropdown menus
    dropdownButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const dropdown = button.nextElementSibling;
            dropdown.classList.toggle('active');
            e.stopPropagation();
        });
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', () => {
        const dropdowns = document.querySelectorAll('.account-btn-container .dropdown-content');
        dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
    });
});