<template>
    <nav id="HomeNave">

        <router-link :to="{ name: 'MessageUserList' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/ChatGreen.svg">
            </span>
            Chat
        </button>
        </router-link>
        
        <router-link :to="{ name: 'AllUsersList' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/All_users.svg">
            </span>
            All Users
        </button>
        </router-link>

        <router-link :to="{ name: 'AllFollowersList' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/Followers.svg">
            </span>
            Followers
        </button>
        </router-link>

        <router-link :to="{ name: 'AllFollowingList' }">
        <button>
            <span>
                <img src="@/assets/BaseIcons/Following.svg">
            </span>
            Following
        </button>
        </router-link>

    </nav>
</template>


<script>


export default {
    name: 'UserListNav',
    methods:{
        //  v-on:click="Display_Chat_Container_Hide_UserList_Container"
        // Display_Chat_Container_Hide_UserList_Container(){
        //     let Hide_UserList = document.getElementById('UserListBase_Conatainer')
        //     let Display_Chat = document.getElementById('ChatHolder_Container')
        //     Hide_UserList.classList.add('Hid_UserListBase_Conatainer')
        //     Display_Chat.classList.remove('Hid_ChatHolder_Container')
        // }
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
.yesAuthenticated{
    display: none;
}



</style>