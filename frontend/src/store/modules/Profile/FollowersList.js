import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    followersList: [],
};

const getters = {
    allFollowersList: state => state.followersList,

};

const mutations = {
    setFollowersList: (state, followersList) => (state.followersList=followersList),
};

const actions = {
    async fetchFollowersList({ commit }){
        let token = localStorage.getItem('token')
        const response = await axios.get(Link+'/AllProfile/followers_list/', {headers: {Authorization: `Token ${token}`}})
        commit('setFollowersList', response.data.followers);
    },
};


export default {
    state,
    getters,
    actions,
    mutations
}