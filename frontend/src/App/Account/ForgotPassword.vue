<template>

    <div class="auth_FixedConatainer">
        <div class="SignUp_PageHOlder">
            <PasswordChangeForm v-if="IsOtp"/>
            <Loading v-else-if="IsLoading"/>
            <div v-else class="SignUp_Base_Container">

                <div class="Main_Containt_Holder">

                    <div class="Sign_Up_Header">
                        ataOta Forgot Password
                        <img src="@/assets/AccountIcons/Icon awesome-user-circle.svg">
                    </div>

                    <div class="SignUp_Form">
                        <form  @submit.prevent="ForgotPassword" method="post">
                            <div class="InputHolder">
                                <input type="text" name="username" placeholder="User Name" autocomplete="username" v-model="forgotPassword.username" />
                                <div v-if="username_errors" class="ErrorText">UserName Is required and atlist contains 8 character</div>
                            </div>
                            <div class="InputHolder">
                                <input type="email" name="email" placeholder="Enter Your Email" v-model="forgotPassword.email" />
                                <div v-if="email_errors" class="ErrorText">Give your email which was give by you during SignIn</div>
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
import NormalCancelButton from './NormalCancelButton.vue'

import PasswordChangeForm from './Pass_ChangeForm.vue'
import Loading from '@/Components/BasicComponents/Loading.vue'

export default {
    name: 'ForgotPassword',
    components:{
        PasswordChangeForm,
        Loading,
        SubmitButton,
        NormalCancelButton
    },
    data(){
        return{
            username_errors: false,
            email_errors: false,
            IsOtp: false,
            IsLoading: false,
            forgotPassword:{
                email: '',
            }
        }
    },
    methods:{

         /* ====:~~~:====[ TERGET Forgot Password BACKEND ]====:~~~:==== */
        ForgotPassword(){
            if (!this.forgotPassword.username){
                this.username_errors = true
            }
            else{
                this.IsLoading = true
                this.$store.dispatch('ForgotPassword', {
                    username: this.forgotPassword.username,
                    email: this.forgotPassword.email
                })
                .then(success => {
                    if (success != null){
                        this.IsOtp = true
                        this.IsLoading = false
                    }
                })
                .catch(err =>{
                    this.email_errors = true
                    this.IsLoading = false
                    console.warn(err)
                })
            }
            
        }
    }
    
}
</script>


<style scoped>
.SignUp_Base_Container{
    min-width: 350px;
    max-width: 420px;
    height: 400px;
    background-color: #fff;
    box-shadow: 0px 0px 5px #888;
    position: relative;
    overflow: hidden;
    /* border-radius: 20px; */

}
.SignUp_Base_Container::before{
    content: " ";
    height: 300px;
    width: 350px;
    background: linear-gradient(0deg, rgba(27,0,217,0.83) 0%, rgba(136,6,106,0.76) 35%, rgba(211,43,223,0.75) 100%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 70%;
    border-bottom-right-radius: 0%;
    z-index: 2;
}

.SignUp_Base_Container::after{
    content: " ";
    height: 400px;
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
    height: 150px;
    width: 100%;
    background-color: transparent;
    display: flex;
    justify-content: center;
}
.SignUp_Form form{
    width: 300px;
}
.InputHolder{
    height: 40px;
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

.ErrorText{
    color: orange;
    font-size: 12px;
}

</style>