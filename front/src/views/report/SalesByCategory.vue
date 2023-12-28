<template>
  <div class="container mt-4">
    <h2><i class="fas fa-chart-bar"></i> Отчет о продажах по категориям</h2>

    <!-- Круговая диаграмма -->
    <div class="chart-container" style="position: relative; height:40vh; width:80vw">
      <canvas id="pieChart"></canvas>
    </div>

    <div v-if="report.length" class="mt-4">
      <table class="table table-striped">
        <thead>
        <tr>
          <th><i class="fas fa-tags"></i> Категория</th>
          <th><i class="fas fa-dollar-sign"></i> Общий объем продаж</th>
          <th><i class="fas fa-boxes"></i> Общее количество</th>
          <th><i class="fas fa-shopping-cart"></i> Количество заказов</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="item in report" :key="item.category">
          <td>{{ item.category }}</td>
          <td>${{ item.total_sales }}</td>
          <td>{{ item.total_quantity }}</td>
          <td>{{ item.count }}</td>
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
    fetchSalesReportByCategory() {
      axios.get('http://127.0.0.1:8000/api/report/SalesReportByCategory', {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(response => {
            this.report = response.data;
            this.createBarChart();
            this.createPieChart();
          })
          .catch(error => {
            console.error('Ошибка при запросе отчета о продажах по категориям:', error);
          });
    },
    createBarChart() {
      // Создание столбчатой диаграммы
    },
    createPieChart() {
      const ctx = document.getElementById('pieChart').getContext('2d');
      new Chart(ctx, {
        type: 'pie',
        data: {
          labels: this.report.map(item => item.category),
          datasets: [{
            label: 'Продажи',
            data: this.report.map(item => item.total_sales),
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              // Добавьте больше цветов для каждой категории
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              // Добавьте больше цветов для каждой категории
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    }
  },
  created(){
    this.fetchSalesReportByCategory();
  }
};
</script>

<style scoped>
/* Кастомные стили для страницы и диаграмм */
.chart-container {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
