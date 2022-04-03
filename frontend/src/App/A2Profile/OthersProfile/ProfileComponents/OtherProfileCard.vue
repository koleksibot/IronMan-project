<template>
    <div class="ProfileCard_Holder">

        <div v-if="OthersProfileDetails">
            <div class="ProfileFront_Container">
                <div class="ProfileBackground_container">
                </div>
                
                <div class="User_status">
                    $status: {{ OthersProfileDetails.normalprofile.status }}
                </div>
            
                <div class="Profile_Picture_holder">
                    <img v-if="OthersProfileDetails.normalprofile.img_url" :src="OthersProfileDetails.normalprofile.img_url" alt="Profile-P">
                    <img v-else src="@/assets/ProfileIcons/Profile_icon.svg" alt="Profile-P">
                </div>

                <div class="UserName_Container">
                    {{ OthersProfileDetails.normalprofile.name }}

                    <span v-if="(authUser != OthersProfileDetails.id)">
                        <FollowUnfollowButton :id="OthersProfileDetails.id" :is_following="OthersProfileDetails.is_following"/>
                    </span>
                </div>
            </div>

            <div class="ProfileDetails_Holder">
                <span v-if="(OthersProfileDetails.normalprofile.address != null)" class="Information_style"> <em>Address:</em> {{ OthersProfileDetails.normalprofile.address }}</span><br>
                <span class="Information_style"> <em>Age:</em> {{ OthersProfileDetails.normalprofile.age }}</span>|
                <span class="Information_style"> <em>Gender:</em> {{ OthersProfileDetails.normalprofile.gender }}</span><br>
                <span v-if="(OthersProfileDetails.normalprofile.more_info != null)" class="Information_style"> <em>About Me:</em> {{ OthersProfileDetails.normalprofile.more_info }}</span>
            </div>

            <div class="Followers_Following_Holder">
                <span>Followers: {{ OthersProfileDetails.get_total_followers }}</span>|
                <span>Following: {{ OthersProfileDetails.get_total_following }}</span>|
            </div>

        </div>
        
    </div>
</template>


<script>
import FollowUnfollowButton from '@/Components/BasicComponents/FollowUnfollowBtn.vue'
export default {
    name: 'OthersProfileCard',
    components:{
        FollowUnfollowButton,
    },
    mounted(){
        let UserId = this.$route.params.id
        this.$store.dispatch('fetchProfileListDetails', UserId);
    },
    computed:{
        OthersProfileDetails(){
            return this.$store.state.ProfileList.profileListDetails
        }
    },
    data(){
        return{
            authUser: localStorage.getItem('id')
        }
    }
}
</script>


<style scoped>
.ProfileCard_Holder{
    width: 100%;
    height: auto;
    background: #fff;
}
.ProfileFront_Container{
    overflow: hidden;
    height: 200px;
    /* height: auto; */
    width: 100%;
    background: green;
}
.ProfileBackground_container{
    width: 100%;
    height: 200px;
    background: #fff;
    position: relative;
}
.ProfileBackground_container::before{
    content: "";
    height: 200px;
    width: 50%;
    margin-left: -50%;
    position: absolute;
    background: linear-gradient(45deg, rgba(5,233,111,1) 0%, rgb(229, 252, 240) 70%);
    border-top-right-radius: 100%;
}
.ProfileBackground_container::after{
    content: "";
    height: 200px;
    width: 50%;
    position: absolute;
    background: linear-gradient(225deg, rgba(5,225,233,0.7) 0%, rgb(224, 254, 255) 70%);
    border-bottom-left-radius: 100%;
}
.User_status{
    height: auto;
    max-width: 100%;
    text-align: center;
    transform: translateY(-200px);
}
.Profile_Picture_holder{
    height: 100px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translateY(-180px);
}
.Profile_Picture_holder img{
    height: 100px;
    width: 100px;
    border-radius: 50%;
    background: #eceded;
    border: 2px solid #fff;
    overflow: hidden;
    object-fit: cover;
}
.UserName_Container{
    /* color: rgb(72, 71, 71); */
    color: #04928b;
    font-weight: bold;
    padding: 5px 0px;
    text-shadow: 0.5px 0px 1px #333;
    transform: translateY(-180px);
}



.ProfileDetails_Holder{
    background: #c7f8f67b;
    color: #04928b;
    padding: 5px;
}

.Information_style em{
    font-weight: bold;
    font-style: normal;
    color: #004148;
}



.Followers_Following_Holder{
    width: 90%;
    margin-left: 5%;
    height: 20px;
    border-radius: 20px;
    background: #2e2e2e80;
    color: #fff;
    padding: 5px 0px;
    margin-bottom: 5px;
    margin-top: 2px;
}
</style>