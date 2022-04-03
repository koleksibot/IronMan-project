<template>
    <ul>
        <li class="item" id="#1">
            <a href="##1" class="Navbtn">
                <img src="@/assets/BaseIcons/ProductUploadGreen.svg">Upload Things
            </a>
            <div class="sMenu">
                <a href="#" >Upload Products</a>
                <a href="#">Upload Contents</a>
            </div>
        </li>
        
        <li class="item" id="#2">
          <a href="##2" class="Navbtn">
              <img src="@/assets/BaseIcons/EditThings.svg">Edit Things
          </a>
          <div class="sMenu">
              <a href="#">Edit Profile</a>
              <a href="#">Edit Products</a>
              <a href="#">Edit Post</a>
              <a href="#">Edit Location</a>
          </div>
        </li>
        
        <li class="item" id="#3">
          <a href="##3" class="Navbtn">
              <img src="@/assets/BaseIcons/SpecialAccount.svg">Create Special Account
          </a>
          <div class="sMenu">
              <a href="#">Seller Account</a>
              <a href="#">Service Provider Accont </a>
          </div>
        </li>

        <li class="item" id="#4">
          <a href="##4" class="Navbtn">
              <img src="@/assets/BaseIcons/CreateThings.svg">Create Things
          </a>
          <div class="sMenu">
              <a href="#">Create Post</a>
              <a href="#">Create Content</a>
          </div>
        </li>


        <li class="item" id="#5">
          <a href="##5" class="Navbtn">
              <img src="@/assets/BaseIcons/SettingsThings.svg">Settings
          </a>
          <div class="sMenu">
              <router-link :to="{ name: 'ForgotPassword'}">
                  Forgot Password
              </router-link>
              <router-link :to="{ name: 'PasswordChangeForm'}">
                  <span  v-on:click="ChangePassword_Request">
                    Change Password
                  </span>
              </router-link>
              <a href="#">Account</a>
              <a href="#">Location</a>
          </div>
        </li>
        
        <li class="item" id="#6">
          <a href="##6" class="Navbtn">
              <img src="@/assets/BaseIcons/DeleteThings.svg">Delete Things
          </a>
          <div class="sMenu">
              <a href="#">Delete Post</a>
              <a href="#">Delete Products</a>
              <a href="#">Delete Account</a>
          </div>
        </li>
        
        <li v-if="authStatus" v-on:click="userLogout" class="item">
          <a href="##" class="Navbtn">
              <img src="@/assets/BaseIcons/LogOutGreen.svg">Logout
          </a>
        </li>

      </ul>
</template>


<script>
import { mapGetters } from 'vuex'

export default {
    name: 'HomeAsideMenu',
    computed: mapGetters(['authStatus'] || false),
    methods:{
        ChangePassword_Request(){
            this.$store.dispatch('ChangePassword_Request')
            .then((success) => {
                if (success.status === 200){
                    console.warn('Success')
                }
            })
        },
        userLogout(){
            this.$store.dispatch('LogOut')
            .then(() =>{
                this.$router.push({name: 'LogIn'})
            })
        }

    }
}
</script>


<style scoped>

/* Creating Animation Scroll purpose */
.HoverLeft{
    margin-left: 0px;
    transition: 1s;
}
.HoverRight{
    margin-left: 100%;
    transition: 1s;
}


/* Inner content of The Nave Bar */
#A_Nave_Shower ul{
    width: 100%;
    height: 100%;
    list-style-type: none;
    position: fixed;
    background: rgba(255, 255, 255, 0.98);
    box-shadow: 0px 0px 3px rgb(180, 177, 177);
    overflow: auto;
}
.item{
    overflow: hidden;
}
.item:first-child{
    border-top: none;
}
.Navbtn{
    display: block;
    padding: 10px;
    background: transparent;
    text-align: left;
    color: #159AC4;
    font-size: 14px;
    font-weight: bold;
    position: relative;
    text-decoration: none;
}
.Navbtn:before{
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    background: rgba(255, 255, 255, 0.98);
    left: 10px;
    bottom: -7px;
    transform: rotate(45deg);
    z-index: 1;
}
.Navbtn img{
    height: 24px;
    width: 24px;
    margin-right: 5px;
    margin-left: -5px;
}

.sMenu{
    background:  #04928b;
    font-weight: bold;
    overflow: hidden;
    transition: max-height 0.5s;
    max-height: 0;
}
.sMenu a{
    display: block;
    padding: 15px 20px;
    font-size: 12px;
    text-align: left;
    color: white;
    position: relative;
    text-decoration: none;
}
.sMenu a:hover{
    background: #0cfff3;
    color: black;
    text-decoration: none;
}
.sMenu a:before{
    content: "";
    position: absolute;
    width: 6px;
    height: 100%;
    background: #04928b;
    left: 0;
    top: 0;
    transition: 0.3s;
    opacity: 0;
}
.sMenu a:hover:before{
    opacity: 1;
}
.item:target .sMenu{
    max-height: 600px;
}

</style>