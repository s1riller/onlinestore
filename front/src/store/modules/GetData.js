import axios from 'axios';

export default {
    state: {
        questions: [],

    },
    getters: {
        getQuestions(state) {
            return state.questions;
        },
        getQuestion(state){
            return state.questions.id
        }
    },
    mutations: {
        setQuestions(state, questions) {
            state.questions = questions;
        },
    },
    actions: {
        fetchQuestions({ commit, state }, token) {
            // Определяем заголовки для запроса, включая токен авторизации
            const headers = {
                Authorization: `Token ${token}`,
            };

            // Осуществляем GET-запрос к API для получения вопросов и ответов
            axios
                .get('http://127.0.0.1:8000/api/questions/', { headers })
                .then((response) => {
                    // Обновляем состояние с полученными данными
                    commit('setQuestions', response.data);
                })
                .catch((error) => {
                    console.error('Ошибка при запросе данных:', error);
                });
        },
    },
};
