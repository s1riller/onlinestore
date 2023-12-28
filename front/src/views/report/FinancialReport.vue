<template>
  <div class="container mt-4">
    <h2>Финансовый отчет</h2>
    <div v-if="report">
      <p><strong>Общий объем продаж:</strong> ${{ report.total_sales }}</p>
      <p><strong>Общая стоимость доставки:</strong> ${{ report.total_delivery_fees }}</p>
      <p><strong>Средний размер заказа:</strong> ${{ report.average_order_value }}</p>
      <p><strong>Общее количество заказов:</strong> {{ report.total_orders }}</p>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      report: null
    };
  },
  methods: {
    fetchFinancialReport() {
      axios.get('http://127.0.0.1:8000/api/report/FinancialReportAPIView',{
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(response => {
            this.report = response.data;
          })
          .catch(error => {
            console.error('Ошибка при запросе финансового отчета:', error);
          });
    }
  },
  created() {
    this.fetchFinancialReport()
  }
};
</script>

<style>
/* Добавьте необходимые стили */
</style>
