<template>
    <div class="Chat_BoxHolder_Container">
        <div class="ChatBox_Header">
            <ChatBoxComponents/>
        </div>
        <div class="ChatBox_Message_Container Scroll_Button_Container">
            <RandomText/>
        </div>
        <div class="ChatMSG_Container_Footer">
            Footer
        </div>
    </div>
</template>


<script>
import ChatBoxComponents from './ChatBoxNavigation.vue'
import RandomText from '@/App/Test/RandomText.vue'

export default {
    name: 'AllUsersBase',
    components:{
        ChatBoxComponents,
        RandomText,
    }
}
</script>

<style scoped>
.Chat_BoxHolder_Container{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 45px 1fr 45px;
    height: 100%;
    width: 100%;
}
.ChatBox_Header{
    height: 40px;
    background: transparent;
    overflow: hidden;
}
.ChatBox_Message_Container{
    background: #e8e8e8;
    width: 100%;
    overflow: auto;
}
.ChatMSG_Container_Footer{
    background: #fff;
    box-shadow: 0px -1px 2px #27c997;
    height: 40px;
    width: 100%;
}
/* @media only screen and (min-width: 600px){
    .ChatBox_Message_Container::-webkit-scrollbar{
        background: transparent;
        width: 10px;
    }
    .ChatBox_Message_Container::-webkit-scrollbar-button{
        width: 5px;
    }
    .ChatBox_Message_Container::-webkit-scrollbar-thumb{
        color: green;
        height: 100px;
    }
    .ChatBox_Message_Container::-webkit-scrollbar-track{
        background: transparent;
    }
    .ChatBox_Message_Container::-webkit-scrollbar-thumb{
        max-width: 250px;
        background: #4c9d63ce;

    }

} */
</style>
