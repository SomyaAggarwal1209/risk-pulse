document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.nav_item');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            alert(`Navigating to ${item.textContent}`);
        });
    });
});
