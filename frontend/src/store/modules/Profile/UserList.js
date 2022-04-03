import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    userList: [],
};

const getters = {
    allUserList: state => state.userList,

};

const mutations = {
    setUserList: (state, userList) => (state.userList=userList),
};

const actions = {
    async fetchUserList({ commit }){
        let token = localStorage.getItem('token')
        const response = await axios.get(Link+'/AllProfile/users_list/', {headers: {Authorization: `Token ${token}`}})
        commit('setUserList', response.data);
    },
};


export default {
    state,
    getters,
    actions,
    mutations
}