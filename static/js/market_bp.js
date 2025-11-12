// Données des produits (simulation de base de données)
const productsData = [
    {
        "product_id": 8,
        "product_categorie": "Fruits",
        "product_name": "Pommes Golden",
        "product_description": "Pommes Golden fraîches et juteuses, idéales pour les desserts.",
        "product_price": 12,
        "current_stock_quantity": 180,
        "product_entering_date": "2024-11-01",
        "product_expiration_date": "2024-11-20"
    },
    {
        "product_id": 9,
        "product_categorie": "Fruits",
        "product_name": "Oranges Valencia",
        "product_description": "Oranges sucrées et pleines de vitamines, parfaites pour les jus.",
        "product_price": 8,
        "current_stock_quantity": 150,
        "product_entering_date": "2024-11-02",
        "product_expiration_date": "2024-11-15"
    },
    {
        "product_id": 10,
        "product_categorie": "Légumes",
        "product_name": "Carottes Bio",
        "product_description": "Carottes biologiques, croquantes et pleines de saveur.",
        "product_price": 6,
        "current_stock_quantity": 200,
        "product_entering_date": "2024-11-03",
        "product_expiration_date": "2024-11-25"
    },
    {
        "product_id": 11,
        "product_categorie": "Légumes",
        "product_name": "Tomates Cerises",
        "product_description": "Tomates cerises sucrées, parfaites pour les salades.",
        "product_price": 15,
        "current_stock_quantity": 120,
        "product_entering_date": "2024-11-04",
        "product_expiration_date": "2024-11-18"
    },
    {
        "product_id": 12,
        "product_categorie": "Produits Laitiers",
        "product_name": "Lait Entier",
        "product_description": "Lait entier frais, riche en calcium et protéines.",
        "product_price": 7,
        "current_stock_quantity": 90,
        "product_entering_date": "2024-11-05",
        "product_expiration_date": "2024-11-12"
    },
    {
        "product_id": 13,
        "product_categorie": "Produits Laitiers",
        "product_name": "Yaourt Nature",
        "product_description": "Yaourt nature crémeux, excellent pour la santé digestive.",
        "product_price": 4,
        "current_stock_quantity": 200,
        "product_entering_date": "2024-11-06",
        "product_expiration_date": "2024-11-20"
    },
    {
        "product_id": 14,
        "product_categorie": "Épicerie",
        "product_name": "Huile d'Olive Extra Vierge",
        "product_description": "Huile d'olive de première qualité, pressée à froid.",
        "product_price": 45,
        "current_stock_quantity": 80,
        "product_entering_date": "2024-11-01",
        "product_expiration_date": "2025-05-01"
    },
    {
        "product_id": 15,
        "product_categorie": "Épicerie",
        "product_name": "Miel Naturel",
        "product_description": "Miel 100% pur, récolté dans les montagnes de l'Atlas.",
        "product_price": 35,
        "current_stock_quantity": 60,
        "product_entering_date": "2024-10-28",
        "product_expiration_date": "2025-10-28"
    }
];

// Données des commandes (stockage local)
let ordersData = JSON.parse(localStorage.getItem('hormarket_orders')) || [];
let user_id = 1; // ID utilisateur simulé

// Panier (stockage local)
let cart = JSON.parse(localStorage.getItem('hormarket_cart')) || [];

