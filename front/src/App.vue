<template>
  <navbar/>
  <v-popup
      v-if="isInfoPopupVisible"
      @closePopup="closeInfoPopup"
      :popupName="popupName"
      :popupSize="popupSize"
      :firstName="this.first_name"
      :lastName="this.last_name"
  >
    <div class="position-relative">
      <h2>Введите</h2>
      <div class="mb-3">
        <input v-model="first_name" class="form-control" placeholder="Имя" required/>
      </div>
      <div class="mb-3">
        <input v-model="last_name" class="form-control" placeholder="Фамилия" required/>
      </div>
      <div>
      <span class="mb-3">
   <Calendar v-model="userData.originalDate" dateFormat="dd/mm/yy" placeholder="День рождения" required/>
</span>
      </div>
    </div>

  </v-popup>
<!--  <button @click="showPopupInfo">Показать окно</button>-->
  <div class="app">

    <router-view></router-view>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

  </div>
</template>

<script>

import navbar from "@/components/navbar";
import Calendar from 'primevue/calendar';
import "@/static/css/style.css";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import vPopup from "@/components/popup/v-popup.vue"
import {mapGetters, mapActions, mapState, mapMutations} from 'vuex'
import {} from 'vuex'
import axios from "axios";

export default {
  name: "app",
  components: {
    navbar,
    vPopup,
    Calendar
  },
  data() {
    return {
      isInfoPopupVisible: false,
      popupName: "Не нашли вашы данные, пожтому давайте познакомимся",
      popupSize: {width: '700px', height: '500px'},
      first_name:"",
      last_name: "",
      userData: {
        originalDate: null,
        formattedDate: null,
      },

    }
  },
  methods: {
    formatDate(date) {
      if (!date) return null;
      const d = new Date(date);
      let month = '' + (d.getMonth() + 1);
      let day = '' + d.getDate();
      const year = d.getFullYear();

      if (month.length < 2) month = '0' + month;
      if (day.length < 2) day = '0' + day;

      return [year, month, day].join('-');
    },
    showPopupInfo() {
      this.isInfoPopupVisible = true
      document.body.classList.add('no-scroll'); // Добавление класса для предотвращения прокрутки


    },
    async closeInfoPopup() {
      // if (!this.first_name || !this.last_name || !this.userData.formattedDate) {
      //   alert('Пожалуйста, заполните все поля.');
      //   return;
      // }

      this.isInfoPopupVisible = false
      // console.log(,this.userData)
      try {
        const response = await axios.put('http://127.0.0.1:8000/api/profile', {
          "first_name": this.first_name,
          "last_name": this.last_name,
          "birth_date": this.userData.formattedDate,
        }, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });

      } catch (error) {
        console.error('Ошибка отправки данных APP.vue', error);
      } finally {
        this.loading = false; // Вне зависимости от результата запроса, устанавливаем флаг загрузки в false
      }

    },
    ...mapActions(['fetchUserDataStore']),
    ...mapGetters(['getUserDataProfile'])
  },
  created() {

  },

  computed: {
    formattedDate() {
      this.userData.formattedDate = this.formatDate(this.userData.originalDate);
      return this.formatDate(this.userData.originalDate);
    },
  },
  mounted() {
    this.fetchUserDataStore();
    setTimeout(() => {
      //console.log(this.getUserDataProfile());
      if(localStorage.getItem('token')!=null){}
      if (!this.getUserDataProfile().first_name || !this.getUserDataProfile().last_name ) {
        this.isInfoPopupVisible = true
      }
    }, 5000);

  }


}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  font-family: "gg sans", sans-serif;

}

{
.no-scroll {
  overflow: hidden;
}

}
</style>
