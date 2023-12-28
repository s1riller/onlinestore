<template>

  <body>
  <section class="page-header">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="content">
            <h1 class="page-name">С возвращением!</h1>
            <p>Мы рады видеть вас снова!</p>
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
                  <p>Адрес электронной почты или номер телефона</p>
                  <input v-model="username" type="text" class="form-control" id="emailOrPhone" placeholder="">
                </div>
                <div class="form-group">
                  <p>Пароль</p>
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="">
                </div>
                <a href="#">Забыли пароль?</a>
                <div>
                  <button @click.prevent="login" class="btn btn-success btn-lg">Вход</button>

                </div>
                <p>Нужна учетная запись?<a class="text-info" @click="$router.push({ name: 'Register' })"> Зарегистироваться!</a></p>
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
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(
            'http://127.0.0.1:8000/auth/token/login',
            {
              username: this.username,
              password: this.password,
            }
        );

        // Обработка успешного ответа от сервера
        const token = response.data.auth_token;

        // Сохранение токена в локальном хранилище
        localStorage.setItem("token", token);

        // Редирект на другую страницу, например, 'Home'
        this.$router.push({ name: 'Home' });
        setTimeout(() => {
          location.reload();
        }, 1000);

      } catch (error) {
        // Обработка ошибок
        console.error("Ошибка при авторизации:", error);
      }
    },
  },
};

</script>