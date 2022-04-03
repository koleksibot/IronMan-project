import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    status: '' || localStorage.getItem('status'),
    Token: '' || localStorage.getItem('token'),
};

const getters ={
    isLoggedIn: state => !! state.Token,
    authStatus: state => state.status,
};
const mutations = {
    auth_request(state){
        state.status = 'loading'
    },
    auth_success(state, token, id, user){
        state.status = 'success'
        state.token = token
        state.id = id
        state.user = user
    },
    auth_error(state){
        state.status = 'error'
    },
    user_Logout(state){
        state.status = ''
        state.token = ''
    },
};
const actions = {
    Login: ({commit}, payload) =>{
        return new Promise((resolve, reject) => {
            commit('auth_request')
            axios.post(Link+'/Account/login/', payload)
            .then((resp) =>{
                if (resp.status === 200){
                    const token = resp.data.token
                    const id = resp.data.user_id
                    const auth_status = 'success'
                    localStorage.setItem('token', token)
                    localStorage.setItem('id', id)
                    localStorage.setItem('status', auth_status)
                    commit('auth_success', token, id, payload)
                    resolve(resp);
                }
            })
            .catch(error => {
                localStorage.removeItem('token')
                localStorage.removeItem('id')
                console.warn(error)
                reject(error);
            })
        })
    },
    LogOut: ({commit}) =>{
        return new Promise((resolve) =>{
            commit('user_Logout')
            localStorage.clear();
            resolve()
        })
    }

}

export default {
    state,
    getters,
    actions,
    mutations,
}