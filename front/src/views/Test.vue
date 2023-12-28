<template>
  <div class="d-flex bg-light vh-100">
    <div class="container">
      <div class="row">
        <div class="mx-auto">
          <div class="card bg-light text-dark d-flex justify-content-center align-items-center vh-100">
            <div v-if="currentQuestion" class="card-body">
              <h5 class="card-title text-dark text-center">{{ currentQuestion.question }}</h5>
              <div class="d-flex flex-row align-items-center justify-content-center">
                <div v-for="answer in currentQuestion.answers" :key="answer.id" class="mx-2">
                  <button type="button" class="btn" @click="selectAnswer(answer.text)">
                    <img :src="answer.img" alt="" class="img-fluid rounded" style="width: 230px; height: 300px;" />
                    <h5 class="mt-2 text-center">{{ answer.text }}</h5>
                  </button>
                </div>
              </div>
            </div>
            <div v-else class="card-body">
              <div v-if="loading" class="loader-overlay">
                <div class="loader">Анализируем ответы...</div>
              </div>
              <p class="card-text">Тест пройден</p>
              <p class="card-text">Выбранные ответы: {{ formatSelectedAnswers }}</p>
              <div v-if="serverResponse">
                <p class="card-text">Ответ сервера: {{ serverResponse }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<!-- остальной код остается без изменений -->


<script>
import "@/static/discord.css";
import axios from "axios";

export default {
  data() {
    return {
      currentQuestionIndex: 0,
      selectedAnswers: {},
      loading: false,
      serverResponse: null,
      questions: [],
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex];
    },
    formatSelectedAnswers() {
      return Object.keys(this.selectedAnswers)
          .map((question) => `${question} ${this.selectedAnswers[question]}`)
          .join(" ");
    },
  },
  methods: {
    selectAnswer(value) {
      // Инициализируем массив ответов для текущего вопроса, если его еще нет
      if (!this.selectedAnswers[this.currentQuestion.question]) {
        this.selectedAnswers[this.currentQuestion.question] = [];
      }

      // Добавляем выбранный ответ в массив
      this.selectedAnswers[this.currentQuestion.question].push(value);

      // Переходим к следующему вопросу
      this.currentQuestionIndex++;

      if (this.currentQuestionIndex >= this.questions.length) {
        console.log("No more questions");
        // Выполните действия, когда больше нет вопросов
        this.submitAnswers()
      }
    },

    async getQuestions() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/questions/', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`,
          },
        });
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },
    async submitAnswers() {
      try {
        this.loading = true; // Установите loading в true перед началом загрузки

        // Запрос, чтобы получить id пользователя
        const profileResponse = await axios.get('http://127.0.0.1:8000/api/profile', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        const userId = profileResponse.data.id;

        // Фильтруем selectedAnswers, чтобы удалить null значения
        const cleanedAnswers = {};
        for (const key in this.selectedAnswers) {
          if (this.selectedAnswers[key] !== null) {
            cleanedAnswers[key] = this.selectedAnswers[key];
          }
        }

        const results = {
          user: userId, // Отправляем id пользователя
          answers: cleanedAnswers, // Отправляем выбранные ответы без null
          time: new Date().toISOString().slice(11, 23),
        };

        const response = await axios.post('http://127.0.0.1:8000/api/user_test_results/', results, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        await new Promise((resolve) => {
          setTimeout(resolve, 10000);
        });
        this.loading = false; // Завершите загрузку, установив loading в false
        this.$router.replace({ name: 'Account' });


        setTimeout(() => {
          window.location.reload();
        }, 100);
      } catch (error) {
        this.loading = false; // Установите loading в false в случае ошибки
        console.error(error);
      }
    },
  },
  created() {
    this.getQuestions();
  },
};
</script>
<style>
.loader-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it's above other content */
}

.loader {
  font-size: 2em;
  color: #333;
}
</style>
