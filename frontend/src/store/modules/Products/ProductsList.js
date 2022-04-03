import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    productssList: [],
};

const getters = {
    allProductsList: state => state.productssList,

};

const mutations = {
    setProductsList: (state, productssList) => (state.productssList=productssList),
};

const actions = {
    async fetchProductsList({ commit }){
        const response = await axios.get(Link+'/Products/')
        commit('setProductsList', response.data);
    },
};


export default {
    state,
    getters,
    actions,
    mutations
}