<template>
  <div class="container mt-4">
    <h2><i class="fas fa-chart-line"></i> Средний чек на пользователей</h2>

    <!-- Диаграмма -->
    <div class="chart-container" style="position: relative; height:40vh; width:80vw">
      <canvas id="barChart"></canvas>
    </div>

    <div v-if="report.length" class="mt-4">
      <table class="table table-striped">
        <thead>
        <tr>
          <th><i class="fas fa-user"></i> Пользователь</th>
          <th><i class="fas fa-dollar-sign"></i> Средний чек</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="item in report" :key="item.user">
          <td>{{ item.user }}</td>
          <td>${{ item.average_order_value.toFixed(2) }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  data() {
    return {
      report: []
    };
  },
  methods: {
    fetchAverageOrderValuePerUser() {
      axios.get('http://127.0.0.1:8000/api/report/AverageOrderValuePerUser', {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(response => {
            this.report = response.data;
            this.createBarChart();
          })
          .catch(error => {
            console.error('Ошибка при запросе среднего чека на пользователя:', error);
          });
    },
    createBarChart() {
      const ctx = document.getElementById('barChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.report.map(item => item.user),
          datasets: [{
            label: 'Средний чек',
            data: this.report.map(item => item.average_order_value),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          },
          responsive: true,
          maintainAspectRatio: false
        }
      });
    }
  },
  created(){
    this.fetchAverageOrderValuePerUser();
  }
};
</script>

<style scoped>
.chart-container {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
