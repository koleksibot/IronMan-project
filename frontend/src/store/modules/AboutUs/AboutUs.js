import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    aboutUs: []
};

const getters = {
    allAboutUs: state => state.aboutUs
};

const actions = {
    async fetchAboutUs({ commit }){
        const response = await axios.get(Link+'/aboutUs/')
        commit('setAboutUs', response.data);
    }
};

const mutations = {
    setAboutUs: (state, aboutUs) => (state.aboutUs=aboutUs)
};

export default {
    state,
    getters,
    actions,
    mutations
};