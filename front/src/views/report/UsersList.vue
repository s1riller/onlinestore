<template>
  <div v-if="!isLoading">
    <div id="sortable" aria-dropeffect="move" class="list list-row card" data-sortable-id="0">
      <div
          v-for="user in users" :key="user.id" class="list-item"
          draggable="true"
          style=""
      >
        <div><a data-abc="true" href="#"><span class="w-40 avatar gd-primary"><img
            :src="user.avatar_url" alt="."></span></a></div>
        <div class="flex">
          <!-- Добавлена проверка на наличие user перед попыткой чтения first_name или last_name -->
          <a v-if="user" class="item-author text-color" data-abc="true" href="#">{{ user.first_name }} {{
              user.last_name
            }}</a>
          <a v-if="user && !user.first_name || !user.last_name" class="item-author text-color" data-abc="true" href="#">Не
            знаем как зовут пользователя</a>
          <div class="item-except text-muted text-sm h-1x">
          <span class="material-icons">
            alternate_email
          </span>
            {{ user.username }}
            {{ ageInfo(user.birth_date) }}
          </div>

        </div>
        <div class="no-wrap">
          <div class="item-date text-muted text-sm d-none d-md-block"> Последнее действие:
            {{ lastLoginInfo(user.last_login) }}
          </div>
        </div>
        <div>
          <div class="item-action dropdown">
            <a class="text-muted" data-abc="true" data-toggle="dropdown" href="#">
              <svg class="feather feather-more-vertical" fill="none" height="16" stroke="currentColor"
                   stroke-linecap="round"
                   stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="16"
                   xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="1"></circle>
                <circle cx="12" cy="5" r="1"></circle>
                <circle cx="12" cy="19" r="1"></circle>
              </svg>
            </a>
            <div class="dropdown-menu dropdown-menu-right bg-black" role="menu">
              <a class="dropdown-item" data-abc="true" href="#">See detail </a><a class="dropdown-item download"
                                                                                  data-abc="true">Download </a><a
                class="dropdown-item edit" data-abc="true">Edit</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item trash" data-abc="true">Delete item</a>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>

  <div v-else>
    <h1>Загружаем данные</h1>
  </div>
</template>

<script>

import axios from "axios";
import {differenceInCalendarYears, formatDistanceToNow, parseISO} from 'date-fns';
import {ru} from 'date-fns/locale'; // Импортируйте локаль, если хотите локализовать вывод

export default {
  data() {
    return {
      users: [],
      isLoading: true
    };
  },
  methods: {
    fetchUsers() {
      axios.get('http://127.0.0.1:8000/api/report/Users') // Замените URL_API_ПОЛЬЗОВАТЕЛЕЙ на фактический URL вашего API
          .then(response => {
            this.isLoading = false;
            this.users = [...response.data];
          })
          .catch(error => {
            console.error("Ошибка при получении данных о пользователях:", error);
          });
    },
    lastLoginInfo(lastLogin) {
      const loginDate = parseISO(lastLogin);
      return formatDistanceToNow(loginDate, {addSuffix: true, locale: ru}); // Используйте 'ru' для русского языка
    },
    ageInfo(date) {
      if (date) {
        const age = differenceInCalendarYears(new Date(), parseISO(date));
        return `${age} ${this.getAgeWord(age)}`;
      }
    },
    getAgeWord(age) {
      let lastDigit = age % 10;
      let lastTwoDigits = age % 100;

      if (lastTwoDigits >= 11 && lastTwoDigits <= 14) {
        return 'лет';
      }

      switch (lastDigit) {
        case 1:
          return 'год';
        case 2:
        case 3:
        case 4:
          return 'года';
        default:
          return 'лет';
      }
    },

  },
  created() {
    this.fetchUsers()
  }
};
</script>


<style scoped>

body {
  background-color: #f9f9fa
}

.flex {
  -webkit-box-flex: 1;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto
}

@media (max-width: 991.98px) {
  .padding {
    padding: 1.5rem
  }
}

@media (max-width: 767.98px) {
  .padding {
    padding: 1rem
  }
}

.padding {
  padding: 5rem
}

.card {
  background: #fff;
  border-width: 0;
  border-radius: .25rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, .05);
  margin-bottom: 1.5rem
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(19, 24, 44, .125);
  border-radius: .25rem
}

.list-item {
  position: relative;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word
}

.list-item.block .media {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0
}

.list-item.block .list-content {
  padding: 1rem
}

.w-40 {
  width: 40px !important;
  height: 40px !important
}

.avatar {
  position: relative;
  line-height: 1;
  border-radius: 500px;
  white-space: nowrap;
  font-weight: 700;
  border-radius: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: center;
  justify-content: center;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  border-radius: 500px;
  box-shadow: 0 5px 10px 0 rgba(50, 50, 50, .15)
}

.avatar img {
  border-radius: inherit;
  width: 100%
}

.gd-primary {
  color: #fff;
  border: none;
  background: #448bff linear-gradient(45deg, #448bff, #44e9ff)
}

.flex {
  -webkit-box-flex: 1;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto
}

.text-color {
  color: #5e676f
}

.text-sm {
  font-size: .825rem
}

.h-1x {
  height: 1.25rem;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical
}

.no-wrap {
  white-space: nowrap
}

.list-row .list-item {
  -ms-flex-direction: row;
  flex-direction: row;
  -ms-flex-align: center;
  align-items: center;
  padding: .75rem .625rem;
}

.list-item {
  position: relative;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-direction: column;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
}

.list-row .list-item > * {
  padding-left: .625rem;
  padding-right: .625rem;
}

.dropdown {
  position: relative;
}

a:focus, a:hover {
  text-decoration: none;
}

list-item {
  background: white;
}

.user-list-enter-active, .user-list-leave-active {
  transition: opacity 2.5s;
}
.user-list-enter, .user-list-leave-to /* .user-list-leave-active в версии 2.1.8+ */ {
  opacity: 0;
}

</style>