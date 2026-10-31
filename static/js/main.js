// 1. Copy Email Functionality
function copyEmail() {
  const email = "hello@mohamedbelali.com";
  const toast = document.getElementById('toast');
  const lang = document.documentElement.lang;
  const msg = lang === 'ar' ? "تم نسخ البريد الإلكتروني." : "Email copied to clipboard.";

  navigator.clipboard.writeText(email).then(() => {
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => { toast.classList.remove('show'); }, 3000);
  }).catch(err => console.error('Failed to copy: ', err));
}

// 2. Scroll Reveals (Intersection Observer)
document.addEventListener("DOMContentLoaded", () => {
  // Check for reduced motion preference
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  
  if (!prefersReducedMotion) {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15 // Trigger when 15% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target); // Reveal only once
        }
      });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
      observer.observe(el);
    });
  } else {
    // If reduced motion is preferred, show all immediately
    document.querySelectorAll('.reveal').forEach(el => {
      el.classList.add('is-visible');
    });
  }
});
