<template>
  <div v-if="this.is_admin()" class="d-flex justify-content-center align-items-center">
    <button class="btn d-flex justify-content-center align-items-center" @click="$router.push({ name: 'AddProduct' })">
    <span class="material-icons">
      add_circle_outline
    </span>
      Добавить товар
    </button>
  </div>


  <modal v-if="show" @close="closeModal">
    <template v-slot:body>
      <div v-if="selectedProduct">
        <h4>{{ selectedProduct.name }}</h4>
        <p>{{ selectedProduct.description }}</p>
        <img :src="selectedProduct.img" alt="" class="product-thumb" style="width:550px;height:auto">

        <div>
          <p>{{ selectedProduct.price }}$</p>
        </div>
        <!-- Остальные данные продукта -->
      </div>
    </template>
    <template v-slot:footer>

      <div>
           <span class="material-icons">
favorite_border
</span>

        <button class="btn" @click="addToCart(selectedProduct)">
    <span class="material-icons">
      shopping_cart
    </span>
        </button>

      </div>
      <button class="btn" @click="closeModal">ОК</button>
    </template>
  </modal>
  <section class="products section">
    <div class="container">
      <div class="row">
        <div v-if="loading" class="text-center">
          <i class="fa fa-spinner fa-spin"></i> Загрузка продуктов...
        </div>
        <div v-for="product in products" :key="product.id" class="col-md-4">
          <div class="product-item">
            <div class="product-thumb">
              <img :src="product.img" alt="Потеряли изобажение товара" class="img-responsive"/>
              <div class="preview-meta">
                <ul>
                  <li @click="showModal(product)">
                    <span class="material-icons">
lightbulb
</span>
                  </li>
                  <li>
                    <span class="material-icons">
favorite_border
</span>
                  </li>
                  <li>

        <button class="btn" @click="addToCart(product)">
        <span class="material-icons">
shopping_cart
</span>
                    </button>
                  </li>
                </ul>
              </div>
            </div>
            <div class="product-content">
              <h4><a href="#">{{ product.name }}</a></h4>
              <p class="price">${{ product.price }}</p>
            </div>
          </div>
        </div>

        <!-- ... другие элементы ... -->

        <!-- Modal.vue -->
        <div id="product-modal" class="modal product-modal fade">
          <!-- ... содержимое модального окна ... -->
        </div><!-- /.modal -->
      </div>
    </div>
  </section>

  <div v-if="showAddToCartNotification" class="notification">
    <p class="text-white">Товар добавлен в корзину </p>
    <p class="text-white">{{addedProduct}}</p>
  </div>
</template>

<script>
import axios from 'axios';
import Modal from "@/components/Modal.vue";
import {mapGetters} from "vuex";

export default {
  name: 'ShopPage',
  components: {
    Modal
  },
  data() {
    return {
      show: false,
      products: [],
      loading: false,
      selectedProduct: null,
      showAddToCartNotification:false,
      addedProduct: null,
    };
  },
  created() {
    this.fetchProducts(); // Добавьте эту строку
  },
  methods: {
    ...mapGetters(['is_admin']),
    showModal(product) {
      console.log(product)
      this.selectedProduct = product;
      this.show = true; // Показать модальное окно
    },
    closeModal() {
      this.show = false; // Закрыть модальное окно
    },
    async fetchProducts() {
      try {
        this.loading = true; // Устанавливаем флаг загрузки в true перед запросом
        const response = await axios.get('http://127.0.0.1:8000/api/medicines/');
        this.products = response.data;
      } catch (error) {
        console.error('Ошибка при получении списка продуктов:', error);
      } finally {
        this.loading = false; // Вне зависимости от результата запроса, устанавливаем флаг загрузки в false
      }
    },

    async addToCart(product) {
      try {
        // Вызываем мутацию addToCart для добавления товара в корзину
        this.$store.commit('addToCart', product); // Замените 'addToCart' на имя вашей мутации
        this.addedProduct = product.name
        // После успешного добавления товара в корзину, устанавливаем флаг для отображения уведомления
        this.showAddToCartNotification = true;

        // Устанавливаем таймер для скрытия уведомления через 3 секунды
        setTimeout(() => {
          this.showAddToCartNotification = false;
        }, 1500);
      } catch (error) {
        // Обработка ошибок, если что-то пошло не так при добавлении в корзину
        console.error('Ошибка при добавлении в корзину:', error);
      }
    },
  }
};
</script>
<style>
.overlay-popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000; /* Выберите значение z-index по вашему усмотрению */
  background-color: rgba(0, 0, 0, 0.5); /* Чтобы создать полупрозрачный фон */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Дополнительные стили для контента внутри popup, если необходимо */
.overlay-popup > .position-relative {
  /* Добавьте стили для контента, чтобы он был выровнен по центру popup */
}

/* Стили для изображения по умолчанию */
.product-thumb img {
  transition: transform 0.2s; /* Добавляем анимацию */
}

/* Стили для изображения при наведении */
.product-thumb img:hover {
  transform: scale(1.1); /* Увеличиваем изображение на 10% */
}
.notification {
  /* Стили для уведомления */
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: rgb(128, 128, 128);
  color: white;
  padding: 10px;
  border-radius: 5px;
}
</style>
