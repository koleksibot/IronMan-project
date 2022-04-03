<template>
    <div class="NormalProfile_Update_FromHolder">
        <form @submit.prevent="UserProfileUpdate" method="put">

            <!-- NAME INPUT -->
            <div class="ProfileFrom_InputContainer">
                <span>Name:</span>
                <input type="text" name="name" class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.name"/>
            </div>

            <!-- ADDRESS INPUT -->
            <div class="ProfileFrom_InputContainer">
                <span>Address:</span>
                <input type="text" class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.address" />
            </div>

            <!-- STATUS INPUT -->
            <div class="ProfileFrom_InputContainer">
                <span>Status:</span>
                <input type="text" class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.status" />
            </div>

            <!-- AGE INPUT -->
            <div class="ProfileFrom_InputContainer">
                <span>Age:</span>
                <input type="number" maxlength="2" class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.age" />
            </div>

            <!-- GENDER INPUT -->
            <div class="ProfileFrom_InputContainer">
                <span>Gender:</span>
                <select name="cars" class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.gender">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="TransGen">TransGen</option>
                </select>
            </div>

            <!-- ABOUT ME -->
            <div class="ProfileFrom_InputContainer">
                <span>About Me:</span>
                <textarea class="Input_OutLine_Zero" v-model="profileDetails.normalprofile.more_info" ></textarea>
            </div>

            <!-- IMAGE INPUT -->
            <!-- <div class="Profile_Picture_Upload">
                <input type="file" id="id_profile_pick" class="Hide_Container">
                <label for="id_profile_pick">
                    <img src="@/assets/ProfileIcons/Folder_Icon.svg" alt="file Icon">
                    Choose Your Profile Picture:
                </label>
            </div> -->

            <div class="SubmitButton_Container">
                <button type="submit" class="Save_Btn button_OutLine_Zero">Save Changes</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'NormalProfileUpdageForm',
    computed:{
        profileDetails(){
            return this.$store.state.ProfileDetails.profiledetails
        }
    },
    methods:{
        UserProfileUpdate(){
            this.$store.dispatch('ProfileUpdate', {
                name: this.profileDetails.normalprofile.name,
                address: this.profileDetails.normalprofile.address,
                status: this.profileDetails.normalprofile.status,
                age: this.profileDetails.normalprofile.age,
                gender: this.profileDetails.normalprofile.gender,
                description: this.profileDetails.normalprofile.more_info
            })
            
            .then(success => {
                if (success.status === 200){
                    // this.$router.push({'name': 'NormalProfile'})
                    console.warn('success')
                }
            })
            .catch(err =>{
                this.LoginError = true
                console.warn(err)
            })
        },
    }
}
</script>

<style scoped>
.NormalProfile_Update_FromHolder{
    width: 100%;
    height: auto;
    padding-bottom: 5px;
}
.NormalProfile_Update_FromHolder form{
    width: 100%;
}
.ProfileFrom_InputContainer{
    width: 100%;
    display: inline-block;
    margin: 5px 0px;
}
.ProfileFrom_InputContainer:first-child{
    margin-top: 0px;
}
.ProfileFrom_InputContainer span{
    min-width: 20%;
    float: left;
    color: #04928b;
    font-weight: bold;
    height: 20px;
    font-size: 14px;
}
.ProfileFrom_InputContainer input{
    min-width: 75%;
    margin-right: 5px;
    height: 20px;
    border: none;
    border-bottom: 1px solid purple;
    font-size: 14px;
}
.ProfileFrom_InputContainer select{
    min-width: 75%;
    margin-right: 5px;
    height: 20px;
    border: none;
    border-bottom: 1px solid purple;
    font-size: 14px;
}
.ProfileFrom_InputContainer textarea{
    min-width: 90%;
    height: 100px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid purple;
    font-size: 14px;
    resize: none;
}

.Profile_Picture_Upload{
    height: 30px;
}



.SubmitButton_Container{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.Save_Btn{
    min-width: 100px;
    padding: 0px 10px;
    height: 30px;
    margin: 5px;
    font-weight: bold;
    border-radius: 30px;
    border: none;
    background: rgba(102, 250, 57, 0.2);
    border: 1px solid #035328;
    color: #035328;
}

</style>