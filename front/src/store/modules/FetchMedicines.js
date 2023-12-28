// store.js
import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

export default({
    state: {
        productList: [],
    },
    getters: {
        getProductList: (state) => state.productList,
    },
    mutations: {
        setProductList(state, productList) {
            state.productList = productList;
        },
    },

    actions: {
        async fetchMedicines({ commit }) {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/medicines/', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`,
                    },
                });
                const data = await response.data;

                commit('setProductList', data);
            } catch (error) {
                console.error('Error fetching medicines:', error);
            }
        },
    },
});