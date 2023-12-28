<template>
  <div class="container mt-4">
    <h2>Отчет о результатах пользовательских тестов</h2>

    <div class="card my-3">
      <div class="card-body">
        <h3 class="card-title">Статистика предпочтений</h3>
        <table class="table table-striped">
          <thead>
          <tr>
            <th>Ответы</th>
            <th>Количество тестов</th>
            <th>Средний рейтинг</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="stat in report.preference_stats" :key="stat.answers">
            <td>
              <div v-for="(value, key) in parseAnswers(stat.answers)" :key="key">
                <strong>{{ key }}:</strong> {{ value.join(', ') }}
              </div>
            </td>
            <td>{{ stat.total }}</td>
            <td>{{ stat.average_rate }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="alert alert-info">
      <i class="fas fa-info-circle"></i>
      Общее количество тестов: {{ report.total_tests }}
    </div>

    <!-- Диаграмма (пример с использованием Chart.js) -->
    <div class="card my-3">
      <div class="card-body">
        <h3 class="card-title">Диаграмма предпочтений</h3>
        <canvas id="preferenceChart"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart } from 'chart.js';

export default {
  data() {
    return {
      report: {
        preference_stats: [],
        total_tests: 0
      }
    };
  },
  methods: {
    parseAnswers(answersJson) {
      try {
        const answersObj = answersJson;
        return answersObj;
      } catch (e) {
        console.error('Ошибка при разборе ответов:', e);
        return {};
      }
    },
    fetchUserTestResultsReport() {
      axios.get('http://127.0.0.1:8000/api/report/UserTestResultsReport', {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(response => {
            this.report = response.data;
            this.createChart();
          })
          .catch(error => {
            console.error('Ошибка при запросе отчета о результатах пользовательских тестов:', error);
          });
    },
    createChart() {
      const ctx = document.getElementById('preferenceChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar', // или другой тип диаграммы
        data: {
          labels: this.report.preference_stats.map(item => item.answers),
          datasets: [{
            label: 'Количество тестов',
            data: this.report.preference_stats.map(item => item.total),
            backgroundColor: 'rgba(54, 162, 235, 0.2)'
          }, {
            label: 'Средний рейтинг',
            data: this.report.preference_stats.map(item => item.average_rate),
            backgroundColor: 'rgba(255, 99, 132, 0.2)'
          }]
        }
      });
    }
  },
  mounted() {
    this.fetchUserTestResultsReport();
  }
};
</script>

<style scoped>
/* Добавьте необходимые стили */
</style>
