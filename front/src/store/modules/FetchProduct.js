// store.js
import axios from "axios";
import {url_server} from "@/main";
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
        async fetchProducts({ commit }) {
            try {
                const response = await axios.get(`http://${url_server}:8000/api/medicines/`);
                const data = await response.data;
                commit('setProductList', data);
            } catch (error) {
                console.error('Error fetching medicines:', error);
            }
        },
    },
});