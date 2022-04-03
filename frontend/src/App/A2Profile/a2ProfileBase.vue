<template>
<div class="Profile_Holder">
    <div class="Profile_DynamicConatainer">
        <OtherHeader/>
        <HomeAside/>
        <ProfileSection/>
    </div>
</div>
</template>


<script>
import OtherHeader from '@/Components/BasicComponents/OtherHeader.vue'
import ProfileSection from './ProfileSection.vue'
import HomeAside from '@/Components/F1Homecomponents/f3HomeAside.vue'

export default {
    middleware: ['auth-guard'],
    name: 'ProfileBase',
    components:{
        OtherHeader,
        ProfileSection,
        HomeAside,
    },
    mounted(){
        let WhereAmI = this.$route.matched[0].name
        this.$store.dispatch('fetchWhereAmI', WhereAmI);
    }
}
</script>

<style scoped>

#Home_Holder{
    position: absolute;
    margin: 0px;
    padding: 0px;
    height: auto;
    width: 100%;
}
/* .Profile_Fixed_Container{
    position: fixed;
    height: auto;
    background: rgba(0, 0, 255, 0.453);
    width: 100%;
    z-index: 1500;
    background: transparent;
} */
.Profile_DynamicConatainer{
    position: relative;
}

</style>