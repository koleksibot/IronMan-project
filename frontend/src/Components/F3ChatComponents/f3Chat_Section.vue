<template>
    <section>

        <div class="UserListBase_Conatainer Chat_Section_HolderStyle"  id="UserListBase_Conatainer">
            <div class="UserList_Conatainer">
                <AllUsersBase/>
            </div>
        </div>

        <div class="ChatHolder_Container Chat_Section_HolderStyle Hid_ChatHolder_Container" id="ChatHolder_Container">
            <div class="Chat_Conatainer">
                <ChatBoxContainer/>
            </div>
        </div>

    </section>
</template>


<script>
import AllUsersBase from '@/Components/F7UserListRelated/AllUserBase.vue'
import ChatBoxContainer from '@/Components/F3ChatComponents/ChatBoxComponents/ChatBoxContainer.vue'

export default {
    name: 'ChatSection',
    components:{
        AllUsersBase,
        ChatBoxContainer,
    }
}
</script>


<style scoped>
section{
    position: relative;
    height: 100vh;
    position: fixed;
    background: transparent;
    padding-top: 40px;
    padding-bottom: 40px;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 100vh;
}
.Chat_Section_HolderStyle{
    box-sizing: border-box;
    max-height: 100vh;
    padding-bottom: 40px;

}
.UserListBase_Conatainer{
    height: 100vh;
    width: 100%;
}

.UserList_Conatainer{
    height: 100%;
    overflow: auto;
}

.ChatHolder_Container{
    width: 100%;
    height: 100vh;
}
.Chat_Conatainer{
    height: 100%;
    overflow: auto;
}


@media only screen and (max-width:750px){
    .Hid_UserListBase_Conatainer{
        display: none;
    }
    .Hid_ChatHolder_Container{
        display: none;
    }
}

@media only screen and (max-width:600px){
    section{
        width: 100%;
    }
}

@media only screen and (min-width:600px){
    section{
        width: 75%;
    }
}
@media only screen and (min-width:750px){
    section{
        width: 80%;
        position: relative;
        height: 100vh;
        position: fixed;
        background: transparent;
        padding-top: 45px;
        padding-bottom: 45px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 100vh;
    }
    .Chat_Section_HolderStyle{
        box-sizing: border-box;
        padding: 0px 5px;
        max-height: 100vh;
        padding-bottom: 90px;

    }
    .UserListBase_Conatainer{
        height: 100vh;

    }
    .UserList_Conatainer{
        height: 100%;
        width: 100%;
        box-shadow: 0px 0px 3px rgb(105, 106, 105);
        overflow: auto;
    }
    .ChatHolder_Container{
        width: auto;
    }
    .Chat_Conatainer{
        height: 100%;
        width: 100%;
        box-shadow: 0px 0px 3px rgb(105, 106, 105);
        overflow: auto;
    }
}
@media only screen and (min-width:1000px){
    section{
        width: 84%;
    }
}
@media only screen and (min-width:1200px){
    section{
        width: 86%;
    }
}
</style>