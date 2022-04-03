<template>
    <div class="UserList_Container">
        <div class="UsersList_InnerContent_Holder">
            <div class="Profile_Picture_holder" >
            </div>

            <div class="Name_and_Description_holder" v-if="allChatUserList">
                {{ allChatUserList.comments }}
            </div>
            <div class="OthersLink_holder">
            </div>
        </div>
    </div>
</template>


<script>
import { mapGetters, mapActions} from 'vuex';
export default {
    name: 'MessageUserList',
    methods: {
        ...mapActions(['fetchChatUserList']),
    },
    computed: mapGetters(["allChatUserList"]),
    created(){
        this.fetchChatUserList();
    },
}
</script>

<style scoped>

.UserList_Container{
    height: auto;
    width: 99%;
    padding: 0px 0.5%;
    background: transparent;
}
.UsersList_InnerContent_Holder{
    background: #fff;
    height: 40px;
    width: 100%;
    display: grid;
    grid-template-columns: 40px 1fr 100px;
    grid-template-rows: 1fr;
    margin: 2px 0px;
    grid-gap: 3px;
}


.Profile_Picture_holder{
    height: 40px;
    width: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.Profile_Picture_holder img{
    height: 30px;
    width: 30px;
    border-radius: 50%;
    background: #ddd;
    overflow: hidden;
    border: 1px solid red;
    object-fit: cover;
}

.Name_and_Description_holder{
    display: inline-block;
    text-align: left;
    font-size: 13px;
    font-weight: bold;
    overflow: auto;

}

.OthersLink_holder{
    height: 100%;
    width: 100%;
    display: inline-flex;
    overflow: hidden;
    align-items: center;
    justify-content: center;
    margin-right: 5px;
}

</style>