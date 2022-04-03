<template>
    <div class="auth_FixedConatainer">
        <div class="SignUp_PageHOlder">
            
                
            <Loading v-if="IsLoading"/>
            <div  v-else  class="SignUp_Base_Container">

                <div class="Main_Containt_Holder">

                    <div class="Sign_Up_Header">
                        ataOta Change Your Password
                        <img src="@/assets/AccountIcons/Icon awesome-user-circle.svg">
                    </div>

                    <div class="SignUp_Form">
                        <form  @submit.prevent="ChangePasswordForm" method="post">
                            
                            <div class="InputHolder">
                                <input v-if="thisIspassword" type="password" name="password" placeholder="Enter New Password" v-model="send_EmVe_Otp.password" autocomplete="new-password"/>
                                <input v-else type="text" name="password" placeholder="Enter New Password" v-model="send_EmVe_Otp.password"/>

                                <span 
                                v-on:click="TogglePassword" 
                                class="Hide_Show_Icon">
                                    <img v-if="thisIspassword" src="@/assets/AccountIcons/Icon ionic-md-eye-off.svg">
                                    <img v-else src="@/assets/AccountIcons/Icon ionic-md-eye.svg">
                                </span>

                                <div v-if="password_errors" class="ErrorText">Password is required and contains atlist 1-Capital 1-smaller case, 1special character and 1-number with 8-60 character
                                </div>
                            </div>

                            <div class="InputHolder">
                                <input v-if="thisIspassword" type="password" name="password2" placeholder="Retype Password" v-model="send_EmVe_Otp.password2" autocomplete="new-password"/>

                                <input v-else type="text" name="password2" placeholder="Retype Password" v-model="send_EmVe_Otp.password2" />

                                <div v-if="password2_errors" class="ErrorText">Your Second Password don't match with password One</div>
                                <div v-if="invalidCr_errors" class="ErrorText">Someting Is invalid inyour credential, Try Again</div>
                            </div>
                            
                            <input type="text" class="OtpInput" name="OTP" maxlength="6" v-model="send_EmVe_Otp.OTP" placeholder="6-Digit OTP"/>
                            <div v-if="invalidOtp_errors" class="ErrorText">Otp is required</div>
                            <div v-on:click="newOtp" class="Re_Send_OTP">
                                Re Send OTP
                            </div>

                            <SubmitButton buttonText="Send" />
                        </form>
                    </div>




                    <div class="SignUp_Footer">
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
import SubmitButton from './SubmitButton.vue'
import Loading from '@/Components/BasicComponents/Loading.vue'
import NormalCancelButton from './NormalCancelButton.vue'

export default {
    name: 'PasswordChangeForm',
    components:{
        SubmitButton,
        Loading,
        NormalCancelButton
    },
    data(){
        return{
            IsLoading: false,
            thisIspassword:true,
            password_errors: false,
            password2_errors: false,
            invalidCr_errors: false,
            invalidOtp_errors: false,
            send_EmVe_Otp:{
                password: '',
                password2: '',
                OTP:'',
            }
        }
    },
    methods:{
        /* ====:~~~:====[ PASSWORD SHOW AND HIDE FUNCTION ]====:~~~:==== */
        TogglePassword(){
            this.thisIspassword =! this.thisIspassword
        },
        /* ====:~~~:====[ TERGET OTP BACKEND ]====:~~~:==== */
        ChangePasswordForm(){
            
            if (this.send_EmVe_Otp.password == ''){
                this.password_errors = true
            }
            else if (this.send_EmVe_Otp.password != this.send_EmVe_Otp.password2){
                this.password2_errors = true
            }
            else if (this.send_EmVe_Otp.OTP == ''){
                this.invalidOtp_errors = true
            }
            else{
                this.$store.dispatch('ChangePasswordFormSubmit', {
                    password: this.send_EmVe_Otp.password,
                    password2: this.send_EmVe_Otp.password2,
                    otp: this.send_EmVe_Otp.OTP
                })
                .then(success => {
                    if (success != null){
                        this.IsLoading = false
                        this.$router.push({name: 'LogIn'})
                        localStorage.removeItem('UsId')
                    }
                })
                .catch(err =>{
                    this.IsLoading = false
                    console.warn(err)
                })
            }
        },
        newOtp(){
            this.IsLoading = true
            this.$store.dispatch('ReSentOtp')
            .then(success => {
                if (success != null){
                    this.IsLoading = false
                }
            })
            .catch(err =>{
                this.IsLoading = false
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
    min-height: 250px;
    width: 100%;
    background-color: transparent;
    display: flex;
    justify-content: center;
}
.SignUp_Form form{
    width: 300px;
}
.InputHolder{
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