<template>
    <nav id="HomeNave">
        

        <!-- <router-link to="/SignUp"> -->
        <router-link v-if="!authStatus" :to="{ name: 'SignUp' }">
            <button>
                <!-- v-if="!" -->
                <span>
                    <img src="@/assets/BaseIcons/SignUpGreen.svg">
                </span>
                SignUp
            </button>
        </router-link>
        
        <router-link v-if="!authStatus" :to="{ name: 'LogIn' }">
            <button>
                <span>
                    <img src="@/assets/BaseIcons/LogInGreen.svg">
                </span>
                LogIn
            </button>
        </router-link>

        <button>
            <span>
                <img src="@/assets/BaseIcons/AllProducts.svg">
            </span>
            All Products
        </button>

        <router-link :to="{ name: 'AllUsersList' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/All_users.svg">
            </span>
            All Users
        </button>
        </router-link>

        <router-link :to="{ name: 'AboutUs' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/AboutUsGreen.svg">
            </span>
            About Us
        </button>
        </router-link>

        <button>
            <span>
                <img src="@/assets/BaseIcons/AllServices.svg">
            </span>
            All Services
        </button>

        <button>
            <span>
                <img src="@/assets/BaseIcons/TendingGreen.svg">
            </span>
            Trending
        </button>

    </nav>
</template>


<script>
let prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
let HomeNave = document.getElementById("HomeNave");
if (prevScrollpos > currentScrollPos) {
    if (HomeNave != null){
        HomeNave.style.top = "0";
    }
} else {
    document.getElementById("HomeNave").style.top = "-40px";
}
prevScrollpos = currentScrollPos;
}

import { mapGetters } from 'vuex'

export default {
    name: 'HomeNav',
    computed: mapGetters(['authStatus']) || false,
    methods:{
    },

}
</script>



<style scoped>
nav{
    width: 100%;
    height: 40px;
    margin-top: 40px;
    position: fixed;
    background: #ffffff;
    box-shadow: 0px 1px 3px #27c997;
    transition: 0.3s;
    white-space: nowrap;
    overflow: auto;
    z-index: 700;
}


nav button{
    height: 38px;
    background: transparent;
    border: none;
    border-radius: 35px;
    padding: 0px 10px;
    font-weight: bold;
    color: #04928b;
}
nav button:hover{
    background: #d2f7ff;
    border: 1px solid #27c997;
    box-sizing: border-box;
}
nav button:focus{
    outline: 0;
}
nav button img{
    height: 24px;
    width: 24px;
}
.yesAuthenticated{
    display: none;
}

@media only screen and (max-width:480px){
    nav button{
        margin-top: 3px;
        height: 35px;
        background: transparent;
        border: none;
        border-radius: 35px;
        padding: 0px 10px;
        font-weight: bold;
        color: #04928b;
    }
}
@media only screen and (min-width:480px){
    nav{
        height: 45px;
    }
}
@media only screen and (min-width:600px){
    nav{
        width: 75%;
    }
}
@media only screen and (min-width:750px){
    nav{
        width: 80%;
    }
}
@media only screen and (min-width:1000px){
    nav{
        width: 84%;
    }
}
@media only screen and (min-width:1200px){
    nav{
        width: 86%;
    }
}
</style>