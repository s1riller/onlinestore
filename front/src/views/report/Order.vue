<template>
  <div>
    <h1>Заказ</h1>
    <p>Название товара: {{ order.product.name }}</p>
    <p>Количество: {{ order.quantity }}</p>
    <p>Минимальный остаток: {{ order.product.min_quantity }}</p>
    <button @click="editMinQuantity">Редактировать минимальный остаток</button>
  </div>
</template>

<script>
import {url_server} from "@/main";
export default {
  data() {
    return {
      order: null,
    };
  },
  mounted() {
    // Загрузка данных о заказе с сервера по его ID
    const orderId = this.$route.params.id; // предполагается, что вы используете Vue Router
    this.loadOrder(orderId);
  },
  methods: {
    loadOrder(orderId) {
      // Здесь вы можете использовать Axios или другую библиотеку для выполнения GET-запроса к API Django
      axios.get(`http://${url_server}:8000/api/orders/`,
          {
            headers: {
              'Authorization': `Token ${localStorage.getItem('token')}`
            }
          }
      )

          .then((response) => {
            this.order = response.data;
          })
          .catch((error) => {
            console.error('Ошибка при загрузке заказа', error);
          });
    },
    editMinQuantity() {
      // Перенаправление на страницу редактирования минимального остатка товара
      const productId = this.order.product.id;
      this.$router.push(`/edit-min-quantity/${productId}`);
    },
  },
};
</script>
