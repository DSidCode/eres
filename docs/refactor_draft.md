# CSS to add
```css
/* WELCOME OVERLAY */
#welcomeOverlay {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  background: rgba(5, 7, 17, 0.85);
  backdrop-filter: blur(10px);
  z-index: 9999;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: opacity 1s ease, transform 1s ease;
}
.welcome-title {
  font-family: var(--font-title);
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 900;
  color: #fff;
  letter-spacing: 4px;
  text-shadow: 0 0 20px rgba(251, 191, 36, 0.5);
  margin-bottom: 1rem;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeUp 1.5s ease forwards 0.5s;
}
.welcome-subtitle {
  font-family: var(--font-title);
  font-size: clamp(1rem, 3vw, 1.5rem);
  color: var(--accent-gold);
  font-style: italic;
  margin-bottom: 3rem;
  opacity: 0;
  animation: fadeIn 2s ease forwards 1.5s;
}
.btn-enter {
  background: linear-gradient(135deg, rgba(251, 191, 36, 0.2), rgba(244, 114, 182, 0.2));
  border: 1px solid var(--accent-gold);
  color: #fef08a;
  padding: 1rem 2.5rem;
  border-radius: 999px;
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  transition: all 0.4s ease;
  box-shadow: 0 0 20px rgba(251, 191, 36, 0.2);
  opacity: 0;
  animation: fadeIn 2s ease forwards 2.5s;
}
.btn-enter:hover {
  background: linear-gradient(135deg, rgba(251, 191, 36, 0.4), rgba(244, 114, 182, 0.4));
  box-shadow: 0 0 30px rgba(251, 191, 36, 0.6);
  transform: scale(1.05);
  color: #fff;
}
@keyframes fadeUp {
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  to { opacity: 1; }
}
.content-hidden {
  opacity: 0;
  pointer-events: none;
}

/* TOP NAVIGATION */
.top-nav {
  position: sticky;
  top: 10px;
  z-index: 100;
  background: rgba(13, 19, 36, 0.7);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 0.5rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.top-nav .tab-btn {
  background: transparent;
  border: none;
  padding: 0.75rem 1.25rem;
  border-radius: 14px;
  font-size: 0.9rem;
}
.top-nav .tab-btn.active {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid var(--accent-gold);
  box-shadow: none;
}
```
