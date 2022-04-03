const state = {
    whereAmI: []
};

const getters = {
    getWhereAmI: state => state.whereAmI
};

const actions = {
    async fetchWhereAmI({ commit }, data){
        commit('setWhereAmI', data);
    }
};

const mutations = {
    setWhereAmI: (state, whereAmI) => (state.whereAmI=whereAmI)
};

export default {
    state,
    getters,
    actions,
    mutations
};