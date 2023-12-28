<template>
  <div class="row-custom-padding">
    <div class="row">
      <div class="col-12">
        <h4 class="mb-3 text-center">Добавление продукта</h4>
        <form class="needs-validation" novalidate="">
          <div class="row g-3">

            <div class="col-md-6 mb-3">
              <label class="form-label" for="username">Название</label>
              <input v-model="product.name" class="form-control" placeholder="Название продукта" required="" type="text">
              <div class="invalid-feedback">
                Название продукта обязательно.
              </div>
            </div>

            <div class="col-md-6 mb-3">
              <label class="form-label" for="email">Описание</label>
              <input v-model="product.description" class="form-control" placeholder="Описание продукта" type="text">
              <div class="invalid-feedback">
                Описание продукта обязательно.
              </div>
            </div>

            <div class="col-12 mb-3">
              <label class="form-label" for="email">Цена</label>
              <input v-model="product.price" class="form-control" placeholder="Цена продукта" type="number">
              <div class="invalid-feedback">
                Цена продукта обязательно.
              </div>
            </div>

            <div class="col-12 mb-3">
              <label class="form-label" for="country">Категория товара</label>
              <select id="country" v-model="product.category" class="form-select" required=""
                      @change="checkForNewCategory">
                <option v-for="category in categories" :value="category">{{ category.name }}</option>
                <option value="new-category">Добавить новую категорию...</option>
              </select>
              <div class="alert alert-danger" v-if="categoryExistsError">
                Категория уже существует
              </div>
              <div class="invalid-feedback">
                Пожалуйста, выберите категорию товара
              </div>
            </div>

            <div v-if="showNewCategoryForm" class="col-12 mb-3">
              <div class="d-flex align-items-center">
                <input v-model="newCategoryName" class="form-control me-2" placeholder="Введите название новой категории" type="text">

                <!-- Кнопка -->
                <button class="btn btn-primary btn-circle" @click="addNewCategory">
            <span class="material-icons">
                add
            </span>
                </button>
              </div>
            </div>



            <div class="col-12 mb-3">
              <label class="form-label" for="country">Связанный вопрос</label>
              <select id="country" v-model="product.treats" class="form-select" required="">
                <option v-for="answer in answers" :value="answer">{{ answer.text }}</option>
              </select>
              <div class="invalid-feedback">
                Пожалуйста, выберите связанный вопрос
              </div>
            </div>

            <div class="col-12">
              <v-upload-image v-on:file-changed="handleFileChanged"/>
            </div>

            <div class="col-12">
              <button class="w-100 btn btn-primary btn-lg" @click="submitResponse">Отправить</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import VUploadImage from "@/components/v-upload-image.vue";

export default {

  components: {VUploadImage},
  data() {
    return {
      answers: [],
      categories: [],
      showNewCategoryForm: false,
      newCategoryName: '',
      product: {
        name: null,
        description: null,
        treats: null,
        img: null,
        price: null,
        category: null,
        file: null,
      },

      categoryExistsError: false,
    }
  },
  methods: {
    async fetchAnswers() {
      try {
        this.loading = true; // Устанавливаем флаг загрузки в true перед запросом
        const response = await axios.get('http://127.0.0.1:8000/api/answers/');
        this.answers = response.data;
      } catch (error) {
        console.error('Ошибка при получении списка вопросов:', error);
      } finally {
        this.loading = false; // Вне зависимости от результата запроса, устанавливаем флаг загрузки в false
      }
    },
    async fetchCategory() {
      try {
        this.loading = true; // Устанавливаем флаг загрузки в true перед запросом
        const response = await axios.get('http://127.0.0.1:8000/api/categories/');
        this.categories = response.data;
      } catch (error) {
        console.error('Ошибка при получении списка категорий:', error);
      } finally {
        this.loading = false; // Вне зависимости от результата запроса, устанавливаем флаг загрузки в false
      }
    },

    checkForNewCategory() {
      if (this.product.category === 'new-category') {
        this.showNewCategoryForm = true;
      }
    },

    async addNewCategory() {
      event.preventDefault();
      if (this.newCategoryName) {

        const existingCategory = this.categories.find(category => category.name === this.newCategoryName);

        if (existingCategory) {
          // Если категория уже существует, показываем ошибку
          this.categoryExistsError = true;
          return; // Выходим из метода
        }

        try {
          let response = await axios.post('http://127.0.0.1:8000/api/categories/', {
            name: this.newCategoryName
          });

          // Обработка успешного ответа
          if (response.data) {
            this.product.category =  { name: this.newCategoryName };
            this.categories.push({ name: this.newCategoryName });
            this.product.category = this.newCategoryName;
            this.showNewCategoryForm = false;
            this.newCategoryName = '';
            this.categoryExistsError = false;
          } else {
            console.log('Категория добавлена:', response.data);
          }
        } catch (error) {
          // Обработка ошибки отправки запроса
          console.error('Ошибка при добавлении категории:', error);
        }
      }
    },

    handleFileChanged(file) {
      const reader = new FileReader();

      reader.onload = (e) => {
        this.product.img = e.target.result; // Сохраняем base64 строку в свойство img
      };

      reader.readAsDataURL(file); // Чтение файла как Data URL (base64)
    },
    handleFileUpload() {
      this.product.file = this.$refs.file.files[0];
    },

    submitResponse() {
      event.preventDefault();
      let formData = new FormData();
      formData.append('name', this.product.name);
      formData.append('description', this.product.description);
      formData.append('treats', this.product.treats.id);
      formData.append('price', this.product.price);
      formData.append('category', this.product.category.id);
      formData.append('img', this.product.img); // Добавляем base64 строку изображения

      axios.post('http://127.0.0.1:8000/api/medicines/', formData,
          {
            headers: {
              'Authorization': `Token ${localStorage.getItem('token')}`,
              'Content-Type': 'multipart/form-data' // Важно указать правильный Content-Type
            }
          })
          .then(response => {
              console.log(response)
          })
          .catch(error => {
            console.error('Ошибка при создании товара',error)
          });
    }
  },
  created() {
    this.fetchAnswers(); // Добавьте эту строку
    this.fetchCategory();
  },
}
</script>

<style scoped>
.row-custom-padding {
  padding-left: 35%; /* или любое другое значение */
  padding-right: 35%; /* или любое другое значение */
}
.btn-circle {
  width: 38px;
  height: 38px;
  border-radius: 19px;
  text-align: center;
  padding-left: 0;
  padding-right: 0;
  font-size: 16px;
}
</style>
