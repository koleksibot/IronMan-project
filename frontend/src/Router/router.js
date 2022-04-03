import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store';


import HomeBase from '@/App/A1Home/a1HomeBase.vue'
// import SerchBase from '@/App/A6Search/a6SerchBase.vue'
import SignUp from '@/App/Account/SignUp.vue'
import LogIn from '@/App/Account/LogIn.vue'
import ForgotPassword from '@/App/Account/ForgotPassword.vue'
import PasswordChangeForm from '@/App/Account/Pass_ChangeForm.vue'

import ProfileBase from '@/App/A2Profile/a2ProfileBase.vue'
import NormalProfile from '@/App/A2Profile/NormalProfile/NormalProfile.vue'
import OthersProfile from '@/App/A2Profile/OthersProfile/OthersProfile.vue'

import ChatBase from '@/App/A3Chat/a3ChatBase.vue'
import AllUsersList from '@/Components/F7UserListRelated/AllUsersLIst.vue'
import AllFollowersList from '@/Components/F7UserListRelated/AllFollowersList.vue'
import AllFollowingList from '@/Components/F7UserListRelated/AllFollowingList.vue'
import MessageUserList from '@/Components/F7UserListRelated/MessageUserList.vue'


import MapBase from '@/App/A4Map/a4MapBase.vue'

import CartBase from '@/App/A5Cart/a4CartBase.vue'

import AboutUs from '@/App/AboutUs/AboutUs.vue'


Vue.use(VueRouter);


let router = new VueRouter({
    mode: 'history',
    routes: [
        // {
        //     path: '/SerchBase',
        //     component: SerchBase,
        //     name: 'SerchBase',
        // },
        {
            path: '/',
            component: HomeBase,
            name: 'Home',
            children: [
                {
                    path: '/SignUp',
                    component: SignUp,
                    name: 'SignUp',
                    beforeEnter(to, from, next){
                        if (store.getters.authStatus == 'success'){
                            return next({name: 'Home'})
                        }
                        next()
                    }
                },
                {
                    path: '/LogIn',
                    component: LogIn,
                    name: 'LogIn',
                    beforeEnter(to, from, next){
                        if (store.getters.authStatus == 'success'){
                            return next({name: 'Home'})
                        }
                        next()
                    }
                },
                {
                    path: '/ForgotPassword',
                    component: ForgotPassword,
                    name: 'ForgotPassword',
                },
                {
                    path: '/PasswordChangeForm',
                    component: PasswordChangeForm,
                    name: 'PasswordChangeForm',
                    beforeEnter(to, from, next){
                        if (!(store.getters.authStatus == 'success')){
                            return next({name: 'LogIn'})
                        }
                        next()
                    },
                },
            ]
        },
        {
            path: '/ProfileBase',
            component: ProfileBase,
            name: 'ProfileBase',
            beforeEnter(to, from, next){
                if (!(store.getters.authStatus == 'success')){
                    return next({name: 'LogIn'})
                }
                next()
            },
            children:[
                {
                    path: 'NormalProfile',
                    component: NormalProfile,
                    name: 'NormalProfile',
                },
                {
                    path: 'OthersProfile/:id',
                    component: OthersProfile,
                    name: 'OthersProfile',
                },
            ]
        },
        {
            path: '/ChatBase',
            component: ChatBase,
            name: 'ChatBase',
            beforeEnter(to, from, next){
                if (!(store.getters.authStatus == 'success')){
                    return next({name: 'LogIn'})
                }
                next()
            },
            children:[
                {
                    path: 'AllUsersList',
                    component: AllUsersList,
                    name: 'AllUsersList'
                },
                {
                    path: 'AllFollowersList',
                    component: AllFollowersList,
                    name: 'AllFollowersList'
                },
                {
                    path: 'AllFollowingList',
                    component: AllFollowingList,
                    name: 'AllFollowingList'
                },
                {
                    path: 'MessageUserList',
                    component: MessageUserList,
                    name: 'MessageUserList'
                }
            ]
        },
        {
            path: '/MapBase',
            component: MapBase,
            name: 'MapBase'
        },
        {
            path: '/CartBase',
            component: CartBase,
            name: 'CartBase'
        },
        {
            path: '/AboutUs',
            component: AboutUs,
            name: 'AboutUs'
        },
    ]
})

export default router;