<template>
<div>
    <OtherHeader/>
    <HomeAside/>
    <CartSection/>
</div>
</template>


<script>
import OtherHeader from '@/Components/BasicComponents/OtherHeader.vue'
import CartSection from '@/Components/F5CartComponents/f5Cart_Section.vue'
import HomeAside from '@/Components/F1Homecomponents/f3HomeAside.vue'

export default {
    name: 'CartBase',
    components:{
        OtherHeader,
        HomeAside,
        CartSection,
    },
    mounted(){
        let WhereAmI = this.$route.matched[0].name
        this.$store.dispatch('fetchWhereAmI', WhereAmI);
    }
}
</script>

<style scoped>

</style>