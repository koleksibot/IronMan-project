<template>
    <footer>
        
        
        <router-link :to="{ name: 'MapBase' }">
            <button v-bind:class="[(deatilsWhereAmI == 'MapBase') ? 'yesActive':'notActive']">
                <img src="@/assets/BaseIcons/EarthGreen.svg">
                Map
            </button>
        </router-link>
        

        <router-link :to="{ name: 'NormalProfile'}">
            <button v-bind:class="[(deatilsWhereAmI == 'ProfileBase')? 'yesActive':'notActive']">
                <img src="@/assets/BaseIcons/ProfileGreen.svg">
                Profile
            </button>
        </router-link>
        
        <router-link :to="{ name: 'Home' }">
            <button v-bind:class="[(deatilsWhereAmI == 'Home') ? 'yesActive':'notActive']">
                <img src="@/assets/BaseIcons/HomeGreen.svg">
                Home
            </button>
        </router-link>
        

        
        <router-link :to="{ name: 'MessageUserList' }">
            <button  v-bind:class="[(deatilsWhereAmI == 'ChatBase') ? 'yesActive':'notActive']">
                <img src="@/assets/BaseIcons/ChatGreen.svg">
                Chat
            </button>
        </router-link>
        

        
        <router-link :to="{ name: 'CartBase' }">
            <button v-bind:class="[(deatilsWhereAmI == 'CartBase') ? 'yesActive':'notActive']">
                <img src="@/assets/BaseIcons/CartGreen.svg">
                Cart
            </button>
        </router-link>
        
    </footer>
</template>


<script>

export default {
    name: 'HomeFooter',
    computed:{
        deatilsWhereAmI(){
            return this.$store.state.WhereAmI.whereAmI
        }
    },
}
</script>



<style scoped>
footer{
    width: 100%;
    height: 40px;
    position: fixed;
    bottom: 0;
    background: #fff;
    box-shadow: 0px -1px 3px #27c997;
    transition: 0.3s;
    white-space: nowrap;
    overflow: auto;
    z-index: 800;
}
footer button{
    margin-top: 2px;
    height: 38px;
    background: transparent;
    border: none;
    border-radius: 35px;
    padding: 0px 5px;
    min-width: 20%;
    font-weight: bold;
    color: #04928b;
}

.yesActive{
    background: #d2f7ff;
    border: 1px solid #27c997;
    box-sizing: border-box;
}
footer button:focus{
    outline: 0;
}
footer button img{
    height: 24px;
    width: 24px;
}
@media only screen and (min-width:600px){
    footer{
        width: 75%;
    }
}
@media only screen and (min-width:750px){
    footer{
        width: 80%;
    }
}
@media only screen and (min-width:1000px){
    footer{
        width: 84%;
    }
    footer button{
        min-width: 10%;
    }
}
@media only screen and (min-width:1200px){
    footer{
        width: 86%;
    }
}
</style>