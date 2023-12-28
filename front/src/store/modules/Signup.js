import axios from 'axios';

export default {
    state: {
        birth_date: null,
        password: null,
        token: localStorage.getItem('token') || '',
        username: null, // Здесь будет храниться информация о пользователе
        first_name: null, // Здесь будет храниться информация о пользователе
        last_name: null, // Здесь будет храниться информация о пользователе
        error: null
    },
    getters: {
        getUserData(state){
            return {username:state.username,
                password:state.password,
            }
        },
        getError(state) {
            return state.error
        }
    },
    mutations: {
        setUserData(state, userData) {
            state.username = userData.username;
            state.password = userData.password;
            state.first_name = userData.first_name;
            state.last_name = userData.last_name;
        },
        setError(state,error){
            state.error = error
        },
        setToken(state, token){
            state.token = token
            localStorage.setItem('token', token); // Сохранить токен в локальное хранилище
        }

    },
    actions: {
        async SignupStore({ commit }, userData) {
            const { username, password, birth_date } = userData;
            console.log('Vuex - SignupStore',username, birth_date, password);

            try {
                // Регистрация пользователя
                const registrationResponse = await axios.post('http://127.0.0.1:8000/auth/users/', {
                    username: username,
                    birth_date: birth_date,
                    password: password,
                });

                commit('setUserData', userData);
                console.log('Успешная регистрация');
                commit('setError', 'Поздравляем! Успешная регистрация!');

                try {
                    // Авторизация пользователя
                    const loginResponse = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
                        username: username,
                        password: password,
                    });

                    if (loginResponse.data && loginResponse.data.auth_token) {
                        // Успешная авторизация
                        const token = loginResponse.data.auth_token;
                        // Здесь вы можете выполнить дополнительные действия, связанные с успешной авторизацией
                        // Например, сохранить токен в состоянии, если это требуется

                        commit('setToken', token); // Предположим, что у вас есть мутация setToken для сохранения токена
                        window.location.reload();

                    } else {
                        // Ошибка при авторизации
                        commit('setError', 'Произошла ошибка при авторизации после регистрации.');
                    }
                } catch (loginError) {
                    console.error(loginError);
                    commit('setError', 'Произошла ошибка при авторизации после регистрации.');
                }
            } catch (registrationError) {
                console.error(registrationError);
                commit('setError', 'Произошла ошибка при регистрации. Пожалуйста, проверьте данные и повторите попытку.');
            }
        },
        async LogoutStore({ commit }) {
            // Ваш код для выхода пользователя
            // Например, отправьте запрос на сервер для отмены текущего сеанса аутентификации
            // или удалите токен из локального хранилища и сбросьте состояние пользователя
            // После выхода пользователя перезагрузите страницу
            // Затем сбросьте состояние пользователя
            localStorage.removeItem('token'); // Удалить токен из локального хранилища
            commit('setToken', null); // Сбросить токен в состоянии
            commit('setUserData', { username: null, password: null }); // Сбросить данные пользователя
            commit('setError', null); // Очистить ошибки
            window.location.reload();
        },
        async LoginStore({ commit }, userData) {
            const { username, password } = userData;
            console.log(username,password);

            try {
                // Авторизация пользователя
                const loginResponse = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
                    username: username,
                    password: password,
                });

                if (loginResponse.data && loginResponse.data.auth_token) {
                    // Успешная авторизация
                    const token = loginResponse.data.auth_token;

                    // Сохранить токен в состоянии Vuex
                    commit('setToken', token); // Используйте соответствующую мутацию для сохранения токена

                    // Перезагрузить страницу после успешной авторизации
                    window.location.reload();
                } else {
                    // Ошибка при авторизации
                    commit('setError', 'Произошла ошибка при авторизации.');
                }
            } catch (loginError) {
                console.error(loginError);
                commit('setError', 'Произошла ошибка при авторизации.');
            }
        },

    },
};
