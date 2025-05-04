document.addEventListener('DOMContentLoaded', () => {
    const carousel = new bootstrap.Carousel(document.getElementById('productCarousel'), {
        interval: 5000, // 5 seconds
        pause: 'hover'
    });
});