// Navigation entre les pages
document.addEventListener('DOMContentLoaded', function() {
    const commandsLink = document.querySelector('.commands-link');
    const pages = document.querySelectorAll('.page');
    const cartToggle = document.getElementById('cart-toggle');
    const cartOverlay = document.getElementById('cart-overlay');
    const closeCart = document.getElementById('close-cart');
    const searchBtn = document.getElementById('search-btn');
    const categoryFilter = document.getElementById('category-filter');
    const sortFilter = document.getElementById('sort-filter');
    const checkoutBtnLarge = document.getElementById('checkout-btn-large');
    const closeReceiptBtn = document.getElementById('close-receipt');
    const currentPageTitle = document.getElementById('current-page-title');
    
    // Navigation via le lien "Mes Commandes"
    commandsLink.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Masquer toutes les pages
        pages.forEach(page => page.classList.remove('active'));
        
        // Afficher la page des commandes
        document.getElementById('commandes').classList.add('active');
        
        // Mettre à jour le titre de la page
        updatePageTitle('commandes');
        
        // Fermer le panier si ouvert
        cartOverlay.classList.remove('active');
        
        // Charger les commandes
        loadOrders();
    });

    // Retour à la page des produits quand on clique sur le titre
    currentPageTitle.addEventListener('click', function() {
        if (!document.getElementById('produits').classList.contains('active')) {
            // Masquer toutes les pages
            pages.forEach(page => page.classList.remove('active'));
            
            // Afficher la page des produits
            document.getElementById('produits').classList.add('active');
            
            // Mettre à jour le titre de la page
            updatePageTitle('produits');
            
            // Fermer le panier si ouvert
            cartOverlay.classList.remove('active');
        }
    });
    
    // Ouvrir le panier
    cartToggle.addEventListener('click', function() {
        cartOverlay.classList.add('active');
        updateCartModal();
    });
    
    // Fermer le panier
    closeCart.addEventListener('click', function() {
        cartOverlay.classList.remove('active');
    });
    
    // Recherche
    searchBtn.addEventListener('click', performSearch);
    
    // Recherche avec Entrée
    document.getElementById('search-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') performSearch();
    });
    
    // Filtres
    categoryFilter.addEventListener('change', loadProducts);
    sortFilter.addEventListener('change', loadProducts);
    
    // Confirmation d'achat depuis le modal
    checkoutBtnLarge.addEventListener('click', confirmPurchase);
    
    // Fermer le reçu
    closeReceiptBtn.addEventListener('click', function() {
        document.getElementById('receipt-overlay').classList.remove('active');
        // Recharger les commandes بعد إغلاق الإيصال
        if (document.getElementById('commandes').classList.contains('active')) {
            loadOrders();
        }
    });
    
    // Initialisation
    updateCartDisplay();
    loadProducts();
    loadOrders();
    
    // Fonction pour mettre à jour le titre de la page
    function updatePageTitle(pageId) {
        const titles = {
            'produits': 'Nos Produits',
            'commandes': 'Mes Commandes'
        };
        currentPageTitle.textContent = titles[pageId] || 'HorMarket';
        currentPageTitle.style.cursor = pageId === 'commandes' ? 'pointer' : 'default';
    }
    
    // Fonction pour effectuer la recherche
    function performSearch() {
        const searchTerm = document.getElementById('search-input').value.toLowerCase();
        loadProducts('all', searchTerm);
    }
    
    // Fonction pour charger les produits
    function loadProducts(category = 'all', searchTerm = '') {
        const productsContainer = document.getElementById('products-container');
        productsContainer.innerHTML = '';
        
        // Appliquer les filtres
        let filteredProducts = applyFilters(productsData, category, searchTerm);
        
        if (filteredProducts.length === 0) {
            productsContainer.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--gris-tres-clair);">
                    Aucun produit trouvé avec ces critères de recherche.
                </div>
            `;
        } else {
            filteredProducts.forEach(product => {
                const productCard = createProductCard(product);
                productsContainer.appendChild(productCard);
            });
        }
    }
    
    // Fonction pour appliquer les filtres
    function applyFilters(products, category = 'all', searchTerm = '') {
        let filteredProducts = [...products];
        
        // Filtrer par catégorie
        if (category !== 'all') {
            filteredProducts = filteredProducts.filter(product => product.product_categorie === category);
        }
        
        // Filtrer par terme de recherche
        if (searchTerm) {
            filteredProducts = filteredProducts.filter(product => 
                product.product_name.toLowerCase().includes(searchTerm) || 
                product.product_description.toLowerCase().includes(searchTerm)
            );
        }
        
        // Appliquer le tri
        const sortValue = document.getElementById('sort-filter').value;
        switch(sortValue) {
            case 'price-asc':
                filteredProducts.sort((a, b) => a.product_price - b.product_price);
                break;
            case 'price-desc':
                filteredProducts.sort((a, b) => b.product_price - a.product_price);
                break;
            case 'stock':
                filteredProducts.sort((a, b) => b.current_stock_quantity - a.current_stock_quantity);
                break;
            default: // name
                filteredProducts.sort((a, b) => a.product_name.localeCompare(b.product_name));
        }
        
        return filteredProducts;
    }
    
    // Fonction pour créer une carte de produit
    function createProductCard(product) {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <div class="product-image">Image ${product.product_name}</div>
            <div class="product-name">${product.product_name}</div>
            <div class="product-description">${product.product_description}</div>
            <div class="product-price">${product.product_price} MAD</div>
            <div class="product-stock">Stock: ${product.current_stock_quantity} unités</div>
            <div class="product-actions">
                <div class="quantity-selector">
                    <button class="quantity-btn minus" data-id="${product.product_id}">-</button>
                    <input type="text" class="quantity-input" value="1" data-id="${product.product_id}">
                    <button class="quantity-btn plus" data-id="${product.product_id}">+</button>
                </div>
                <button class="add-to-cart-btn" data-id="${product.product_id}" ${product.current_stock_quantity === 0 ? 'disabled' : ''}>
                    ${product.current_stock_quantity === 0 ? 'Rupture' : 'Ajouter'}
                </button>
            </div>
        `;
        
        // Ajouter des écouteurs d'événements
        const minusBtn = productCard.querySelector('.minus');
        const plusBtn = productCard.querySelector('.plus');
        const quantityInput = productCard.querySelector('.quantity-input');
        const addToCartBtn = productCard.querySelector('.add-to-cart-btn');
        
        minusBtn.addEventListener('click', function() {
            let value = parseInt(quantityInput.value);
            if (value > 1) {
                quantityInput.value = value - 1;
            }
        });
        
        plusBtn.addEventListener('click', function() {
            let value = parseInt(quantityInput.value);
            const productId = parseInt(this.getAttribute('data-id'));
            const product = productsData.find(p => p.product_id === productId);
            
            if (value < product.current_stock_quantity) {
                quantityInput.value = value + 1;
            }
        });
        
        addToCartBtn.addEventListener('click', function() {
            const productId = parseInt(this.getAttribute('data-id'));
            const quantity = parseInt(quantityInput.value);
            addToCart(productId, quantity);
            quantityInput.value = 1; // Réinitialiser la quantité
        });
        
        return productCard;
    }
    
    // Fonction pour ajouter au panier
    function addToCart(productId, quantity) {
        const product = productsData.find(p => p.product_id === productId);
        
        if (!product) {
            alert('Produit non trouvé!');
            return;
        }
        
        if (quantity <= 0) {
            alert('Veuillez sélectionner une quantité valide!');
            return;
        }
        
        if (quantity > product.current_stock_quantity) {
            alert('Stock insuffisant!');
            return;
        }
        
        // Vérifier si le produit est déjà dans le panier
        const existingItem = cart.find(item => item.product_id === productId);
        
        if (existingItem) {
            // Vérifier si la nouvelle quantité dépasse le stock
            if (existingItem.quantity + quantity > product.current_stock_quantity) {
                alert('Quantité totale dépasse le stock disponible!');
                return;
            }
            existingItem.quantity += quantity;
        } else {
            // Ajouter un nouvel article au panier
            cart.push({
                product_id: productId,
                product_name: product.product_name,
                product_price: product.product_price,
                quantity: quantity
            });
        }
        
        // Sauvegarder le panier
        localStorage.setItem('hormarket_cart', JSON.stringify(cart));
        
        // تحديث السلة فوراً - تحديث العداد والنافذة
        updateCartDisplay();
        
        // إذا كانت نافذة السلة مفتوحة، تحديث محتواها أيضاً
        if (cartOverlay.classList.contains('active')) {
            updateCartModal();
        }
        
        // Afficher un message de confirmation
        alert(`${quantity} ${product.product_name} ajouté(s) au panier!`);
    }
    
    // Fonction pour mettre à jour l'affichage du panier
    function updateCartDisplay() {
        const cartCount = document.getElementById('cart-count');
        const cartIndicator = document.getElementById('cart-indicator');
        
        // Calculer le nombre total d'articles
        const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
        
        // Mettre à jour les indicateurs
        cartCount.textContent = `${totalItems} article${totalItems > 1 ? 's' : ''}`;
        cartIndicator.textContent = totalItems;
    }
    
    // Fonction pour mettre à jour le modal du panier
    function updateCartModal() {
        const cartItemsLarge = document.getElementById('cart-items-large');
        const emptyCartLarge = document.getElementById('empty-cart-large');
        const cartTotalLarge = document.getElementById('cart-total-large');
        const cartTotalAmountLarge = document.getElementById('cart-total-amount-large');
        const checkoutBtnLarge = document.getElementById('checkout-btn-large');
        
        // Afficher ou masquer le panier vide
        if (cart.length === 0) {
            emptyCartLarge.style.display = 'block';
            cartTotalLarge.style.display = 'none';
            checkoutBtnLarge.disabled = true;
            cartItemsLarge.innerHTML = '';
        } else {
            emptyCartLarge.style.display = 'none';
            cartTotalLarge.style.display = 'flex';
            checkoutBtnLarge.disabled = false;
            
            // Vider et remplir la liste des articles
            cartItemsLarge.innerHTML = '';
            
            let totalAmount = 0;
            
            cart.forEach((item, index) => {
                const product = productsData.find(p => p.product_id === item.product_id);
                if (product) {
                    const itemTotal = item.quantity * item.product_price;
                    totalAmount += itemTotal;
                    
                    const cartItem = document.createElement('div');
                    cartItem.className = 'cart-item-large';
                    cartItem.innerHTML = `
                        <div class="cart-item-image">Image ${item.product_name}</div>
                        <div class="cart-item-details">
                            <div class="cart-item-name">${item.product_name}</div>
                            <div class="cart-item-price">${item.product_price} MAD</div>
                        </div>
                        <div class="cart-item-controls">
                            <div class="quantity-controls-large">
                                <button class="quantity-btn-large minus-large" data-index="${index}">-</button>
                                <input type="text" class="quantity-input-large" value="${item.quantity}" data-index="${index}">
                                <button class="quantity-btn-large plus-large" data-index="${index}">+</button>
                            </div>
                            <button class="remove-item-large" data-index="${index}">Supprimer</button>
                        </div>
                    `;
                    cartItemsLarge.appendChild(cartItem);
                }
            });
            
            // Mettre à jour le total
            cartTotalAmountLarge.textContent = `${totalAmount} MAD`;
        }
        
        // Ajouter des écouteurs d'événements pour les boutons de contrôle
        document.querySelectorAll('.minus-large').forEach(btn => {
            btn.addEventListener('click', function() {
                const index = parseInt(this.getAttribute('data-index'));
                updateCartItemQuantity(index, -1);
            });
        });
        
        document.querySelectorAll('.plus-large').forEach(btn => {
            btn.addEventListener('click', function() {
                const index = parseInt(this.getAttribute('data-index'));
                updateCartItemQuantity(index, 1);
            });
        });
        
        document.querySelectorAll('.quantity-input-large').forEach(input => {
            input.addEventListener('change', function() {
                const index = parseInt(this.getAttribute('data-index'));
                const newQuantity = parseInt(this.value);
                if (newQuantity > 0) {
                    setCartItemQuantity(index, newQuantity);
                }
            });
        });
        
        document.querySelectorAll('.remove-item-large').forEach(btn => {
            btn.addEventListener('click', function() {
                const index = parseInt(this.getAttribute('data-index'));
                removeFromCart(index);
            });
        });
    }
    
    // Fonction pour mettre à jour la quantité d'un article
    function updateCartItemQuantity(index, change) {
        if (index >= 0 && index < cart.length) {
            const product = productsData.find(p => p.product_id === cart[index].product_id);
            const newQuantity = cart[index].quantity + change;
            
            if (newQuantity <= 0) {
                removeFromCart(index);
            } else if (newQuantity > product.current_stock_quantity) {
                alert('Stock insuffisant!');
            } else {
                cart[index].quantity = newQuantity;
                localStorage.setItem('hormarket_cart', JSON.stringify(cart));
                updateCartDisplay();
                updateCartModal();
            }
        }
    }
    
    // Fonction pour définir la quantité d'un article
    function setCartItemQuantity(index, newQuantity) {
        if (index >= 0 && index < cart.length) {
            const product = productsData.find(p => p.product_id === cart[index].product_id);
            
            if (newQuantity > product.current_stock_quantity) {
                alert('Stock insuffisant!');
                updateCartModal(); // Réinitialiser l'affichage
            } else {
                cart[index].quantity = newQuantity;
                localStorage.setItem('hormarket_cart', JSON.stringify(cart));
                updateCartDisplay();
                updateCartModal();
            }
        }
    }
    
    // Fonction pour supprimer un article du panier
    function removeFromCart(index) {
        if (index >= 0 && index < cart.length) {
            cart.splice(index, 1);
            localStorage.setItem('hormarket_cart', JSON.stringify(cart));
            updateCartDisplay();
            updateCartModal();
        }
    }
    
    // Fonction pour confirmer l'achat
    function confirmPurchase() {
        if (cart.length === 0) {
            alert('Votre panier est vide!');
            return;
        }
        
        // Vérifier le stock pour tous les articles
        for (const item of cart) {
            const product = productsData.find(p => p.product_id === item.product_id);
            if (!product || product.current_stock_quantity < item.quantity) {
                alert(`Stock insuffisant pour ${item.product_name}!`);
                return;
            }
        }
        
        // حفظ المنتجات التي تم شراؤها للإيصال
        const purchasedItems = [...cart];
        
        // Créer une commande pour chaque article du panier
        const orderDate = new Date().toISOString().split('T')[0];
        let totalPurchaseAmount = 0;
        
        purchasedItems.forEach(item => {
            const product = productsData.find(p => p.product_id === item.product_id);
            const totalPrice = item.quantity * item.product_price;
            totalPurchaseAmount += totalPrice;
            
            // Créer la commande
            const newOrder = {
                "order_id": ordersData.length > 0 ? Math.max(...ordersData.map(o => o.order_id)) + 1 : 1,
                "user_id": user_id,
                "product_id": item.product_id,
                "order_date": orderDate,
                "product_quantity": item.quantity,
                "order_total_price": totalPrice
            };
            
            // Ajouter à la base de données simulée
            ordersData.push(newOrder);
            
            // Mettre à jour le stock (simulation)
            product.current_stock_quantity -= item.quantity;
        });
        
        // Sauvegarder les commandes
        localStorage.setItem('hormarket_orders', JSON.stringify(ordersData));
        
        // Afficher le reçu مع البيانات المحفوظة
        showReceipt(purchasedItems, totalPurchaseAmount);
        
        // Vider le panier
        cart = [];
        localStorage.setItem('hormarket_cart', JSON.stringify(cart));
        updateCartDisplay();
        updateCartModal();
        
        // Fermer le modal du panier
        cartOverlay.classList.remove('active');
        
        // Recharger les produits pour mettre à jour les stocks
        loadProducts();
    }
    
    // Fonction pour afficher le reçu
    function showReceipt(purchasedItems, totalAmount) {
        const receiptDate = document.getElementById('receipt-date');
        const receiptItems = document.getElementById('receipt-items');
        const receiptTotal = document.getElementById('receipt-total');
        const receiptFooter = document.querySelector('.receipt-footer');
        
        // Mettre à jour la date
        const now = new Date();
        receiptDate.textContent = now.toLocaleDateString('fr-FR', {
            day: 'numeric',
            month: 'long',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
        
        // Mettre à jour les articles
        receiptItems.innerHTML = '';
        
        purchasedItems.forEach(item => {
            const product = productsData.find(p => p.product_id === item.product_id);
            if (product) {
                const itemTotal = item.quantity * item.product_price;
                
                const receiptItem = document.createElement('div');
                receiptItem.className = 'receipt-item';
                receiptItem.innerHTML = `
                    <span>${item.product_name}</span>
                    <span>${item.quantity} x ${item.product_price} MAD</span>
                `;
                receiptItems.appendChild(receiptItem);
            }
        });
        
        // Mettre à jour le total
        receiptTotal.textContent = `${totalAmount} MAD`;
        
        // تحديث نص الإيصال
        receiptFooter.innerHTML = `
            Votre commande a été transférée vers "Mes Commandes"<br>
            Merci pour votre achat!<br>
            À bientôt chez HorMarket
        `;
        
        // Afficher le reçu
        document.getElementById('receipt-overlay').classList.add('active');
    }
    
    // Fonction pour charger les commandes
    function loadOrders() {
        const ordersTable = document.getElementById('orders-table');
        ordersTable.innerHTML = '';
        
        // Filtrer les commandes de l'utilisateur actuel
        const userOrders = ordersData.filter(order => order.user_id === user_id);
        
        if (userOrders.length === 0) {
            ordersTable.innerHTML = `
                <tr>
                    <td colspan="7" style="text-align: center; color: var(--gris-tres-clair); padding: 30px;">
                        Aucune commande trouvée. Vos commandes apparaîtront ici après vos achats.
                    </td>
                </tr>
            `;
        } else {
            // ترتيب الطلبات من الأحدث إلى الأقدم
            const sortedOrders = userOrders.sort((a, b) => new Date(b.order_date) - new Date(a.order_date));
            
            sortedOrders.forEach(order => {
                const product = productsData.find(p => p.product_id === order.product_id);
                const row = ordersTable.insertRow();
                row.innerHTML = `
                    <td>#${order.order_id}</td>
                    <td>${order.order_date}</td>
                    <td>${product ? product.product_name : 'Produit inconnu'}</td>
                    <td>${order.product_quantity}</td>
                    <td>${product ? product.product_price + ' MAD' : 'N/A'}</td>
                    <td>${order.order_total_price} MAD</td>
                    <td><span class="status-badge status-completed">Complétée</span></td>
                `;
            });
        }
    }
});