import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;


const state = {
    IsSendOtp: '',
};

const getters ={
};
const mutations = {
    sedOtp_request(state){
        state.IsSendOtp = 'loading'
    },
    sendOtp_success(state){
        state.IsSendOtp = 'success'
    },
    sendOtp_error(state){
        state.IsSendOtp = 'error'
    },
};
const actions = {
    ForgotPassword: ({commit}, payload) => {
        return new Promise((resolve, reject) => {
            axios.post(Link+'/Account/forgotPassword_email/', payload)
            .then((resp) => {
                if (resp.status === 200){
                    console.warn(resp.data)
                    commit('sendOtp_success', payload);
                    resolve(resp);
                }
            })
            .catch(error => {
                console.warn(error)
                reject(error)
            })
        })
    },
    ChangePasswordFormSubmit: ({commit}, payload) => {
        return new Promise((resolve, reject) => {
            let id = localStorage.getItem('id')
            axios.post(Link+`/Account/forgot_Password_Change/${id}/`, payload)
            .then((resp) => {
                if (resp.status === 200){
                    console.warn(resp.data)
                    commit('sendOtp_success', payload);
                    resolve(resp);
                }
            })
            .catch(error => {
                console.warn(error)
                reject(error)
            })
        })
    },
    ChangePassword_Request:({commit}) =>{
        return new Promise((resolve, reject) =>{
            let token = localStorage.getItem('token')
            let id = localStorage.getItem('id')
            axios.get(Link+`/Account/authenticated_UserPassword_email/${id}/`, {headers: {Authorization: `Token ${token}`}})
            .then((resp) => {
                if (resp.status === 200){
                    console.warn(resp.data)
                    commit('sendOtp_success');
                    resolve(resp);
                }
            })
            .catch(error => {
                console.warn(error)
                reject(error)
            })

        })
    }

}

export default {
    state,
    getters,
    actions,
    mutations,
}