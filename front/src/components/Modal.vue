<template>
  <div class="modal-backdrop" @click="closeModal">
    <div class="modal" @click.stop>
      <header class="modal-header">
        <slot name="header">

        </slot>
        <button type="button" class="btn-close" @click="closeModal">x</button>
      </header>
      <section class="modal-body">
        <slot name="body">
          <!-- Тело по умолчанию -->
        </slot>
      </section>
      <footer class="modal-footer">
        <slot name="footer">
          <!-- Футер по умолчанию -->
        </slot>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'modal',
  props:{
    selectedProduct: Object,
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
  },
};
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: hidden; /* Скрываем горизонтальную прокрутку */
  overflow-y: auto; /* Добавляем вертикальную прокрутку */
  display: flex;
  flex-direction: column;
  max-width: 80%; /* Максимальная ширина модального окна */
}


.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  border-bottom: 1px solid #eeeeee;
  color: #4AAE9B;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  border: none;
  font-size: 20px;
  padding: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #4AAE9B;
  background: transparent;
}

</style>
