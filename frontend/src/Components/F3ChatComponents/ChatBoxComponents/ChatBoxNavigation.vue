<template>
    <nav>
        
        <router-link :to="{ name: 'AllUsersList' }">
        <button v-on:click="Hide_ChatBox_dispaly_UserList">
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
                <img src="@/assets/BaseIcons/AllProducts.svg">
            </span>
            All Products
        </button>

        <button>
            <span>
                <img src="@/assets/BaseIcons/AllServices.svg">
            </span>
            All Services
        </button>

    </nav>
</template>


<script>

export default {
    name: 'ChatBoxNav',
    methods:{
        Hide_ChatBox_dispaly_UserList(){
            let Hide_UserList = document.getElementById('UserListBase_Conatainer')
            let Display_Chat = document.getElementById('ChatHolder_Container')
            Hide_UserList.classList.remove('Hid_UserListBase_Conatainer')
            Display_Chat.classList.add('Hid_ChatHolder_Container')
        }
    },

}
</script>



<style scoped>
nav{
    height: 40px;
    width: 100%;
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

@media only screen and (max-width:480px){
    nav::-webkit-scrollbar{
        display: none;
    }
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

</style>