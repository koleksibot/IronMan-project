<template>
    <section class="Hide_Scroll_button">
        <div class="UserProfileBase_Conatainer Profile_ContainerCommon_Style">
            <div class="Profile_Holder_Conatainer">
                <NormalProfileCard/>
            </div>
        </div>
        <div class="UserProfile_Dynamic_Container Profile_ContainerCommon_Style">
            <div class="Dynamic_Holder_Conatainer Scroll_Button_Container">
                <!-- <RandomText/> -->
            </div>
        </div>
    </section>
</template>


<script>
import NormalProfileCard from '@/App/A2Profile/NormalProfile/ProfileComponents/NormalProfileCard.vue'
// import RandomText from '@/App/Test/RandomText.vue'
export default {
    name: 'NormalProfile',
    components:{
        NormalProfileCard,
        // RandomText,
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
    grid-template-columns: 1fr;
    grid-template-rows: 100vh;
    overflow: auto;
}
.Profile_ContainerCommon_Style{
    max-height: 100vh;

}
.UserProfileBase_Conatainer{
    height: auto;
    width: 100%;
}

.Profile_Holder_Conatainer{
    height: 100%;
    overflow: auto;
    box-shadow: 0px 0px 3px rgb(105, 106, 105);
}

.UserProfile_Dynamic_Container{
    width: 100%;
    height: 100vh;
    padding-bottom: 85px;
}
.Dynamic_Holder_Conatainer{
    height: 100%;
    overflow: auto;
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
    .Profile_ContainerCommon_Style{
        box-sizing: border-box;
        padding: 0px 5px;
        max-height: 100vh;
        padding-bottom: 90px;

    }
    .Profile_Holder_Conatainer{
        height: auto;
        box-shadow: 0px 0px 3px rgb(105, 106, 105);

    }
    .UserProfileBase_Conatainer{
        height: 100%;
        width: 100%;
        overflow: auto;
    }
    .UserProfile_Dynamic_Container{
        width: auto;
    }
    .Dynamic_Holder_Conatainer{
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