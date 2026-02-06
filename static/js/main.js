/**
 * SAMERA Architecture Portfolio
 * Main JavaScript - Animations & Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all components
    initPreloader();
    initCustomCursor();
    initNavigation();
    initHeroSlider();
    initScrollAnimations();
    initProjectFilter();
    initProjectModal();
    initCounterAnimation();
    initSmoothScroll();
    initContactForm();
});

/**
 * Preloader
 */
function initPreloader() {
    const preloader = document.getElementById('preloader');

    window.addEventListener('load', () => {
        setTimeout(() => {
            preloader.classList.add('hidden');
            document.body.style.overflow = 'visible';

            // Trigger initial animations after preloader
            triggerHeroAnimations();
        }, 1500);
    });
}

/**
 * Custom Cursor
 */
function initCustomCursor() {
    const cursor = document.getElementById('cursor');
    const follower = document.getElementById('cursor-follower');

    if (!cursor || !follower) return;

    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    let followerX = 0, followerY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // Smooth cursor animation
    function animateCursor() {
        // Cursor follows immediately
        cursorX += (mouseX - cursorX) * 0.5;
        cursorY += (mouseY - cursorY) * 0.5;
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';

        // Follower has delay
        followerX += (mouseX - followerX) * 0.15;
        followerY += (mouseY - followerY) * 0.15;
        follower.style.left = followerX + 'px';
        follower.style.top = followerY + 'px';

        requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Cursor hover effects
    const hoverElements = document.querySelectorAll('a, button, .project-card');
    hoverElements.forEach(el => {
        el.addEventListener('mouseenter', () => follower.classList.add('active'));
        el.addEventListener('mouseleave', () => follower.classList.remove('active'));
    });
}

/**
 * Navigation
 */
function initNavigation() {
    const nav = document.getElementById('nav');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Scroll effect
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;

        if (currentScroll > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Mobile menu toggle
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });

    // Close menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

/**
 * Hero Slider
 */
function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dot');
    let currentSlide = 0;
    let slideInterval;

    if (slides.length <= 1) return;

    function goToSlide(index) {
        slides[currentSlide].classList.remove('active');
        dots[currentSlide].classList.remove('active');

        currentSlide = index;
        if (currentSlide >= slides.length) currentSlide = 0;
        if (currentSlide < 0) currentSlide = slides.length - 1;

        slides[currentSlide].classList.add('active');
        dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        goToSlide(currentSlide + 1);
    }

    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, 6000);
    }

    function stopAutoSlide() {
        clearInterval(slideInterval);
    }

    // Dot navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            stopAutoSlide();
            goToSlide(index);
            startAutoSlide();
        });
    });

    startAutoSlide();
}

/**
 * Trigger Hero Animations
 */
function triggerHeroAnimations() {
    const heroElements = document.querySelectorAll('.hero .reveal-text');
    heroElements.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('revealed');
        }, index * 150);
    });
}

/**
 * Scroll Animations (Intersection Observer)
 */
function initScrollAnimations() {
    const revealElements = document.querySelectorAll('.reveal-text:not(.hero .reveal-text)');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealElements.forEach(el => observer.observe(el));
}

/**
 * Project Filter
 */
function initProjectFilter() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active button
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;

            // Filter projects with animation
            projectCards.forEach(card => {
                const category = card.dataset.category;

                if (filter === 'all' || category === filter) {
                    card.classList.remove('hidden');
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';

                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';

                    setTimeout(() => {
                        card.classList.add('hidden');
                    }, 300);
                }
            });
        });
    });
}

/**
 * Project Modal
 */
function initProjectModal() {
    const modal = document.getElementById('project-modal');
    const modalClose = modal.querySelector('.modal-close');
    const modalImage = modal.querySelector('.modal-image');
    const modalCategory = modal.querySelector('.modal-category');
    const modalTitle = modal.querySelector('.modal-title');
    const modalDescription = modal.querySelector('.modal-description');
    const modalLocation = modal.querySelector('.modal-location');
    const modalYear = modal.querySelector('.modal-year');

    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        card.addEventListener('click', () => {
            const image = card.querySelector('.project-image').src;
            const category = card.querySelector('.project-category').textContent;
            const title = card.querySelector('.project-title').textContent;
            const location = card.querySelector('.project-location').textContent;
            const year = card.querySelector('.project-year').textContent;

            modalImage.innerHTML = `<img src="${image}" alt="${title}">`;
            modalCategory.textContent = category;
            modalTitle.textContent = title;
            modalDescription.textContent = `A stunning ${category.toLowerCase()} project located in ${location}, completed in ${year}.`;
            modalLocation.textContent = location;
            modalYear.textContent = year;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    // Close modal
    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

/**
 * Counter Animation
 */
function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-number');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    counters.forEach(counter => observer.observe(counter));

    function animateCounter(element) {
        const target = parseInt(element.dataset.count);
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        function update() {
            current += step;
            if (current < target) {
                element.textContent = Math.floor(current);
                requestAnimationFrame(update);
            } else {
                element.textContent = target;
            }
        }

        update();
    }
}

/**
 * Smooth Scroll
 */
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const headerHeight = 80;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Contact Form
 */
function initContactForm() {
    const form = document.getElementById('contact-form');

    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        // Simulate form submission
        const submitBtn = form.querySelector('.form-submit');
        const originalText = submitBtn.innerHTML;

        submitBtn.innerHTML = '<span>Sending...</span>';
        submitBtn.disabled = true;

        setTimeout(() => {
            submitBtn.innerHTML = '<span>Message Sent!</span>';
            submitBtn.style.background = '#2ecc71';

            form.reset();

            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.style.background = '';
                submitBtn.disabled = false;
            }, 2000);
        }, 1500);
    });
}

/**
 * Parallax Effect (Optional - Performance Optimized)
 */
function initParallax() {
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    if (parallaxElements.length === 0) return;

    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrolled = window.scrollY;

                parallaxElements.forEach(el => {
                    const speed = parseFloat(el.dataset.parallax) || 0.5;
                    const yPos = -(scrolled * speed);
                    el.style.transform = `translateY(${yPos}px)`;
                });

                ticking = false;
            });

            ticking = true;
        }
    });
}

/**
 * Add transition styles to project cards
 */
document.querySelectorAll('.project-card').forEach(card => {
    card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
});
