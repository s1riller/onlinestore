<script>
import axios from "axios";
import user from "@/store/modules/User";
import {url_server} from "@/main";
export default {
  data() {
    return {
      data: null,
      users: null,
    }
  },
  created() {

    console.log(this.$route.params.id)
    this.fetchProductRatings();
    this.fetchUserData();
  },
  methods: {
    async fetchProductRatings() {
      try {
        const response = await axios.get(`http://localhost:8000/api/report/User/${this.$route.params.id}/rated-products/`, {
              headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`
              }
            }

        );

        console.log('Rating updated successfully:', response.data);

        this.data = response.data.map(item => {

          item.product.img = `http://localhost:8000${item.product.img}`;
          return item;
        });
      } catch (error) {
        console.error('Error updating rating:', error);
      }
    },
    async fetchUserData(){
      try {
        const response = await axios.get(`http://${url_server}:8000/api/report/Users`, {
              headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`
              }
            }
        );

        console.log('Rating updated successfully:', response.data);
        this.users = response.data
      } catch (error) {
        console.error('Error updating rating:', error);
      }
    },
    getUserData(id){
      return this.users.find(user => user.id === id);
    }
    }
}
</script>

<template>
  <div class="products-container">
    <div v-for="(item, index) in data" :key="index" class="product-card">
      <div class="product-image">
        <img :src="item.product.img" :alt="item.product.name">
      </div>
      <div class="product-info">
        <h3 class="product-name">{{ item.product.name }}</h3>
        <p class="product-description">{{ item.product.description }}</p>
        <div class="product-details">
          <span class="product-price">{{ item.product.price }} ₽</span>
          <span class="product-rating">Рейтинг: {{ item.rating }} / 5</span>
        </div>
      </div>
    </div>
    <div v-if="data && data.length === 0" class="no-ratings">
      <p>Ещё не оценил ни одного продукта.</p>
    </div>
  </div>
</template>


<style scoped>
.products-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.product-card {
  width: 300px;
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.product-image {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px; /* Высота блока, можно изменить по желанию */
  overflow: hidden;
}

.product-image img {

  max-width: 200%;
  max-height: 200%;
  object-fit: cover;
}


.product-info {
  padding: 15px;
}

.product-name {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.product-description {
  font-size: 14px;
  color: #666;
}

.product-details {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.product-price {
  font-weight: bold;
  color: #4CAF50;
}

.product-rating {
  background-color: #FFC107;
  color: #fff;
  padding: 3px 8px;
  border-radius: 5px;
}

.no-ratings {
  text-align: center;
  padding: 20px;
  font-size: 16px;
  color: #666;
}
</style>