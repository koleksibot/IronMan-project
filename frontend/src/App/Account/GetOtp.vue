<template>
    <div class="auth_FixedConatainer">
        <div class="SignUp_PageHOlder">
        <Loading v-if="IsLoading"/>

        <div  v-else  class="SignUp_Base_Container">

                <div class="Main_Containt_Holder">

                    <div class="Sign_Up_Header">
                        ENTER YOUR OTP
                        <img src="@/assets/AccountIcons/Icon awesome-user-circle.svg">
                    </div>

                    <div class="SignUp_Form">
                        <form  @submit.prevent="Submit_EmailValidate_Otp" method="post">
                            <span>Check your Email and Enter OTP, to active your account</span><br><br>
                            
                            <input type="text" class="OtpInput" name="OTP" maxlength="6" v-model="send_EmVe_Otp.OTP" placeholder="6-Digit OTP"/>
                            <div v-if="invalidOtp_errors" class="ErrorText">Otp is required</div>
                            <div v-on:click="newOtp" class="Re_Send_OTP">
                                Re Send OTP
                            </div>

                            <SubmitButton buttonText="Send" />
                        </form>
                    </div>


                    <div class="SignUp_Footer">
                        <span style="color:#09bf09;">The given email is not mine, Give me SignIn Again!</span>
                        <NormalCancelButton style="color:red;" ButtonText="Re-Try "/>
                        <span style="color:#de0a10;">we don't recommend Re-try, until you give wrong email!</span>
                        <router-link to="/" class="AllLinksStyle">
                            <NormalCancelButton ButtonText="Cancel"/>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import Vue from 'vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
Vue.use(VueAxios, axios)


import SubmitButton from './SubmitButton.vue'
import Loading from '@/Components/BasicComponents/Loading.vue'
import NormalCancelButton from './NormalCancelButton.vue'

import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl


export default {
    name: 'EnterOTP',
    components:{
        SubmitButton,
        Loading,
        NormalCancelButton
    },
    data(){
        return{
            IsLoading: false,
            invalidOtp_errors: false,
            send_EmVe_Otp:{
                OTP:'',
            }
        }
    },
    methods:{
        /* ====:~~~:====[ TERGET OTP BACKEND ]====:~~~:==== */
        Submit_EmailValidate_Otp(e){
            this.IsLoading = true
            let UsId = localStorage.getItem('UsId')
            this.axios.post(Link+'/Account/user_email_validate/'+UsId+'/', {
                otp: this.send_EmVe_Otp.OTP,
            })
            
            /* ====:~~~:====[ RESPONSE COME FROM OTP BACKEND ]====:~~~:==== */
            .then(
                resp => {
                    this.IsLoading = false

                    // console.warn(resp)
                    // console.warn(resp.data[0])
                    if(resp.request.status==200 & resp.data[0]=='true'){
                        this.IsOtp = true
                        localStorage.removeItem('UsId')
                        localStorage.removeItem('otpPage')
                        this.$router.push({name: 'LogIn'})
                    }
                    else if (resp.request.status==200 & resp.data[0]=='false'){
                        alert('invalid OTP')
                    }
                })

            /* ====:~~~:====[ CATCHING ERROR COME FROM BACKEND ]====:~~~:==== */
            .catch(err => console.warn(err))
            e.preventDefault();
        },

        
        /* ====:~~~:====[ TERGET OTP BACKEND ]====:~~~:==== */
        newOtp(){
            this.IsLoading = true
            this.$store.dispatch('ReSentOtp')
            /* ====:~~~:====[ RESPONSE COME FROM OTP BACKEND ]====:~~~:==== */
            .then(success => {
                if (success != null){
                    this.IsLoading = false
                }
            })
            /* ====:~~~:====[ CATCHING ERROR COME FROM BACKEND ]====:~~~:==== */
            .catch(err =>{
                this.IsLoading = false
                this.invalidOtp_errors = true
                console.warn(err)
            })
        }
    }
}
</script>


<style scoped>
.SignUp_Base_Container{
    min-width: 350px;
    max-width: 420px;
    height: 450px;
    background-color: #fff;
    box-shadow: 0px 0px 5px #888;
    position: relative;
    overflow: hidden;
    /* border-radius: 20px; */

}
.SignUp_Base_Container::before{
    content: " ";
    height: 350px;
    width: 350px;
    background: linear-gradient(0deg, rgba(27,0,217,0.83) 0%, rgba(136,6,106,0.76) 35%, rgba(211,43,223,0.75) 100%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 60%;
    border-bottom-right-radius: 0%;
    z-index: 2;
}

.SignUp_Base_Container::after{
    content: " ";
    height: 450px;
    width: 350px;
    background: linear-gradient(0deg, rgba(78,9,146,0.98) 0%, rgba(210,153,238,0.72) 32%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 70%;
    border-bottom-right-radius: 0%;
    z-index: 1;
}


.Main_Containt_Holder{
    height: 100%;
    width: 100%;
    position: absolute;
    background-color: transparent;
    z-index: 10;
    color: #fff;
}
.Sign_Up_Header{
    height: 70px;
    padding-top: 20px;
    width: 100%;
    background-color: transparent;
    display: flex;
    text-align: center;
    flex-direction: column;
    justify-content: center;
    font-weight: bold;
    font-variant: small-caps;
    text-shadow: 0px 1px 3px #888;
}


.SignUp_Form{
    min-height: 200px;
    width: 100%;
    background-color: transparent;
    display: flex;
    justify-content: center;
}
.SignUp_Form form{
    width: 300px;
}

.ErrorText{
    color: orange;
    font-size: 12px;
}
.OtpInput{
    width: 80%;
    height: 30px;
    text-align: center;
}
.Re_Send_OTP{
    margin-top: 10px;
    color: cyan;
    cursor: pointer;
}
</style>