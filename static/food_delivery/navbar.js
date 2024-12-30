document.addEventListener("DOMContentLoaded", () => {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;

    // Check local storage for dark mode preference
    const darkModeEnabled = localStorage.getItem("dark-mode") === "enabled";

    // Apply dark mode if previously enabled
    if (darkModeEnabled) {
        body.classList.add("dark-mode");
        darkModeToggle.textContent = "☀️"; // Update icon to sun
    }

    // Add click event listener to toggle button
    darkModeToggle.addEventListener("click", () => {
        const isDarkMode = body.classList.toggle("dark-mode");

        // Update local storage and toggle icon
        if (isDarkMode) {
            localStorage.setItem("dark-mode", "enabled");
            darkModeToggle.textContent = "☀️"; // Sun icon for light mode
        } else {
            localStorage.setItem("dark-mode", "disabled");
            darkModeToggle.textContent = "🌙"; // Moon icon for dark mode
        }
    });
});
