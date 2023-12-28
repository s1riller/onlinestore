<template>
  <div class="container">
    <div v-if="!report" class="row">
      <div class="col-md-6 offset-md-3">
        <div class="form-group">
          <label class="text-dark" for="start_date">Выберите начальную дату:</label>
          <input id="start_date" v-model="start_date" class="form-control" required type="datetime-local"/>
        </div>

        <div class="form-group">
          <label class="text-dark" for="end_date">Выберите конечную дату:</label>
          <input id="end_date" v-model="end_date" class="form-control" required type="datetime-local"/>
        </div>

        <button class="btn btn-primary" @click="fetchReportData()">Сформировать отчет</button>
      </div>
    </div>

    <div v-if="report" class="row mt-4">
      <div class="col-md-6 offset-md-3">

        <button class="btn btn-primary" @click="clearReport()">Новый отчет</button>
      </div>
      <div class="col-md-6 offset-md-3">
        <h1>Отчет о заказах</h1>
        <p>Начальная дата: {{ report.start_date }}</p>
        <p>Конечная дата: {{ report.end_date }}</p>
        <p>Суммарная стоимость заказов: ${{ report.total_sales }}</p>
        <p>Количество заказов: {{ report.total_orders }}</p>
        <p>Средний размер заказа: ${{ report.average_order_size }}</p>

        <h2>Список заказов:</h2>
        <ul>
          <li v-for="order in report.orders" :key="order.id">
            <h3>Заказ №{{ order.id }}</h3>
            <p>Пользователь: {{ order.full_name }}</p>
            <div class="dropdown">
              <button class="dropbtn">Продуктов {{order.order_items.length}}</button>
              <div class="dropdown-content">
                <div v-for="item in order.order_items" :key="item.product.id">
                  <p>{{ item.product.name }} Цена: ${{ item.product.price }} Количетсво: {{ item.quantity }} </p>
                  <p>Сумма ${{getOrderPrice(item.product.price, item.quantity)}}</p>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      report: null,  // Здесь будут храниться данные отчета
      start_date: null,
      end_date: null,
    };
  },
  mounted() {
    // В этом методе вы можете сделать запрос к серверу для получения данных отчета
    // Например, с использованием библиотеки Axios
    this.fetchReportStartEndDate();
  },
  methods: {
    getOrderPrice(q,p){
      return q*p
    },
    clearReport() {
      this.report = null
    },
    formatDate(tdate) {
      const date = new Date(tdate);

// Получите год, месяц и день
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // Добавляем ведущий ноль, если месяц < 10
      const day = String(date.getDate()).padStart(2, '0'); // Аналогично для дня

      return `${year}-${month}-${day}`
    },
    fetchReportStartEndDate() {
      axios.get('http://127.0.0.1:8000/api/report/Summary',
          {
            headers: {
              'Authorization': `Token ${localStorage.getItem('token')}`
            }
          })
          .then(response => {
            this.start_date = response.data.first_date;
            this.end_date = response.data.last_date;
          })
          .catch(error => {
            console.error('Ошибка при запросе данных отчета:', error);
          });
    },
    fetchReportData() {
      // Здесь делайте запрос к серверу, чтобы получить данные отчета

      axios.post('http://127.0.0.1:8000/api/report/Summary', {
        start_date: this.formatDate(this.start_date),
        end_date: this.formatDate(this.end_date)
      }, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(response => {
            this.report = response.data;
          })
          .catch(error => {
            console.error('Ошибка при запросе данных отчета:', error);
          });
    },
  },
};
</script>

<style scoped>
/* Кнопка выпадающего списка */
.dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

/* Контейнер <div> - необходим для размещения выпадающего содержимого */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Выпадающее содержимое (скрыто по умолчанию) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Ссылки внутри выпадающего списка */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Изменение цвета выпадающих ссылок при наведении курсора */
.dropdown-content a:hover {background-color: #ddd;}

/* Показать выпадающее меню при наведении курсора */
.dropdown:hover .dropdown-content {display: block;}

/* Изменение цвета фона кнопки раскрывающегося списка при отображении содержимого раскрывающегося списка */
.dropdown:hover .dropbtn {background-color: #3e8e41;}
</style>
