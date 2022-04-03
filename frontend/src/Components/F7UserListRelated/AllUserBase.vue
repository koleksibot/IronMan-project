<template>
    <div class="UserList_Holder_Container">
        <div class="AllUserHeader">
            <UserListNavigation/>
        </div>
        <div class="UserList_Section">
            <router-view />
        </div>
    </div>
</template>


<script>
import UserListNavigation from './UserListNavigation.vue'
export default {
    name: 'AllUsersBase',
    components:{
        UserListNavigation,
    }
}
</script>

<style scoped>
.UserList_Holder_Container{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 40px 1fr 40px;
    height: 100%;
    width: 100%;
}
.AllUserHeader{
    height: 40px;
    width: 100%;
    background: green;
    overflow: hidden;
}
.UserList_Section{
    background: #e8e8e8;
    width: 100%;
    overflow: auto;
}
.UserList_Section::-webkit-scrollbar{
    background: transparent;
    width: 10px;
}
.UserList_Section::-webkit-scrollbar-button{
    width: 5px;
}
.UserList_Section::-webkit-scrollbar-thumb{
    color: green;
    height: 100px;
}
.UserList_Section::-webkit-scrollbar-track{
    background: transparent;
}
.UserList_Section::-webkit-scrollbar-thumb{
    max-width: 250px;
    background: #a4d178ce;
}
@media only screen and (min-width: 750px){
    .UserList_Holder_Container{
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 40px 1fr;
        height: 100%;
        width: 100%;
    }
}
</style>