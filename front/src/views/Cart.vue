<template>
  <section class="h-100 h-custom" style="background-color: #eee;">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col">
          <div class="card">
            <div class="card-body p-4">
              <div class="row" v-if="!orderSuccess">

                <div class="col-lg-7">
                  <h5 class="mb-3" @click="$router.push({ name: 'Shop' })"><a class="text-body" href="#!"><i
                      class="fas fa-long-arrow-alt-left me-2"></i>Продолжить покупки</a></h5>
                  <hr>
                  <h5 class="mb-3" @click="confirmClearCart"><a class="text-body" href="#!"><i
                      class="fas fa-long-arrow-alt-left me-2"></i>Очистить корзину</a></h5>
                  <hr>

                  <div class="d-flex justify-content-between align-items-center mb-4">
                    <div>
                      <p class="mb-1">Корзина</p>
                      <p class="mb-0">У вас в корзине {{ cartItems().length }}
                        {{ getProductsWord(cartItems().length) }}</p>
                    </div>
                    <div>
                      <p class="mb-0"><span class="text-muted">Sort by:</span> <a class="text-body"
                                                                                  href="#!">Цене <i
                          class="fas fa-angle-down mt-1"></i></a></p>
                    </div>
                  </div>


                  <div v-for="item in cartItems()" class="card mb-3">
                    <div class="card-body">
                      <div class="d-flex justify-content-between">
                        <div class="d-flex flex-row align-items-center">
                          <div>
                            <img
                                :src="item.img"
                                alt="Shopping item" class="img-fluid rounded-3" style="width: 65px;">
                          </div>
                          <div class="ms-3">
                            <h5>{{ item.name }}</h5>
                            <p class="small mb-0">{{ item.description }}</p>
                          </div>
                        </div>
                        <div class="d-flex flex-row align-items-center">
                          <div style="width: 50px;">
                            <h5 class="fw-normal mb-0">{{ item.quantity }}</h5>
                          </div>
                          <div style="width: 80px;">
                            <h5 class="mb-0">{{ item.price }}$</h5>
                          </div>
                          <a href="#!" style="color: #cecece;"><i class="fas fa-trash-alt"></i></a>
                        </div>
                      </div>
                    </div>
                  </div>


                </div>
                <div class="col-lg-5">

                  <div class="card bg-primary text-white rounded-3">
                    <div class="card-body">
                      <div class="d-flex justify-content-between align-items-center mb-4">
                        <h5 class="mb-0">Детали корзины</h5>
                        <!--                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp"-->
                        <!--                             class="img-fluid rounded-3" style="width: 45px;" alt="Avatar">-->
                      </div>


                      <form class="mt-4">
                        <div class="form-outline form-white mb-4">
                          <input id="typeName" v-model="fullName" class="form-control form-control-lg"
                                 placeholder="Полное имя получателя получателя" siez="17"
                                 type="text" required/>
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input id="typeName" v-model="phone" class="form-control form-control-lg"
                                 placeholder="Контактный телефон"
                                 siez="17"
                                 type="text" required/>
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input id="typeText" v-model="address" class="form-control form-control-lg"
                                 placeholder="Адрес доставки" siez="17" type="text" required/>
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input id="typeText" v-model="deliveryInstructions" class="form-control form-control-lg"
                                 maxlength="19" minlength="19"
                                 placeholder="Комментарий к доставке" siez="17" type="text"/>
                        </div>


                        <div class="form-outline form-white mb-4">
                          <input id="email" v-model="email" class="form-control form-control-lg"
                                 placeholder="Электронная почта"
                                 type="email" required/>
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input id="postalCode" v-model="postalCode" class="form-control form-control-lg"
                                 placeholder="Почтовый индекс"
                                 type="text" required/>
                        </div>

                        <div class="form-outline form-white mb-4">
                          <div class="form-outline form-white mb-4">
                            <p class="text-white">Выберите предпочтительную дату и время доставки:</p>
                            <input id="deliveryTime" v-model="deliveryTime" class="form-control form-control-lg"
                                   type="datetime-local" required/>
                          </div>


                        </div>


                      </form>

                      <hr class="my-4">

                      <div class="d-flex justify-content-between">
                        <p class="mb-2 text-white">Итог</p>
                        <p class="mb-2 text-white">${{ cartTotal() }}</p>
                      </div>

                      <div class="d-flex justify-content-between">
                        <p class="mb-2 text-white">Стоимость доставки</p>
                        <p class="mb-2 text-white">$0</p>
                      </div>

                      <div v-if="!isFormValid" class="alert alert-danger">
                        {{ errorMessage }}
                      </div>

                      <button class="btn btn-info btn-block btn-lg" @click="submitOrder" type="button">
                        <div class="d-flex justify-content-between">
                          <span>${{ cartTotal() }}</span>
                          <span>Продолжить <i class="fas fa-long-arrow-alt-right ms-2"></i></span>
                        </div>
                      </button>

                    </div>
                  </div>

                </div>

              </div>
              <div class="row" v-if="orderSuccess">
                <div class="col">
                  <div class="alert alert-success">
                    Ваш заказ успешно оформлен!
                  </div>
                  <div>
                    <h5>Детали заказа:</h5>
                    <p>Номер заказа: {{ orderDetails.id }}</p>
                    <p>Имя получателя: {{ orderDetails.full_name }}</p>
                    <p>Адрес доставки: {{ orderDetails.address }}</p>
                    <p>Общая стоимость: ${{ orderDetails.total_price }}</p>
                  </div>
                </div>
                <h5 class="mb-3" @click="$router.push({ name: 'Shop' })"><a class="text-body" href="#!"><i
                    class="fas fa-long-arrow-alt-left me-2"></i>Продолжить покупки</a></h5>
              </div>

            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapGetters,mapActions} from "vuex";
