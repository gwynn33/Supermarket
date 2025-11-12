// Navigation between pages
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const pages = document.querySelectorAll('.page');
    
    // Main navigation
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Hide all pages
            pages.forEach(page => page.classList.remove('active'));
            
            // Show corresponding page
            const pageId = this.getAttribute('data-page');
            document.getElementById(pageId).classList.add('active');
        });
    });
    
    // Simulate data updates for charts (to be replaced with Python/Matplotlib data)
    simulateDataUpdates();
    
    function simulateDataUpdates() {
        // This function simulates data updates
        // In a real case, it would be replaced by Python API calls
        setInterval(() => {
            // Simulate data card updates
            const dataValues = document.querySelectorAll('.data-value');
            dataValues.forEach(value => {
                if (value.textContent.includes('MAD')) {
                    const current = parseInt(value.textContent.replace(/[^0-9]/g, ''));
                    const change = Math.floor(Math.random() * 1000) - 500;
                    const newValue = Math.max(1000, current + change);
                    value.textContent = newValue.toLocaleString() + ' MAD';
                } else if (!isNaN(parseInt(value.textContent))) {
                    const current = parseInt(value.textContent);
                    const change = Math.floor(Math.random() * 20) - 10;
                    const newValue = Math.max(1, current + change);
                    value.textContent = newValue.toLocaleString();
                }
            });
        }, 10000);
    }
});