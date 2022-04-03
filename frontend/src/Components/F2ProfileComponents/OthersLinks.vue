<template>
    <nav id="HomeNave Hide_Scroll_button">
        

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

        <button>
            <span>
                <img src="@/assets/BaseIcons/All_Post.svg">
            </span>
            All Post
        </button>

        <button>
            <span>
                <img src="@/assets/BaseIcons/createpost.svg">
            </span>
            Create Post
        </button>

    </nav>
</template>


<script>
export default {
    name: 'OtherLinks',
}
</script>



<style scoped>
nav{
    width: 100%;
    height: 40px;
    position: relative;
    background: #ffffff;
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
@media only screen and (min-width:480px){
    nav{
        height: 45px;
    }
}
</style>