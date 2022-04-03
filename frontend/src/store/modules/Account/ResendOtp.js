import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;


const state = {
    IsSendOtp: ''
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
    ReSentOtp: ({commit}) => {
        return new Promise((resolve, reject) => {
            axios.post(Link+`/Account/user_New_Otp/${localStorage.getItem('UsId')}/`)
            .then((resp) => {
                if (resp.status === 200){
                    console.warn(resp.data)
                    commit('sendOtp_success', resp.data.id);
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