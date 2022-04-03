import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;


const state = {
    profileListDetails: []
};

const getters = {
    profileListDetails: state => state.profileListDetails
};

const mutations = {
    setprofileListDetails: (state, profileListDetails) => (state.profileListDetails=profileListDetails)
};
const actions = {
    async fetchProfileListDetails({commit}, id){
        let token = localStorage.getItem('token')
        const response = await axios.get(`${Link}/AllProfile/profile_details/${id}/`, {headers: {Authorization: `Token ${token}`}})
        commit('setprofileListDetails', response.data);
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};

