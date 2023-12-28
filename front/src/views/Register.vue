<template>

  <body>
  <section class="page-header">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="content">
            <h1 class="page-name">Здравсвуйте!</h1>
            <p>Мы рады видеть вас!</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="page-wrapper">
    <div class="checkout shopping">
      <div class="container">
        <div class="row">
          <div class="col w-100">
            <div class="block billing-details">
              <form class="checkout-form">
                <div class="form-group">
                  <p>Адрес электронной почты</p>
                  <input v-model="username" type="text" class="form-control" id="emailOrPhone" placeholder="">
                </div>
                <div class="form-group">
                  <p>Дата рождения</p>
                  <input v-model="birthdate" type="date" class="form-control" id="birthdate" required />
                </div>

                <div class="form-group">
                  <p>Пароль</p>
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="">
                </div>
                <div>
                  <button @click.prevent="register" class="btn btn-success btn-lg">Продолжить</button>
                  <p v-if="registrationStatus">{{ registrationMessage }}</p>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      birthdate: "",
      registrationStatus: null, // Добавлено поле для статуса регистрации
      registrationMessage: "", // Добавлено поле для сообщения о регистрации
    };
  },
  methods: {
    async register() {
      try {

        // Выполнение запроса на регистрацию
        const response = await axios.post(
            'http://127.0.0.1:8000/api/registeruser/',
            {
              username: this.username,
              password: this.password,
              birth_date: this.birthdate,
            }
        );

        // Установка статуса и сообщения о успешной регистрации
        this.registrationStatus = "success";
        this.registrationMessage = "Регистрация прошла успешно!";
        setTimeout(() => {
          // Редирект на страницу авторизации
          this.$router.push({ name: 'Login' });
        }, 2000);
      } catch (error) {
        // Обработка ошибок
        this.registrationStatus = "error";
        this.registrationMessage = `Ошибка при регистрации: ${error.message}`;
        console.error("Регистрации:", error);
      }
    },
  },
};
</script>