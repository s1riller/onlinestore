<template>
  <div class="p-5">
    <h1>Отчеты интернет-магазина</h1>

    <!-- Категория: Продажи -->
    <h2>Продажи</h2>

    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'ListSoldProduct' })">
              <h3 class="card-title">Список проданных товаров</h3>
            </button>
            <!-- Здесь можно вставить графики или данные о продажах -->
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'VolumeOfSales' })">
            <h3 class="card-title">Общий объем продаж</h3>
            </button>
            <!-- Здесь можно вставить графики или данные о продажах -->
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'FinancialReport' })">
              <h3 class="card-title">Финансовый отчет</h3>
            </button>
            <!-- Здесь можно вставить графики или данные о продажах -->
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'SalesByCategory' })">
              <h3 class="card-title">Сравнение продаж по категориям</h3>
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">

            <!-- Здесь можно вставить графики или данные о среднем чеке -->
            <button class="btn" @click="$router.push({ name: 'AverageOrderValuePerUser' })">
              <h3 class="card-title">Средний чек покупателей</h3>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Категория: Клиенты -->
    <h2>Клиенты</h2>
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'UsersList' })">
              <h3 class="card-title"> Список пользователей</h3>
            </button>
          </div>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <button class="btn" @click="$router.push({ name: 'UserTestResultsReport' })">
              <h3 class="card-title"> Отчет о результатах пользовательских тестов и предпочтениях</h3>
            </button>
          </div>
        </div>
      </div>
<!--      <div class="col-md-4">-->
<!--        <div class="card">-->
<!--          <div class="card-body">-->
<!--            <h3 class="card-title">Источники трафика</h3>-->
<!--            &lt;!&ndash; Здесь можно вставить графики или данные об источниках трафика &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-md-4">-->
<!--        <div class="card">-->
<!--          <div class="card-body">-->
<!--            <h3 class="card-title">Отзывы клиентов</h3>-->
<!--            &lt;!&ndash; Здесь можно вставить отзывы клиентов &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
    </div>

    <!-- Категория: Маркетинг -->
<!--    <h2>Маркетинг</h2>-->
<!--    <div class="row">-->
<!--      <div class="col-md-4">-->
<!--        <div class="card">-->
<!--          <div class="card-body">-->
<!--            <h3 class="card-title">Эффективность рекламных кампаний</h3>-->
<!--            &lt;!&ndash; Здесь можно вставить графики или данные о рекламных кампаниях &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-md-4">-->
<!--        <div class="card">-->
<!--          <div class="card-body">-->
<!--            <h3 class="card-title">ROI по рекламным кампаниям</h3>-->
<!--            &lt;!&ndash; Здесь можно вставить графики или данные о ROI &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-md-4">-->
<!--        <div class="card">-->
<!--          <div class="card-body">-->
<!--            <h3 class="card-title">Эффективность электронной почты</h3>-->
<!--            &lt;!&ndash; Здесь можно вставить графики или данные о письмах и рассылках &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
  </div>
</template>

<script setup>

</script>

<style scoped>
/* Стили для заголовков */
h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

h2 {
  font-size: 20px;
  margin-top: 30px;
  margin-bottom: 10px;
}

/* Стили для карточек */
.card {
  margin-bottom: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 18px;
  margin-bottom: 10px;
}

/* Стили для отступов */
.p-5 {
  padding: 5%;
}
</style>
