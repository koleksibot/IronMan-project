import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    profiledetails: []
};

const getters = {
    profileDetails: state => state.profiledetails
};

const mutations = {
    setprofileDetails: (state, profiledetails) => (state.profiledetails=profiledetails)
};
const actions = {
    async fetchProfileDetails({commit}){
        let token = localStorage.getItem('token')
        let id = localStorage.getItem('id')
        const response = await axios.get(`${Link}/AllProfile/profile_details/${id}/`, {headers: {Authorization: `Token ${token}`}})
        commit('setprofileDetails', response.data);
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};

