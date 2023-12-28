<template>
  <div class="bg-discord-black p-5">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="row">
            <div class="col-md-8 bg-body p-3 rounded-2 card-hover divChangeColor" >
              <div class="row">
                <div class="col-md-6">
                  <h3 class="text-muted">
                  </h3>
                  <h3>
                    20 лет
                  </h3>
                  <h5 class="text-dark">
                    gg@ggjp.ru
                  </h5>
                  <address>
                    <strong>Россия</strong><br />Иркутская область<br />Иркутск, Ленина 56а<br />
                  </address>
                  <button type="button" class="btn btn-outline-secondary btn-md btn-block active">
                    Редактировать
                  </button>
                </div>
                <div class="col-md-6 d-flex justify-content-center align-items-center">
                  <!--                <img class="rounded-2 mx-auto my-auto" alt="Image Preview" style="height: 256px; width: auto" src="https://sun9-25.userapi.com/impg/VyjBjULKjvWuCRU-me_iMmwIlvYY7Dvw21XYSQ/rDtguY6DPVY.jpg?size=1080x1350&quality=96&sign=5c312e1eb0b1f0377c22890797ebe0b3&type=album" />-->
                  <div class="avatar-container" @mouseover="startAnimation" @animationend="resetAnimation">
                    <img class="avatar" style="height: 256px; width: auto" alt="User Avatar" src="https://sun9-25.userapi.com/impg/VyjBjULKjvWuCRU-me_iMmwIlvYY7Dvw21XYSQ/rDtguY6DPVY.jpg?size=1080x1350&quality=96&sign=5c312e1eb0b1f0377c22890797ebe0b3&type=album" />
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4 bi-gender-ambiguous rounded-2">
              <h3 class="text-white">
                Результаты
              </h3>
              <ul class="list-group">
                <li class="list-group-item">Cras justo odio</li>
                <li class="list-group-item">Dapibus ac facilisis in</li>
                <li class="list-group-item">Morbi leo risus</li>
                <li class="list-group-item">Porta ac consectetur ac</li>
                <li class="list-group-item">Vestibulum at eros</li>
              </ul>
            </div>
          </div>


          <div class="row mt-5 bg-body">
            <h3 class="text-center text-dark mt-2 mb-5">
              h3. Lorem ipsum dolor sit amet.
            </h3>
            <div class="col-md-12">
              <div class="row">
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
                <div class="col-md-2">
                  <img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg" />
                  <h3>
                    h3. Lorem ipsum dolor sit amet.
                  </h3>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "@/static/discord.css";
import Modal from "@/components/Modal.vue";
import { mapGetters } from 'vuex'
export default {
  data() {
    return {
      show: false, // Переменная для управления видимостью модального окна
    };
  },
  components: {
    Modal, // Регистрируем компонент Modal для использования
  },
  methods: {
    showModal() {
      this.show = true; // Показать модальное окно
    },
    closeModal() {
      this.show = false; // Закрыть модальное окно
    },
  },
  computed: {
    ...mapGetters(['getUserDataProfileProfile']),
    user() {
      return {
        first_name: this.getUserDataProfileProfile.first_name,
      };
    },
  },
  created() {
    // Log the user's first name to the console when the component is created.
    console.log(this.user.first_name);
  },
};
</script>


<style>
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
  overflow-x: auto;
  display: flex;
  flex-direction: column;
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

.btn-green {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}

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
  overflow-x: auto;
  display: flex;
  flex-direction: column;
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

.btn-green {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}

.modal::-webkit-scrollbar {
  width: 0;
}

/*Убрать полосу прокрутки для всей страницы*/
::-webkit-scrollbar {
  width: 0;
}

.image-container {
  position: relative;
  overflow: hidden;
}

.image-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* Измените значение альфа-канала для регулировки уровня затемнения */
  pointer-events: none;
}

.image-container {
  width: 100%;
  height: 500px; /* Устанавливаем высоту, которую вы хотите использовать */
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Обрезаем и показываем центр изображения */
}

.square-image {
  width: 256px;
  height: 256px;
  object-fit: cover;
}


.divChangeColor {
  position: relative;
  display: inline-block;
  overflow: hidden;
  text-decoration: none;
  color: #A9A9A9;
  height: 100%; /* Добавьте высоту */
}

.divChangeColor::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, #FFFFFF, #23272A);
  transform-origin: right; /* Установка точки преобразования */
  transform: scaleX(1); /* Изначальное значение ширины градиента */
  transition: transform 0.3s ease; /* Плавный переход для эффекта */
}

.divChangeColor:hover::before {
  transform: scaleX(0); /* Уменьшение ширины градиента при наведении */
}


</style>