<template>
    <div class="auth_FixedConatainer">
        <div class="SignUp_PageHOlder">
                
            <GetOtp v-if="IsOtp"/>
            <Loading v-else-if="IsLoading"/>
            <div v-else class="SignUp_Base_Container">

                <div class="Main_Containt_Holder">
                    <div class="Sign_Up_Header">
                        ataOta Sign Up
                        <img src="@/assets/AccountIcons/Icon awesome-user-circle.svg">
                    </div>

                    <div class="SignUp_Form">
                        <form @submit.prevent="SubmitData" method="post">
                            <div class="InputHolder">
                                <input type="text" name="full_name" placeholder="Full Name" v-model="signup.full_name" />
                                <div v-if="fullname_errors" class="ErrorText">Full Name Is required and atlist contains 6 character</div>
                            </div>
                            <div class="InputHolder">
                                <input type="text" name="username" placeholder="User Name" v-model="signup.username"/>
                                <div v-if="username_errors" class="ErrorText">UserName Is required and atlist contains 8 character</div>
                            </div>
                            <div class="InputHolder">
                                <input type="email" name="email" placeholder="Email Id" v-model="signup.email"/>
                                <div v-if="email_errors" class="ErrorText">Email is required and Must be A valid email</div>
                            </div>
                            <!-- Phone  -->
                            <div class="InputHolder" style="display:none">
                                <input type="text" name="phone" maxlength="10" id="id_phone" placeholder="phone no." v-model="signup.phone" autocomplete="phone"/>
                                <!-- <div v-if="phone_errors" class="ErrorText">Full Name Is required and atlist contains 6 character</div> -->
                            </div>
                            <div class="InputHolder">
                                <input v-if="thisIspassword" type="password" name="password" placeholder="Password" v-model="signup.password"  autocomplete="new-password"/>
                                <input v-else type="text" name="password" placeholder="Password" v-model="signup.password"/>
                                <span v-on:click="TogglePassword" class="Hide_Show_Icon">
                                    <img v-if="thisIspassword" src="@/assets/AccountIcons/Icon ionic-md-eye-off.svg">
                                    <img v-else src="@/assets/AccountIcons/Icon ionic-md-eye.svg">
                                </span>
                                <div v-if="password_errors" class="ErrorText">Password is required and contains atlist 1-Capital 1-smaller case, 1special character and number with 8character</div>
                            </div>
                            <div class="InputHolder">
                                <input v-if="thisIspassword" type="password" name="password2" placeholder="Retype Password" v-model="signup.password2" autocomplete="new-password"/>
                                <input v-else type="text" name="password2" placeholder="Retype Password" v-model="signup.password2" />
                                <div v-if="password2_errors" class="ErrorText">Your Second Password don't match with password One</div>
                                <div v-if="invalidCr_errors" class="ErrorText">Someting Is invalid inyour credential, Try Again</div>
                            </div>
                            <SubmitButton buttonText="Sign Up"/>
                        </form>
                    </div>

                    <div class="SignUp_With">
                        Sign Up With
                        <div class="G_and_F_Icon">
                            <a href="#">
                                <img src="@/assets/AccountIcons/google.svg">
                            </a>
                            <a href="#">
                                <img src="@/assets/AccountIcons/facebook.svg">
                            </a>
                        </div>
                    </div>

                    <div class="SignUp_Footer">
                        I Aleady Have An Account Go To... 
                        <router-link to="/LogIn" class="AllLinksStyle">
                            <NormalFormsButton buttonText="Log In"/>
                        </router-link>
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

import GetOtp from './GetOtp.vue'
import Loading from '@/Components/BasicComponents/Loading.vue'

import SubmitButton from './SubmitButton.vue'
import NormalFormsButton from './NormalFormsButton.vue'
import NormalCancelButton from './NormalCancelButton.vue'

import {BackEndUrl} from "@/constants.js";
let Link = BackEndUrl.BackendTergetUrl


