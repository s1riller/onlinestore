<template>
  <div class="date-range">
    <label for="startDate">Начальная дата:</label>
    <input type="date" id="startDate" v-model="startDate" @change="filterByDateRange" />
  </div>
  <div class="date-range">
    <label for="endDate">Конечная дата:</label>
    <input type="date" id="endDate" v-model="endDate" @change="filterByDateRange" />
  </div>
  <table id="fifthTable">
    <thead>
    <tr>
      <th v-for="col in columns" :key="col" @click="sortTable(col)">
        {{ columnNames[col] || col }}
      </th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="row in filteredRows" :key="row.id">
      <td>{{ row.product_description}}</td>
      <td>{{ row.product_name }}</td>

      <td class="number">{{ row.product_price}}</td>
      <td>{{ row.product_category}}</td>

      <td class="number">{{ row.quantity}}</td>


      <td>{{ formatDate(row.sale_date)}}</td>
      <td><img :src="row.product_image_url" alt="Product Image" class="product-image"></td>
    </tr>
    </tbody>
    <tfoot>
    <tr>
      <td >Общие итоги</td>
      <td></td>
      <td>${{ totalPrice }}</td>
      <td></td>

      <td class="number">{{ totalQuantity }} шт.</td>



    </tr>
    <tr>
      <td>Общая сумма продаж</td> <td></td> <td></td> <td></td> <td></td> <td></td>
      <td>${{ totalRevenue }}</td>
    </tr>
    </tfoot>
  </table>
</template>

<script>
import { defineComponent } from 'vue';
import axios from "axios";

export default defineComponent({
  name: 'FifthTable',
  data() {
    return {
      ascending: false,
      sortColumn: '',
      soldProducts:[],
      columnNames: {
        'product_name': 'Название продукта',
        'product_description': 'Описание',
        'product_price': 'Цена',
        'product_category': 'Категория',
        'quantity': 'Количество',
        'sale_date': 'Дата продажи',
        'product_image_url': 'Изображение продукта',
        // Add other column mappings as needed
      },
      startDate: '', // Начальная дата для фильтрации
      endDate: '', // Конечная дата для фильтрации
      filteredRows: [],
      rows: [

      ]
    };
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toISOString().split('T')[0];
    },
    fetchSoldProducts() {
      axios
          .get('http://127.0.0.1:8000/api/report/SoldProducts', {
            headers: {
              Authorization: `Token ${localStorage.getItem('token')}`,
            },
          })
          .then((response) => {
            this.rows = response.data;
            const saleDates = this.rows.map((row) => new Date(row.sale_date));
            const minDate = new Date(Math.min(...saleDates));
            const maxDate = new Date(Math.max(...saleDates));
            // Устанавливаем их как начальную и конечную даты по умолчанию
            this.startDate = this.formatDate(minDate);
            this.endDate = this.formatDate(maxDate);
            // Фильтруем данные при загрузке
            this.filterByDateRange();
          })
          .catch((error) => {
            console.error('Error fetching the sold products:', error);
          });
    },
    sortTable(col) {
      if (this.sortColumn === col) {
        this.ascending = !this.ascending;
      } else {
        this.ascending = true;
        this.sortColumn = col;
      }

      this.filteredRows.sort((a, b) => {
        if (a[col] > b[col]) {
          return this.ascending ? 1 : -1;
        } else if (a[col] < b[col]) {
          return this.ascending ? -1 : 1;
        }
        return 0;
      });
    },
    groupProducts() {
      const groupedProducts = [];
      this.soldProducts.forEach((product) => {
        const existingProduct = groupedProducts.find((p) => p.product_name === product.product_name);
        if (existingProduct) {
          // Продукт с таким названием уже существует, обновляем данные
          existingProduct.quantity += product.quantity;
          existingProduct.totalPrice += product.quantity * parseFloat(product.product_price);
        } else {
          // Продукт с таким названием не найден, добавляем новый продукт
          groupedProducts.push({
            product_name: product.product_name,
            product_description: product.product_description,
            product_category: product.product_category,
            quantity: product.quantity,
            totalPrice: product.quantity * parseFloat(product.product_price),
            sale_date: product.sale_date,
            product_image_url: product.product_image_url,
          });
        }
      });
      this.filterByDateRange = groupedProducts;
    },
    filterByDateRange() {
      console.log("Sort")
      const filteredRows = this.rows.filter((row) => {
        const saleDate = new Date(row.sale_date);
        return (
            (!this.startDate || saleDate >= new Date(this.startDate)) &&
            (!this.endDate || saleDate <= new Date(this.endDate))
        );
      });
      this.filteredRows = filteredRows;
    },
  },
  mounted() {
    this.fetchSoldProducts();
  },
  computed: {
    totalRevenue() {
      return this.filteredRows.reduce(
          (total, row) => total + row.quantity * parseFloat(row.product_price),
          0
      ).toFixed(2);
    },
    totalQuantity() {
      return this.filteredRows.reduce((total, row) => total + row.quantity, 0);
    },
    totalPrice() {
      return this.filteredRows.reduce(
          (total, row) => total + parseFloat(row.product_price),
          0
      ).toFixed(2);
    },
    columns() {
      if (this.rows.length === 0) {
        return [];
      }
      return Object.keys(this.rows[0]);
    },
  },
  watch: {
    startDate(newStartDate) {
      this.filterByDateRange();
    },
    endDate(newEndDate) {
      this.filterByDateRange();
    },
  },
});
</script>

<style>
.table-container {
  overflow-x: auto; /* Enables horizontal scrolling for smaller screens */
}

table {
  font-family: 'Open Sans', sans-serif;
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ccc;
  margin: 10px auto;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ccc;
}

th {
  background-color: #f4f4f4;
  cursor: pointer;
}

th:hover {
  background-color: #e0e0e0;
}

.arrow-up, .arrow-down {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 5px;
  vertical-align: middle;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
}

.arrow-up {
  border-bottom: 5px solid #666;
}

.arrow-down {
  border-top: 5px solid #666;
}

.product-image {
  width: 50px;
  height: auto;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.product-image {
  width: 50px;
  height: auto;
  transition: transform 0.3s ease; /* Smooth transition for zoom effect */
}

.product-image:hover {
  transform: scale(5.5); /* Adjust the scale value as needed */
  cursor: pointer;
}

/* Выравниваем числовые данные по правой стороне */
td.number {
  text-align: right;
}
</style>

