import axios from "axios";

export default {


    state: {
        userData:{
            id: null,
            birth_date: null,
            username: null,
            email: null,
            first_name: null,
            last_name: null,
            date_joined: null,
            is_admin: null,
        },
    },

    getters: {
        isAuthenticated(state) {
            return !!state.userData;
        },
        getUser(state) {
            return state.userData;
        },
        is_admin(state){
            return state.userData.is_admin
        },
    },

    mutations: {
        SET_USER_DATA(state, userData) {
            state.userData = userData;
        },
        CLEAR_USER_DATA(state) {
            state.userData = null;
        },
    },

    actions: {
        login({commit}, userData) {
            // здесь может быть код для аутентификации, например, запрос к API
            // после успешной аутентификации:
            commit('SET_USER_DATA', userData);
        },
        logout({commit}) {
            // здесь может быть код для выхода пользователя, например, запрос к API
            // после успешного выхода:
            commit('CLEAR_USER_DATA');
        },
        async fetchUserData({ commit }) {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/profile', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`
                    }
                });

                commit('SET_USER_DATA', response.data); // предполагая, что данные пользователя находятся в response.data
            } catch (error) {
                console.error('Ошибка при запросе данных о пользователе:', error);
                // Обрабатывайте ошибку соответствующим образом
            }
        },
    },
};