export default {
    name: 'SignUp',
    components:{
        GetOtp,
        Loading,
        SubmitButton,
        NormalFormsButton,
        NormalCancelButton

    },
    data(){
        return{
            IsOtp: localStorage.getItem('otpPage') || false,
            IsLoading: false,
            thisIspassword:true,
            fullname_errors: false,
            username_errors: false,
            email_errors: false,
            password_errors: false,
            password2_errors: false,
            invalidCr_errors:false,
            signup:{
                full_name: '',
                username: '',
                email: '',
                phone: '',
                password: '',
                password2: '',

            }
        }
    },
    methods:{
        /* ====:~~~:====[ PASSWORD SHOW AND HIDE FUNCTION ]====:~~~:==== */
        TogglePassword(){
            this.thisIspassword =! this.thisIspassword
        },

        /* ====:~~~:====[ TERGET SIGNUP BACKEND ]====:~~~:==== */
        SubmitData(){
            console.warn(this.fullname_errors);
            if (this.signup.full_name == ''){
                this.fullname_errors= true
            }
            else if ((this.signup.username == '')){
                this.username_errors = true
            }
            
            else if (this.signup.email == ''){
                this.email_errors = true
            }
            else if (this.signup.password == ''){
                this.password_errors = true
            }
            else if (this.signup.password != this.signup.password2){
                this.password2_errors = true
            }
            else{
                this.IsLoading = true

                this.axios.post(Link+'/Account/user_signup/', {
                    full_name: this.signup.full_name,
                    username: this.signup.username,
                    email: this.signup.email,
                    phone: this.signup.phone,
                    password: this.signup.password,

                })
                
                /* ====:~~~:====[ RESPONSE COME FROM BACKEND ]====:~~~:==== */
                .then(
                    resp => {
                        // console.warn(resp)
                            this.IsLoading = false

                            if(resp.request.status==200 & resp.data.userId!=undefined){
                                this.IsOtp = true
                                localStorage.setItem('UsId', resp.data.userId)
                                localStorage.setItem('otpPage', true)
                                // let alertText = 'Hello'+this.signup.full_name+' you successfully signup please veryfy your email'
                                // alert('success')
                            }
                            else if(resp.request.status==200 & resp.data.userId==undefined){
                                // alert(resp.data)
                                console.log(resp.data)
                            }
                        }
                    )
                        
                /* ====:~~~:====[ CATCHING ERROR COME FROM BACKEND ]====:~~~:==== */
                .catch(error => {
                    this.invalidCr_errors = true
                    
                    this.fullname_errors= false
                    this.username_errors = false
                    this.email_errors = false
                    this.password_errors = false
                    this.password2_errors = false

                    this.IsLoading = false
                    console.warn(error)
                })
                
            }
        }
        
    }
}
</script>


<style>
.auth_FixedConatainer{
    height: 100vh;
    width: 100vw;
    position: fixed;
    z-index: 1500;
    background: #1c1a1a64;
}
.SignUp_PageHOlder{
    min-height: 100vh;
    width: 100vw;
    background-color: transparent;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: auto;

}

.Submit_ButtonHolder{
    margin-top: 40px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.AllLinksStyle{
    text-decoration: none;
}

.SignUp_Footer{
    min-height: 60px;
    height: auto;
    background-color: transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    text-shadow: 0px 0px 2px #000;
}
</style>

<style scoped>
.SignUp_Base_Container{
    min-width: 360px;
    max-width: 420px;
    height: 100vh;
    max-height: 650px;
    background-color: #fff;
    box-shadow: 0px 0px 5px #888;
    position: relative;
    overflow: hidden;
    /* border-radius: 20px; */

}
.SignUp_Base_Container::before{
    content: " ";
    height: 100vh;
    max-height: 550px;
    min-width: 360px;
    background: linear-gradient(0deg, rgba(27,0,217,0.83) 0%, rgba(136,6,106,0.76) 35%, rgba(211,43,223,0.75) 100%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 50%;
    border-bottom-right-radius: 50%;
    z-index: 2;
}

.SignUp_Base_Container::after{
    content: " ";
    height: 100vh;
    max-height: 650px;
    min-width: 360px;
    background: linear-gradient(0deg, rgba(78,9,146,0.98) 0%, rgba(210,153,238,0.72) 32%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 50%;
    border-bottom-right-radius: 50%;
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
    height: 300px;
    width: 100%;
    background-color: transparent;
    display: flex;
    justify-content: center;
}
.SignUp_Form form{
    width: 300px;
}
.InputHolder{
    height: auto;
    min-height: 40px;
    width: 100%;
}
.InputHolder input{
    background-color: transparent;
    width: 100%;
    border: none;
    border-bottom: 2px solid #fff;
    padding-bottom: 5px;
    font-weight: bold;
    color: #fff;
}
.InputHolder input::placeholder{
    color: #fff;
    font-weight: bold;
    font-size: 14px;
}
.InputHolder input:focus{
    outline: 0;
    border-bottom: 2px solid #fbff00;
    transition: 1s linear;
}

.Input_BottomBorder{
    min-height: 15px;
    height: auto;
    background: transparent;
    width: 100%;
    color: rgb(255, 68, 0);
    font-size: 12px;
}

.Hide_Show_Icon{
    height: 20px;
    width: 20px;
    float: right;
    transform: translateY(-25px);
    cursor: pointer;
}
.Hide_Show_Icon img{
    height: 100%;
    width: 100%;
}

.ErrorText{
    color: orange;
    font-size: 12px;
}


.SignUp_With{
    height: 60px;
    background-color: transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
}
.G_and_F_Icon{
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: center;
}
.G_and_F_Icon a{
    height: 35px;
    width: 35px;
    margin: 5px;
    background-color: transparent;
    border-radius: 50%;
    box-shadow: 0px 0px 2px #fff;
}
.G_and_F_Icon a img{
    height: 100%;
    width: 100%;
}

</style>