import axios from 'axios';
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

const state = {
    followersList: [],
};

const getters = {
    allFollowerList: state => state.followersList,

};

const mutations = {
    setFollowerList: (state, followersList) => (state.followersList=followersList),
};

const actions = {
    async fetchFollowingUser({ commit }){
        let token = localStorage.getItem('token')
        const response = await axios.get(Link+'/AllProfile/following_list/', {headers: {Authorization: `Token ${token}`}})
        commit('setFollowerList', response.data);
    },
};


export default {
    state,
    getters,
    actions,
    mutations
}