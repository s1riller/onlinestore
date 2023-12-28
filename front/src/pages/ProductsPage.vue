<template>
  <body class="mt-5 p-5">
  <div class="text-center">
    <section id="product1">
      <h2>Продукты</h2>
      <p>Для лечения заболеваний кожи лица</p>
<!--      <div class="pro-container">-->

<!--        <div class="row row-cols-5 row-cols-sm-5 row-cols-md-5 g-5">-->
<!--          <div class="col" v-for="(product, index) in productList" :key="index">-->
<!--            <div class="card shadow-sm h-100 d-flex flex-column">-->
<!--              <img :src="product.img" :alt="product.name" class="card-img-top">-->
<!--              <div class="card-body d-flex flex-column">-->
<!--                <p class="card-text">{{ product.description }}</p>-->
<!--                <h4>{{ product.name }}</h4>-->
<!--                <div class="mt-auto">-->
<!--                  <div class="btn-group">-->
<!--                    <button class="btn btn-primary btn-lg" type="button">Добавить в корзину</button>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->



<!--        &lt;!&ndash;        <div class="pro" v-for="(product, index) in productList" :key="index">&ndash;&gt;-->
<!--&lt;!&ndash;          <img :src="product.img" :alt="product.name">&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>{{ product.name }}</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <p>{{ product.description }}</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p>Лечит: {{ product.treats }} заболеваний</p>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--      </div>-->


      <section class="w-100  p-4" style="background-color: #eee; border-radius: .5rem .5rem 0 0;">

        <div class="row justify-content-center mb-3" v-for="(product, index) in productList" :key="index">
          <div class="col-md-12">
            <div class="card shadow-0 border rounded-3">
              <div class="card-body">
                <div class="row">
                  <div class="col-md-12 col-lg-3 col-xl-3 mb-4 mb-lg-0">
                    <div class="bg-image hover-zoom ripple rounded ripple-surface">
                      <img :src="product.img" :alt="product.name" class="w-100">
                      <a href="#!">
                        <div class="hover-overlay">
                          <div class="mask" style="background-color: rgba(253, 253, 253, 0.15);"></div>
                        </div>
                      </a>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-6 col-xl-6">
                    <h5>{{ product.name }}</h5>
                    <div class="d-flex flex-row">
                      <div class="text-danger mb-1 me-2">
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                      </div>

                    </div>

                    <p class="text-truncate mb-4 mb-md-0">
                      {{ product.description }}
                    </p>

                  </div>
                  <div class="col-md-6 col-lg-3 col-xl-3 border-sm-start-none border-start">
                    <div class="d-flex flex-row align-items-center mb-1">
                      <h4 class="mb-1 me-1">$13.99</h4>
                      <span class="text-danger"><s>$20.99</s></span>
                    </div>
                    <h6 class="text-success">Free shipping</h6>
                    <div class="d-flex flex-column mt-4">
                      <button class="btn btn-primary btn-sm" type="button">Details</button>
                      <button class="btn btn-outline-primary btn-sm mt-2" type="button">
                        Add to wishlist
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div >
      </section>



      <div class="p-4 text-center border-top mobile-hidden">
        <a class="btn btn-link px-3" data-mdb-toggle="collapse" href="#example3" role="button" aria-expanded="false" aria-controls="example3" data-ripple-color="hsl(0, 0%, 67%)">
          <i class="fas fa-code me-md-2"></i>
          <span class="d-none d-md-inline-block">
          Show code
        </span>
        </a>


        <a class="btn btn-link px-3 " data-ripple-color="hsl(0, 0%, 67%)">
          <i class="fas fa-file-code me-md-2 pe-none"></i>
          <span class="d-none d-md-inline-block export-to-snippet pe-none">
            Edit in sandbox
          </span>
        </a>

      </div>



    </section>
  </div>
  </body>
</template>


<script>
import {mapGetters} from "vuex";

export default {

  computed: {
    ...mapGetters( [
      'getProductList', // Имя вашего геттера из модуля
    ]),
    productList() {
      console.log("231")
      return this.getProductList;
    },
  },
  mounted() {
    this.$store.dispatch('fetchMedicines');
  },

};
</script>
<style scoped>

</style>
