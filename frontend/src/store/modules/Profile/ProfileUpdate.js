import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    IsProfileUpdate: '',
};

const getters ={
};
const mutations = {
    profileUpdate_request(state){
        state.IsProfileUpdate = 'loading'
    },
    profileUpdate_success(state){
        state.IsProfileUpdate = 'success'
    },
    profileUpdate_error(state){
        state.IsProfileUpdate = 'error'
    },
};
const actions = {
    async ProfileUpdate({commit}, payload){
        let token = localStorage.getItem('token')
        // console.warn(token)
        // console.warn(payload)
        const response = await axios.put(`${Link}/AllProfile/profile_update/`, payload, {headers: {Authorization: `Token ${token}`}})
        commit('profileUpdate_success', response.data)
    },

}

export default {
    state,
    getters,
    actions,
    mutations,
}