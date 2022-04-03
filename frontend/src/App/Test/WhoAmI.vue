<template>

    <div>
        <button v-on:click="TokenManuPulation">Click to Knwo Who Am I</button>
        <div>See Your console or Warning</div>
    </div>
</template>

<script>
import Vue from 'vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
Vue.use(VueAxios, axios)

import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl


export default {
    name: 'WhoAmI',
    data(){
        return{
            tokens: localStorage.getItem('access_token') || null,
        }
    },
    computed:{
        // isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },
    methods:{
        TokenManuPulation(){
            let token = localStorage.getItem('token')
            this.axios.get(Link+'/Account/whoAmI/', {headers: { Authorization: `Token ${token}`}})
            .then(response =>{
                console.warn(response.data.message)
            })
            .catch(error => {
                    console.warn(error)
                }
            )
        },
    }
}
</script>