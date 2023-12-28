

<template>
  <div class="container mt-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div
          class="col"
          v-for="(result, index) in sortedUserTestResults"
          :key="index"
      >
        <div class="card shadow-sm">
          <div class="image-collage">
            <div
                v-for="(image, imageIndex) in parseMedicineImage(decodeUnicodeEscapes(result.medicine))"
                :key="imageIndex"
                class="image"
            >

              <img :src="image" :alt="'Image ' + (imageIndex + 1)">
            </div>
          </div>
          <div class="card-body">
            <p class="card-text">
              <ul>
                <li v-for="item in parseMedicineDescription(result.medicine)">{{ item }}</li>
              </ul>
            </p>
            <div class="d-flex justify-content-between align-items-center">
              <div class="btn-group">
                <button  type="button" class="btn btn-sm btn-outline-secondary" @click="showModal(result)">View</button>
                <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
              </div>
              <small class="text-body-tertiary">{{ index === 0 ? 'Последнее тестирование' : ''}}</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  <modal v-if="show" @close="closeModal">
    <template v-slot:header>
      <h2>Проанализировав ваши данные мы готовы предоставить лечение</h2>
    </template>
    <template v-slot:body>
      <h3>Рекомендуемые препараты:</h3>
      <h4>Количество:{{selectedMedicines.length}}</h4>
      <div v-for="(medicine, index) in selectedMedicines" :key="index" class="medicine-item">
        <img :src="medicine.img" :alt="medicine.name" class="medicine-image">
        <div class="medicine-details">
          <h4>{{ medicine.name }}</h4>
          <p>{{ medicine.description }}</p>
        </div>
      </div>
    </template>
    <template v-slot:footer>
      <button @click="closeModal">Закрыть</button>
    </template>
  </modal>


</template>

<script>
import { mapGetters } from 'vuex';
import "@/static/discord.css";
import axios from 'axios';
import Modal from "@/components/Modal.vue";
function decodeUnicodeEscapes(text) {
  return text.replace(/\\u[\dA-Fa-f]{4}/g, function(match) {
    return String.fromCharCode(parseInt(match.substr(2), 16));
  });
}
function getRandomItemsFromArray(array, count) {
  const shuffledArray = array.slice().sort(() => 0.5 - Math.random());
  return shuffledArray.slice(0, count);
}

function compareByIdDesc(a, b) {
  return b.id - a.id;
}
export default {
  data() {
    return {
      show: false,
      selectedMedicines: [], // Добавьте свойство для хранения выбранных препаратов
    };
  },
  components: {
    Modal, // Регистрируем компонент Modal для использования
  },

  computed: {
    ...mapGetters(['getUserTestResults']),
    sortedUserTestResults() {
      return this.getUserTestResults.slice().sort(compareByIdDesc);
    },

  },
  created() {
    this.$store.dispatch('fetchUserTestResults');

  },
  methods: {
    decodeUnicodeEscapes,

    parseMedicineDescription(medicine) {
      try {
        const parsedMedicine = JSON.parse(decodeUnicodeEscapes(medicine));

        return getRandomItemsFromArray(parsedMedicine.map(medicine => medicine.description), 3);
      } catch (error) {
        return "Данные в обработке"; // Или другое сообщение об ошибке
      }
    }
    ,
    parseMedicineImage(medicine) {
      try {
        const parsedMedicine = JSON.parse(decodeUnicodeEscapes(medicine));

        return getRandomItemsFromArray(parsedMedicine.map(medicine => medicine.img), 6);
      } catch (error) {
        return "Данные в обработке"; // Или другое сообщение об ошибке
      }
    },
    showModal(result) {
      this.selectedMedicines = JSON.parse(decodeUnicodeEscapes(result.medicine));
      this.show = true; // Показать модальное окно
    },
    closeModal() {
      this.show = false; // Закрыть модальное окно
    },
  },
}
</script>

<style>
.image-collage {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-between; /* Добавьте это свойство для размещения в 3 столбца */
}

.image {
  flex: 0 0 calc(33.33% - 10px); /* Устанавливаем ширину для 3 столбцов */
  max-width: calc(33.33% - 10px); /* Устанавливаем максимальную ширину для 3 столбцов */
  text-align: center;
}

.image img {
  max-width: 100%;
  height: auto;
  width: 120px; /* Устанавливаем ширину и высоту 32 пикселя */
  height: 120px;
}

.last-result {
  flex: 0 0 calc(66.66% - 10px); /* Увеличьте ширину для последнего элемента до 2/3 от ширины ряда */
  max-width: calc(66.66% - 10px); /* Увеличьте максимальную ширину */
  text-align: center;
}

/* Добавьте стили для остальных элементов */
.image-collage {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-between;
}

.image {
  flex: 0 0 calc(33.33% - 10px); /* Ширина для 3 столбцов */
  max-width: calc(33.33% - 10px); /* Максимальная ширина для 3 столбцов */
  text-align: center;
}

.image img {
  max-width: 100%;
  height: auto;
  width: 120px;
  height: 120px;
}

.card.shadow-sm {
  flex: 1; /* Распределить доступное пространство равномерно между элементами */
}

.card-body {
  display: flex;
  flex-direction: column;
  height: 100%; /* Задать высоту 100% для одинаковой высоты элементов */
}

.card-text {
  flex: 1; /* Занимать доступное пространство внутри элемента card-body */
}

</style>