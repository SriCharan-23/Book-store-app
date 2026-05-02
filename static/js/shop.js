/**
 * shop.js — Fetches books from /api/books and renders the shop grid.
 * Handles category filtering and Add to Cart interactions.
 */

(() => {
    const grid = document.getElementById('book-grid');
    const spinner = document.getElementById('loading-spinner');
    const filterBar = document.getElementById('filter-bar');
    let currentCategory = 'all';

    /* ── Fetch Books ── */
    async function fetchBooks(category) {
        if (!grid) return;
        grid.innerHTML = '<div class="loading-spinner" id="loading-spinner"><div class="spinner"></div><p>Loading books...</p></div>';

        const url = category && category !== 'all'
            ? `/api/books?category=${encodeURIComponent(category)}`
            : '/api/books';

        try {
            const res = await fetch(url);
            const books = await res.json();
            renderBooks(books);
        } catch (err) {
            grid.innerHTML = '<p class="error-msg">Failed to load books. Please try again.</p>';
            console.error('Fetch error:', err);
        }
    }

    /* ── Render Book Cards ── */
    function renderBooks(books) {
        if (!grid) return;

        if (books.length === 0) {
            grid.innerHTML = '<p class="empty-msg">No books found in this category.</p>';
            return;
        }

        grid.innerHTML = books.map((book, index) => `
            <article class="book-card" style="animation-delay: ${index * 0.05}s" id="book-${book.id}">
                <div class="book-card-image">
                    <img src="${book.cover_image}" alt="${book.title}" loading="lazy">
                    <span class="book-category-tag">${book.category}</span>
                </div>
                <div class="book-card-body">
                    <h3 class="book-title">${book.title}</h3>
                    <p class="book-author">by ${book.author}</p>
                    <p class="book-description">${book.description || ''}</p>
                    <div class="book-card-footer">
                        <span class="book-price">$${book.price.toFixed(2)}</span>
                        <button class="btn btn-add-cart" onclick="Cart.addToCart(${JSON.stringify(book).replace(/"/g, '&quot;')})" id="add-cart-${book.id}">
                            <span class="btn-icon">🛒</span> Add to Cart
                        </button>
                    </div>
                </div>
            </article>
        `).join('');
    }

    /* ── Category Filter Clicks ── */
    if (filterBar) {
        filterBar.addEventListener('click', (e) => {
            const btn = e.target.closest('.filter-btn');
            if (!btn) return;

            // Update active state
            filterBar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            currentCategory = btn.dataset.category;
            fetchBooks(currentCategory);
        });
    }

    /* ── Check URL params for initial category ── */
    function init() {
        const params = new URLSearchParams(window.location.search);
        const catParam = params.get('category');
        if (catParam) {
            currentCategory = catParam;
            // Activate the matching filter button
            const matchBtn = filterBar?.querySelector(`[data-category="${catParam}"]`);
            if (matchBtn) {
                filterBar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                matchBtn.classList.add('active');
            }
        }
        fetchBooks(currentCategory);
    }

    document.addEventListener('DOMContentLoaded', init);
})();
