<template>
    <div class="Home_Holder">
        <div class="Home_Fixed_Container">
            <transition name="slither">
                <router-view/>
            </transition>
        </div>
        
        <div class="Home_DynamicConatainer">
            <HomeHeader/>
            <HomeNav/>
            <HomeAside/>
            <HomeSection/>
        </div>
    </div>
</template>


<script>
import HomeHeader from '@/Components/F1Homecomponents/f1HomeHeader.vue'
import HomeNav from '@/Components/F1Homecomponents/f2HomeNav.vue'
import HomeAside from '@/Components/F1Homecomponents/f3HomeAside.vue'
import HomeSection from '@/Components/F1Homecomponents/f4HomeSection.vue'


export default {
    name: 'HomeBase',
    components:{
        HomeHeader,
        HomeNav,
        HomeAside,
        HomeSection,
    },
    mounted(){
        let WhereAmI = this.$route.matched[0].name
        this.$store.dispatch('fetchWhereAmI', WhereAmI);
    }
}
</script>

<style scoped>
.slither-enter-active, .slither-leave-active {
    transition: transform 1s;
}

.slither-enter, .slither-leave-to {
    /* transform: translateX(-100%); */
    opacity: 0;
    transition: all 0.5s ease;
  
}

.slither-enter-to, .slither-leave {
    /* transform: translateX(0); */
    transition: all 0.5s ease;
}



#Home_Holder{
    position: absolute;
    margin: 0px;
    padding: 0px;
    height: auto;
    width: 100%;
}
.Home_Fixed_Container{
    position: fixed;
    height: auto;
    width: 100%;
    z-index: 1500;
    background: transparent;
    /* background: rgba(255, 68, 0, 0.823); */
}
.Home_DynamicConatainer{
    position: relative;
}


@media only screen and (max-width: 480px){
  .slither-enter, .slither-leave-to {
        transform: translateX(-100%);
        opacity: 0;
        transition: all 0.7s ease;
    
    }

    .slither-enter-to, .slither-leave {
        transform: translateX(0);
        transition: all 0.7s ease;
    }
}
</style>