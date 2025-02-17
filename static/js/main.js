// Theme Switcher Functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');

    // Load the previously selected theme from localStorage, if any
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.classList.add(savedTheme);
        if (savedTheme === 'dark-mode') {
            themeToggle.checked = true;
        } else if (savedTheme === 'blue-mode') {
            themeToggle.checked = true;
        }
    }

    // Switch theme on toggle change
    themeToggle.addEventListener('change', function() {
        // Remove existing theme classes
        document.body.classList.remove('light-mode', 'dark-mode', 'blue-mode');

        // Apply the selected theme
        if (themeToggle.checked) {
            // If the checkbox is checked, apply dark-mode
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
        } else {
            // Otherwise, apply light-mode
            document.body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
        }
    });
});