import axios from "axios";

export default {

  data() {
    return {
      userId: null,
      fullName: null,
      phone: null,
      address: null,
      deliveryInstructions: null,
      email: null,
      postalCode: null,
      deliveryTime: null,
      isFormValid: true,
      errorMessage: null,
      orderSuccess: false,
      orderDetails: null,
    };
  },

  methods: {
    ...mapGetters(['cartItems']),
    ...mapGetters(['cartItemIdsAndQuantities']),
    ...mapGetters(['cartTotal']),
    ...mapActions(['clearCart']),
    async fetchUserId() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/profile', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        this.userId = response.data.id; // Сохраняем ID пользователя
      } catch (error) {
        console.error(error);
      }
    },
    getProductsWord(count) {
      let word = 'товаров';

      if (count % 10 === 1 && count % 100 !== 11) {
        word = 'товар';
      } else if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100)) {
        word = 'товара';
      }

      return word;
    },
    submitOrder() {
      if (!this.fullName || !this.phone || !this.address || !this.email || !this.deliveryTime) {
        this.isFormValid = false;
        this.errorMessage = 'Пожалуйста, заполните все поля.';
        return;
      }

      this.isFormValid = true;
      this.errorMessage = '';

      const orderData = {
        user: this.userId,
        full_name: this.fullName,
        phone: this.phone,
        address: this.address,
        delivery_instructions: this.deliveryInstructions,
        email: this.email,
        postal_code: this.postalCode,
        delivery_date: this.deliveryTime,
        order_items: this.cartItemIdsAndQuantities(), // или преобразуйте данные товаров, если необходимо
        total_price: this.cartTotal(),


      };

      axios.post('http://127.0.0.1:8000/api/order/', orderData)
          .then(response => {
            // Обработка успешного ответа
            console.log('Order submitted:', response.data);
            this.orderSuccess = true;
            this.orderDetails = response.data;
            this.clearCart();
            // Можно добавить действия после успешной отправки, например, перенаправление или сообщение пользователю
          })
          .catch(error => {
            // Обработка ошибок при отправке
            console.error('Error submitting order:', error);
          });
    },
    confirmClearCart() {
      if (confirm("Вы уверены, что хотите очистить корзину?")) {
        this.clearCart();
      }
    }
  },
  created() {
    this.fetchUserId()
  }
}
</script>

<style scoped>

</style>