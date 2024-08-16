document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password') ? document.getElementById('confirm-password').value : '';

            if (confirmPassword && password !== confirmPassword) {
                alert('Passwords do not match!');
                event.preventDefault();
            }
        });
    }
});
