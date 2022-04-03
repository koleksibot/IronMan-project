<template>
    <div class="UnFollow_Container">
        <form @submit.prevent="FollowUnFollow" v-bind:key="id">
            <button v-if="!Following" class="Follow_Btn button_OutLine_Zero">Followme</button>
            <button v-else-if="Following" class="UnFollow_Btn button_OutLine_Zero">Un Follow</button><br>
        </form>

        <button v-if="Following" class="Message_Btn button_OutLine_Zero">Message</button><br>

    </div>
</template>


<script>
import Vue from 'vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
Vue.use(VueAxios, axios)
import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl;

export default {
    name: 'FollowUnfollowButton',
    props:{
        id:Number,
        is_following:Boolean,
    },
    data(){
        return{
            Following: this.is_following
        }
    },
    methods:{
         /* ====:~~~:====[ TERGET SIGNUP BACKEND ]====:~~~:==== */
        FollowUnFollow(){
            let id = this.id
            let token = localStorage.getItem('token')

            this.axios.get(Link+`/AllProfile/follow_unfollow/${id}/`, {headers: {Authorization: `Token ${token}`}})
            .then(resp => {
                if (resp.status === 200){
                    // console.warn(resp.data)
                    if (resp.data == false){
                        this.Following = false
                    }
                    else if(resp.data == true){
                        this.Following = true
                    }
                }
            })
            .catch(err =>{
                this.LoginError = true
                console.warn(err)
            })
        }
    }
}
</script>

<style scoped>

.UnFollow_Container{
    height: 100%;
    width: 100%;
    display: inline-flex;
    overflow: hidden;
    align-items: center;
    justify-content: center;
}
.Follow_Btn{
    background: rgba(172, 255, 47, 0.782);
    border: none;
    box-shadow: 0px 0px 2px rgb(1, 95, 12);
    padding: 5px;
    color: green;
}

.UnFollow_Btn{
    background: rgb(255, 177, 177);
    border: none;
    box-shadow: 0px 0px 2px rgb(255, 0, 0);
    padding: 5px;
    color: rgb(255, 0, 0);
}
.Message_Btn{
    background: rgba(155, 168, 245, 0.782);
    border: none;
    box-shadow: 0px 0px 2px rgb(12, 17, 167);
    padding: 5px;
    color: rgb(12, 17, 167);
    margin-left: 5px;
}
</style>