import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    chatUserList: []
};

const getters = {
    allChatUserList: state => state.chatUserList

};

const mutations = {
    setChatUserList: (state, chatUserList) => (state.chatUserList=chatUserList),
};

const actions = {
    
    async fetchChatUserList({ commit }){
        let token = localStorage.getItem('token')
        const response = await axios.get(Link+'/chat/chat_userList/', {headers: {Authorization: `Token ${token}`}})
        commit('setChatUserList', response.data);
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}