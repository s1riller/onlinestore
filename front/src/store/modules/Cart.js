import axios from 'axios';

export default {
    state: {
        cart: [],
    },
    getters: {
        // Геттер для получения товаров в корзине
        cartItems(state) {
            return state.cart;
        },
        // Геттер для вычисления общей стоимости товаров в корзине
        cartTotal(state) {
            return state.cart.reduce((total, item) => total + item.price * item.quantity, 0);
        },
        cartItemIdsAndQuantities(state) {
            return state.cart.map(item => ({
                product: item.id,
                quantity: item.quantity,
            }));
        }
    },
    mutations: {
        // Мутация для добавления товара в корзину
        addToCart(state, product) {
            console.log(product)
            const existingProduct = state.cart.find(item => item.id === product.id);

            if (existingProduct) {
                // Если товар уже есть в корзине, увеличиваем его количество
                existingProduct.quantity++;
            } else {
                // Если товара нет в корзине, добавляем его
                state.cart.push({ ...product, quantity: 1 });
            }
            localStorage.setItem('cart', JSON.stringify(state.cart));
        },
        // Мутация для удаления товара из корзины
        removeFromCart(state, productId) {
            state.cart = state.cart.filter(item => item.id !== productId);
            localStorage.setItem('cart', JSON.stringify(state.cart));
        },
        // Мутация для изменения количества товара в корзине
        updateCartItemQuantity(state, { productId, quantity }) {
            const product = state.cart.find(item => item.id === productId);
            if (product) {
                product.quantity = quantity;
            }
            localStorage.setItem('cart', JSON.stringify(state.cart));
        },
        setCartFromLocalStorage(state) {
            const savedCart = localStorage.getItem('cart');
            if (savedCart) {
                state.cart = JSON.parse(savedCart);
            }
        },
        clearCart(state) {
            state.cart = []; // Устанавливаем корзину в пустой массив
            localStorage.setItem('cart', JSON.stringify(state.cart)); // Обновляем корзину в localStorage
        },
    },
    actions: {
        // Действие для добавления товара в корзину
        async addToCart({ commit }, productId) {
            try {
                // Здесь вы можете выполнить запрос к серверу для получения информации о товаре по его ID
                // Например, используя axios
                const response = await axios.get(`/api/products/${productId}`);
                const product = response.data;

                // Вызываем мутацию для добавления товара в корзину
                commit('addToCart', product);
            } catch (error) {
                console.error('Ошибка при добавлении товара в корзину', error);
            }
        },
        // Действие для удаления товара из корзины
        removeCartItem({ commit }, productId) {
            commit('removeFromCart', productId);
        },
        // Действие для изменения количества товара в корзине
        updateCartQuantity({ commit }, { productId, quantity }) {
            commit('updateCartItemQuantity', { productId, quantity });
        },
        clearCart({ commit }) {
            commit('clearCart'); // Вызываем мутацию clearCart
        },
    },
};
