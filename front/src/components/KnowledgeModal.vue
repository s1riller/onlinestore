// Modal.vue

<template>
  <div class="modal" v-if="showModal">
    <div class="modal-overlay" @click="closeModal"></div> <!-- Затемняющий фон -->
    <div class="modal-content">
      <button class="modal-close-button" @click="closeModal">×</button> <!-- Кнопка закрытия -->
      <h2>Введите имя и фамилию</h2>
      <input v-model="firstName" placeholder="Имя" />
      <input v-model="lastName" placeholder="Фамилия" />
      <button @click="saveUserData">Сохранить</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
    };
  },
  computed: {
    showModal() {
      // Здесь вы можете определить условие, когда модальное окно должно быть видимым
      // Например, если в глобальном хранилище нет имени и фамилии
      return true;
    },
  },
  methods: {
    saveUserData() {
      // Здесь вы можете отправить данные на сервер и обновить состояние Vuex
      this.$store.dispatch('saveUserData', {
        firstName: this.firstName,
        lastName: this.lastName,
      });
    },
  },
};
</script>


<style scoped>
/* Стили для модального окна и фона */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  z-index: 999;
  padding: 20px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Затемнение с прозрачностью */
  z-index: 998; /* Под фоном модального окна */
}

.modal-close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 20px;
  background: none;
  border: none;
  outline: none;
  color: gray;
}
</style>

