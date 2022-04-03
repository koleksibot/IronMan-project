<template>

    <div class="auth_FixedConatainer">
        <div class="SignUp_PageHOlder">
            <div class="SignUp_Base_Container">

                <div class="Main_Containt_Holder">

                    <div class="Sign_Up_Header">
                        ataOta Log In
                        <img src="@/assets/AccountIcons/Icon awesome-user-circle.svg">
                    </div>

                    <div class="SignUp_Form">
                        <form  @submit.prevent="UserLogin" method="post">
                            <div class="InputHolder">
                                <input type="text" name="username" placeholder="User Name" autocomplete="username" v-model="login.username" />
                                <div v-if="username_errors" class="ErrorText">UserName Is required and atlist contains 8 character</div>
                            </div>
                            <div class="InputHolder">
                                <input v-if="thisIspassword" type="password" name="password" placeholder="Password"  autocomplete="new-password" v-model="login.password" />

                                <input v-else type="text" name="password" v-model="login.password" placeholder="Password" />
                                <span v-on:click="TogglePassword" class="Hide_Show_Icon">
                                    <img v-if="thisIspassword" src="@/assets/AccountIcons/Icon ionic-md-eye-off.svg">
                                    <img v-else src="@/assets/AccountIcons/Icon ionic-md-eye.svg">
                                </span>
                                <div v-if="password_errors" class="ErrorText">UserName Is required and atlist contains 8 character</div>
                                <div v-if="LoginError" class="ErrorText">Password or Username Might be Incorrect!, Try Again</div>
                            </div>
                            <SubmitButton buttonText="Log In" />
                        </form>
                    </div>




                    <div class="SignUp_Footer">
                        I Don't Have An Account Go To... 
                        <router-link to="/SignUp" class="AllLinksStyle">
                            <NormalFormsButton buttonText="SignUp"/>
                        </router-link>
                        
                        <router-link :to="{name: 'ForgotPassword'}" class="AllLinksStyle">
                            <NormalFormsButton buttonText="Foget Password"/>
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
import SubmitButton from './SubmitButton.vue'
import NormalFormsButton from './NormalFormsButton.vue'
import NormalCancelButton from './NormalCancelButton.vue'

// import Vue from 'vue'
// import axios from 'axios'
// Vue.use(axios)

export default {
    name: 'LogIn',
    components:{
        SubmitButton,
        NormalFormsButton,
        NormalCancelButton
    },
    data(){
        return{
            thisIspassword:true,
            username_errors: false,
            password_errors: false,
            LoginError: false,
            isLoggedIN: false,
            login:{
                username: '',
                password: '',
                is_admin : null

            }
        }
    },
    methods:{
        /* ====:~~~:====[ PASSWORD SHOW AND HIDE FUNCTION ]====:~~~:==== */
        TogglePassword(){
            this.thisIspassword =! this.thisIspassword
        },

         /* ====:~~~:====[ TERGET SIGNUP BACKEND ]====:~~~:==== */
        UserLogin(){
            if(!this.login.username){
                this.username_errors = true

            }
            if (!this.login.password){
                this.password_errors = true
            }
            this.$store.dispatch('Login', {
                username: this.login.username, 
                password: this.login.password
            })
            .then(success => {
                if (success.status === 200){
                    this.$router.push({'name': 'Home'})
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
.SignUp_Base_Container{
    min-width: 350px;
    max-width: 420px;
    height: 600px;
    background-color: #fff;
    box-shadow: 0px 0px 5px #888;
    position: relative;
    overflow: hidden;
    /* border-radius: 20px; */

}
.SignUp_Base_Container::before{
    content: " ";
    height: 500px;
    width: 350px;
    background: linear-gradient(0deg, rgba(27,0,217,0.83) 0%, rgba(136,6,106,0.76) 35%, rgba(211,43,223,0.75) 100%);
    position: absolute;
    transform: translateX(-50%);
    border-bottom-left-radius: 50%;
    border-bottom-right-radius: 50%;
    z-index: 2;
}

.SignUp_Base_Container::after{
    content: " ";
    height: 600px;
    width: 350px;
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
    height: 200px;
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

</style>