// Ваш компонент с модальным окном

<template>
  <div>
    <!-- Ваш код компонента -->

    <b-modal v-model="showModal" @hidden="onModalHidden">
      <!-- Содержимое вашего модального окна -->
      <p>Модальное окно</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
    };
  },
  methods: {
    openModal() {


      setTimeout(() => {
        this.showModal = false;
      }, 1000); // Через секунду закрыть модальное окно
    },
    onModalHidden() {
      // Дополнительные действия при закрытии модального окна
    },
  },
};
</script>

<style scoped>
/* Стили вашего компонента */
</style>
