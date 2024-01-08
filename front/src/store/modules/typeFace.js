

import {url_server} from "@/main";
export default {
    namespaced: true,
    actions: {
        async fetchTypeFaces({ commit }) {
            const res = await fetch(`http://${url_server}:8000/api/skintypes/`);
            const typeFaces = await res.json();

            commit('updateTypeFaces', typeFaces); // Обратите внимание на исправленное имя мутации
        },
    },
    mutations: {
        updateTypeFaces(state, typeFaces) {
            state.typeFace = typeFaces;
        },
    },
    state:{
        typeFace:[]
    },
    getters: {
        allTypeFaces(state) {
            return state.typeFace;
        },
    },


}