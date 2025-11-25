const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

hamburger.addEventListener('click', function() {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    document.body.classList.toggle('menu-open');
});

// Arrow scroll to about section with smooth easing
const heroArrow = document.querySelector('.hero-arrow');
if (heroArrow) {
    heroArrow.addEventListener('click', function() {
        const aboutSection = document.getElementById('about');
        if (aboutSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = aboutSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// News hero arrow scroll to news content
const newsHeroArrow = document.querySelector('.news-hero-arrow');
if (newsHeroArrow) {
    newsHeroArrow.addEventListener('click', function() {
        const newsContentSection = document.getElementById('news-content');
        if (newsContentSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = newsContentSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// Partners hero arrow scroll to partners content
const partnersHeroArrow = document.querySelector('.partners-hero-arrow');
if (partnersHeroArrow) {
    partnersHeroArrow.addEventListener('click', function() {
        const partnersContentSection = document.getElementById('partners-content');
        if (partnersContentSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = partnersContentSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// Contacts hero arrow scroll to contacts content
const contactsHeroArrow = document.querySelector('.contacts-hero-arrow');
if (contactsHeroArrow) {
    contactsHeroArrow.addEventListener('click', function() {
        const contactsContentSection = document.getElementById('contacts-content');
        if (contactsContentSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = contactsContentSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// History line hero arrow scroll to history line content
const historyLineArrow = document.querySelector('.history-line-arrow');
if (historyLineArrow) {
    historyLineArrow.addEventListener('click', function() {
        const historyLineContentSection = document.getElementById('history-line-content');
        if (historyLineContentSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = historyLineContentSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// History line CTA button scroll to history line content
const historyLineCta = document.querySelector('.history-line-cta');
if (historyLineCta) {
    historyLineCta.addEventListener('click', function(e) {
        e.preventDefault();
        const historyLineContentSection = document.getElementById('history-line-content');
        if (historyLineContentSection) {
            const headerHeight = document.getElementById('header').offsetHeight;
            const targetPosition = historyLineContentSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// News pagination functionality
const paginationNumbers = document.querySelectorAll('.pagination-number');
const newsItems = document.querySelectorAll('.news-item');
const newsGrid = document.querySelector('.news-grid');

if (paginationNumbers.length > 0 && newsGrid) {
    paginationNumbers.forEach(function(paginationNumber) {
        paginationNumber.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetPage = this.getAttribute('data-page');
            
            // Remove active class from all pagination numbers
            paginationNumbers.forEach(function(num) {
                num.classList.remove('active');
            });
            
            // Add active class to clicked pagination number
            this.classList.add('active');
            
            // Hide all news items
            newsItems.forEach(function(item) {
                item.classList.remove('show');
                item.style.display = 'none';
            });
            
            // Show news items for selected page
            newsItems.forEach(function(item) {
                if (item.getAttribute('data-page') === targetPage) {
                    item.style.display = 'block';
                    item.classList.add('show');
                }
            });
            
            // Scroll to news grid
            const headerHeight = document.getElementById('header') ? document.getElementById('header').offsetHeight : 0;
            const gridPosition = newsGrid.offsetTop - headerHeight - 20;
            
            window.scrollTo({
                top: gridPosition,
                behavior: 'smooth'
            });
        });
    });
}

