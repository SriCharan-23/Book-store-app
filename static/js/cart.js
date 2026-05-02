/**
 * cart.js — Persistent shopping cart using localStorage
 * Manages cart state, UI updates, and the slide-in cart sidebar.
 */

const Cart = (() => {
    const STORAGE_KEY = 'pageturn_cart';

    /* ── State ── */
    function getCart() {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
        } catch {
            return [];
        }
    }

    function saveCart(cart) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
        updateBadge();
        renderCartSidebar();
    }

    /* ── Cart Operations ── */
    function addToCart(book) {
        const cart = getCart();
        const existing = cart.find(item => item.id === book.id);
        if (existing) {
            existing.quantity += 1;
        } else {
            cart.push({ ...book, quantity: 1 });
        }
        saveCart(cart);
        showAddedFeedback(book.title);
    }

    function removeFromCart(bookId) {
        let cart = getCart();
        cart = cart.filter(item => item.id !== bookId);
        saveCart(cart);
    }

    function updateQuantity(bookId, delta) {
        const cart = getCart();
        const item = cart.find(i => i.id === bookId);
        if (item) {
            item.quantity += delta;
            if (item.quantity <= 0) {
                removeFromCart(bookId);
                return;
            }
        }
        saveCart(cart);
    }

    function clearCart() {
        localStorage.removeItem(STORAGE_KEY);
        updateBadge();
        renderCartSidebar();
    }

    function getCartCount() {
        return getCart().reduce((sum, item) => sum + item.quantity, 0);
    }

    function getCartTotal() {
        return getCart().reduce((sum, item) => sum + item.price * item.quantity, 0);
    }

    /* ── UI: Badge ── */
    function updateBadge() {
        const badge = document.getElementById('cart-badge');
        if (badge) {
            const count = getCartCount();
            badge.textContent = count;
            badge.classList.toggle('has-items', count > 0);
            // Pulse animation
            badge.classList.remove('pulse');
            void badge.offsetWidth; // Trigger reflow
            badge.classList.add('pulse');
        }
    }

    /* ── UI: Added Feedback ── */
    function showAddedFeedback(title) {
        const toast = document.createElement('div');
        toast.className = 'cart-toast';
        toast.innerHTML = `<span class="toast-icon">✓</span> <strong>${title}</strong> added to cart`;
        document.body.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('show'));
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 2000);
    }

    /* ── UI: Sidebar Render ── */
    function renderCartSidebar() {
        const container = document.getElementById('cart-items');
        const footer = document.getElementById('cart-footer');
        const totalEl = document.getElementById('cart-total-price');
        if (!container) return;

        const cart = getCart();

        if (cart.length === 0) {
            container.innerHTML = `
                <div class="cart-empty">
                    <div class="cart-empty-icon">🛒</div>
                    <p>Your cart is empty</p>
                    <a href="/" class="btn btn-outline">Start Shopping</a>
                </div>`;
            if (footer) footer.style.display = 'none';
            return;
        }

        if (footer) footer.style.display = 'block';

        container.innerHTML = cart.map(item => `
            <div class="cart-item" data-id="${item.id}">
                <img src="${item.cover_image}" alt="${item.title}" class="cart-item-img">
                <div class="cart-item-details">
                    <h4 class="cart-item-title">${item.title}</h4>
                    <p class="cart-item-author">${item.author}</p>
                    <p class="cart-item-price">$${item.price.toFixed(2)}</p>
                    <div class="cart-item-qty">
                        <button class="qty-btn" onclick="Cart.updateQuantity(${item.id}, -1)">−</button>
                        <span>${item.quantity}</span>
                        <button class="qty-btn" onclick="Cart.updateQuantity(${item.id}, 1)">+</button>
                    </div>
                </div>
                <button class="cart-item-remove" onclick="Cart.removeFromCart(${item.id})" aria-label="Remove item">&times;</button>
            </div>
        `).join('');

        if (totalEl) totalEl.textContent = `$${getCartTotal().toFixed(2)}`;
    }

    /* ── Sidebar Toggle ── */
    function openSidebar() {
        document.getElementById('cart-sidebar')?.classList.add('open');
        document.getElementById('cart-overlay')?.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeSidebar() {
        document.getElementById('cart-sidebar')?.classList.remove('open');
        document.getElementById('cart-overlay')?.classList.remove('open');
        document.body.style.overflow = '';
    }

    /* ── Init ── */
    function init() {
        updateBadge();
        renderCartSidebar();

        document.getElementById('cart-button')?.addEventListener('click', openSidebar);
        document.getElementById('cart-close')?.addEventListener('click', closeSidebar);
        document.getElementById('cart-overlay')?.addEventListener('click', closeSidebar);

        document.getElementById('cart-checkout-btn')?.addEventListener('click', () => {
            alert('Checkout coming soon! Thank you for browsing PageTurn Books.');
        });
    }

    document.addEventListener('DOMContentLoaded', init);

    // Public API
    return { addToCart, removeFromCart, updateQuantity, clearCart, getCart, getCartCount, getCartTotal };
})();
