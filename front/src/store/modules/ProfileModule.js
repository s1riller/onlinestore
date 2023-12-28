// profileModule.js

import axios from 'axios';
import data from "bootstrap/js/src/dom/data";

export default {
    state:{
        user: {
            username: '', // Имя пользователя
            birth_date: '', // Дата рождения пользователя
            first_name: '', // Здесь будет храниться информация о пользователе
            last_name: '', // Здесь будет храниться информация о пользователе
        },
        error: null, // Ошибка, если есть
    },

   getters: {
       getUserName(state) {
           return state.user.username;
       },
       getUserDataProfile(state) {
           return state.user;
       }
   },

   mutations: {
        setUserData(state, userData) {
            state.user.username = userData.username;
            state.user.birth_date = userData.birth_date;
            state.user.first_name = userData.first_name;
            state.user.last_name = userData.last_name;

        },

    },

     actions: {
        async fetchUserDataStore({commit}) {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/profile', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`
                    }
                });
                // console.log(response.data)
                if (response.data) {
                    // console.log(response.data)
                    commit('setUserData',response.data)
                }
            } catch (error) {
                console.error(error);

            }
        },
    }
}