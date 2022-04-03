<template>
    <div class="ProfileCard_Holder">

        <div v-if="(profileDetails != null)">
            <div class="ProfileFront_Container">
                <div class="ProfileBackground_container">
                </div>
                
                <div class="User_status">
                    $status: {{ profileDetails.normalprofile.status }}
                </div>
            
                <div class="Profile_Picture_holder">
                    <img v-if="profileDetails.normalprofile.img_url" :src="profileDetails.normalprofile.img_url" alt="Profile-P">
                </div>

                <div class="UserName_Container">
                    {{ profileDetails.normalprofile.name }}
                </div>
            </div>

            <div class="EditProfie_Btn_container">
                <button v-if="profileBesicDetails" v-on:click="callEditProfile" class="CallUpdate_Profile button_OutLine_Zero">
                    <img src="@/assets/ProfileIcons/Edit_Profile.svg" alt="edit">Edit Profile
                </button>
                <button type="button" class="Cnacel_Btn button_OutLine_Zero" v-else v-on:click="cnacelEditProfile">
                    Close
                </button>
            </div>

            <div v-if="profileBesicDetails" class="ProfileDetails_Holder">
                <span v-if="(profileDetails.normalprofile.address != null)" class="Information_style"> <em>Address:</em>  {{ profileDetails.normalprofile.address }}</span><br>
                <span class="Information_style"> <em>Age:</em>  {{ profileDetails.normalprofile.age }}</span><br>
                <span class="Information_style"> <em>Gender:</em> {{ profileDetails.normalprofile.gender }}</span><br>
                <span v-if="(profileDetails.normalprofile.more_info != null)" class="Information_style"> <em>About Me:</em> {{ profileDetails.normalprofile.more_info }}</span>
            </div>

            <div v-else>
                <ProfileUpdateForm/>
            </div>

            <div class="Followers_Following_Holder">
                <span>Followers: {{ profileDetails.get_total_followers }}</span>|
                <span>Following: {{ profileDetails.get_total_following }}</span>|
            </div>


        </div>
        
        <div>
            <OtherLinks/>
        </div>

    </div>
</template>


<script>
import OtherLinks from '@/Components/F2ProfileComponents/OthersLinks.vue'
import ProfileUpdateForm from '@/App/A2Profile/NormalProfile/ProfileRelatedForms/NormalProfile_updateForm.vue'

import { mapActions } from 'vuex'
export default {
    name: 'NormalProfileCard',
    components:{
        OtherLinks,
        ProfileUpdateForm,
    },
    data(){
        return{
            profileBesicDetails: true,
            tester: 'gandu sala'
        }
    },
    methods: {
        ...mapActions(['fetchProfileDetails']),
        callEditProfile(){
            this.profileBesicDetails = false;
        },
        cnacelEditProfile(){
            this.profileBesicDetails = true;
        }
    },
    computed:{
        profileDetails(){
            return this.$store.state.ProfileDetails.profiledetails
        }
    },
    created(){
        this.fetchProfileDetails();
    },
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
    color: #04928b;
    font-weight: bold;
    padding: 5px 0px;
    text-shadow: 0.5px 0px 1px #333;
    transform: translateY(-180px);
}

.EditProfie_Btn_container{
    float: right;
    margin-right: 10px;
}
.CallUpdate_Profile{
    height: 30px;
    width: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 30px;
    padding: 0px 5px;
    background: #fff;
    color: blue;
    border: 1px solid blue;
    font-weight: bold;
    transform: translateY(-40px);
}
.CallUpdate_Profile img{
    height: 22px;
    width: 22px;
}
.Cnacel_Btn{
    height: 30px;
    min-width: 100px;
    padding: 0px 5px;
    font-weight: bold;
    border-radius: 30px;
    border: none;
    background: #FFF;
    border: 1px solid #FF0000;
    color: #FF0000;
    transform: translateY(-40px);
    z-index: 1;
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