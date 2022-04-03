import Vuex from 'vuex';
import Vue from 'vue';


import WhereAmI from './modules/WhereAmI/WhereAmI'

import ProductList from './modules/Products/ProductsList';

import AboutUs from './modules/AboutUs/AboutUs'

import Login from './modules/Account/Login'
import ForgotPassword from './modules/Account/ForgotPassword';
import ReSendOtp from './modules/Account/ResendOtp';


import ProfileDetails from './modules/Profile/ProfileDetail';
import ProfileUpdate from './modules/Profile/ProfileUpdate';

import ProfileList from './modules/Profile/ProfileLIst';
import UserList from './modules/Profile/UserList';

import FollowersList from './modules/Profile/FollowersList';
import FollowingList from './modules/Profile/FollowingList';
import ChatUserList from './modules/chat/ChatUserList';

Vue.use(Vuex);

export default new Vuex.Store({
    modules:{
        WhereAmI,

        ProductList,

        AboutUs,

        Login,
        ForgotPassword,
        ReSendOtp,

        ProfileDetails,
        ProfileUpdate,

        ProfileList,
        UserList,

        FollowingList,
        FollowersList,

        ChatUserList,
    }

});