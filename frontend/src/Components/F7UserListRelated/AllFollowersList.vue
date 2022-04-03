<template>
    <div class="UserList_Container">
        <div v-for="user in allFollowersList" v-bind:key="user[0].id" class="UsersList_InnerContent_Holder">

            
            <div class="Profile_Picture_holder" >
                <ProfileListPicture :id="user[0].id" :img_url="user[0].normalprofile.img_url"/>
            </div>

            <div class="Name_and_Description_holder">
                <span style="font-size: 12px;">
                    {{ user[0].normalprofile.name }} |
                </span>
                <span  style="font-size: 12px;">
                    followers: {{ user[0].get_total_followers }}| following: {{ user[0].get_total_following }}|
                </span>
                <span v-if="user[0].normalprofile.address != null" style="font-size: 12px;">
                    Address-{{ user[0].normalprofile.address }}
                </span>
            </div>
            <div class="OthersLink_holder">
                <FollowUnfollowButton :id="user[0].id" :is_following="user[0].is_following"/>
            </div>
        </div>
    </div>
</template>


<script>
import ProfileListPicture from '@/Components/BasicComponents/ListProfilePicture.vue'
import FollowUnfollowButton from '@/Components/BasicComponents/FollowUnfollowBtn.vue'
import { mapGetters, mapActions} from 'vuex';

export default {
    name: 'AllFollowersList',
    components:{
        ProfileListPicture,
        FollowUnfollowButton,
    },
    methods: {
        ...mapActions(['fetchFollowersList']),
    },
    computed: mapGetters(["allFollowersList"]),
    created(){
        this.fetchFollowersList();
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
    grid-template-columns: 40px 1fr auto auto;
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
    margin-right: 10px;
}

</style>