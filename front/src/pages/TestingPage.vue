<template>
  <body class="d-flex bg-discord-gray vh-100">
  <div class="container">
    <div class="row">
      <div class="mx-auto">
        <div class="block bg-discord-black text-white d-flex justify-content-center align-items-center vh-100">
          <!-- Кнопка-триггер модального окна -->
          <button type="button" class="btn btn-lg btn-light fw-bold" data-bs-toggle="modal" data-bs-target="#questionsModal">
            Начать
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Второе модальное окно -->
  <div class="modal fade" id="questionsModal" tabindex="-1" aria-labelledby="questionsModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ currentQuestion.question }}</h1>
          <button v-if="!loading" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
        <div class="modal-body">
          <div class="form-check" v-for="(answer, index) in questionsData" :key="index">
            <input
                class="form-check-input"
                :type="currentQuestion.id === 1000 ? 'checkbox' : 'radio'"
                name="answerRadio"
                :value="answer.id"
                :id="'answerRadio_' + index"
                :checked="false"
                :defaultChecked="false"
            @change="saveAnswer(answer)"
            />
            <label class="form-check-label" :for="'answerRadio_' + index">{{ answer.title }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <button v-if="!loading" type="button" class="btn btn-secondary" @click="prevQuestion">Назад</button>
          <button v-if="currentQuestionIndex !== (getQuestions.length - 1)" type="button" class="btn btn-primary" @click="nextQuestion">Далее</button>
          <button v-if="!loading && currentQuestionIndex === (getQuestions.length - 1)" class="btn btn-primary" type="button" @click="submitAnswers">Отправить результаты</button>
          <div v-if="loading" class="d-flex align-items-center">
            <div class="spinner-border text-primary" role="status">

            </div>
            <span class="ms-2">Мы анализируем ваши данные</span>
          </div>

        </div>

      </div>
    </div>
  </div>
  </body>
</template>

<style>
</style>

<script>
import "@/static/discord.css";
import { mapGetters } from 'vuex';
import axios from "axios";

const questionsData = {
  "questions": [
    {
      "id": 1,
      "title": "Какие у вас ощущения после умывания",
      "images": [
        {
          "value": "a",
          "src": "https://aravia.ru/skin-test/img/questions/1a.jpg?v=1",
          "text": "Комфортные, ничего не беспокоит"
        },
        {
          "value": "b",
          "src": "https://aravia.ru/skin-test/img/questions/1b.jpg?v=1",
          "text": "Есть дискомфорт: ощущаю стянутость"
        }
      ]
    },
    {
      "id": 2,
      "title": "Как ведет себя кожа в течение дня?",
      "images": [
        {
          "value": "a",
          "src": "https://aravia.ru/skin-test/img/questions/2a.jpg?v=1",
          "text": "Не очень хорошо. Жирный блеск на всем лице возникает через 2–3 часа после умывания"
        },
        {
          "value": "b",
          "src": "https://aravia.ru/skin-test/img/questions/2b.jpg?v=1",
          "text": "Хорошо. Жирный блеск может появиться только ближе к середине дня или к вечеру"
        },
        // Add other images as needed
      ]
    },
    // Add other questions as needed
  ]
};

export default {
  data() {
    return {
      currentQuestionIndex: 0,
      selectedAnswers: {},
      loading: false, // Инициализируйте состояние loading
    };
  },
  computed: {
    ...mapGetters(['getQuestions']),
    currentQuestion() {
      return this.getQuestions[this.currentQuestionIndex] || {};
    },
  },
  methods: {
    // ... rest of the methods
  },
  mounted() {
    this.$store.dispatch('fetchQuestions', localStorage.getItem('token'));
  },
};

</script>