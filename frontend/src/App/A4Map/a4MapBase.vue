<template>
<div>
    <OtherHeader/>
    <HomeAside/>
    <MapSection/>
</div>
</template>


<script>
import OtherHeader from '@/Components/BasicComponents/OtherHeader.vue'
import MapSection from '@/Components/F4MapComponents/f4Map_Section.vue'
import HomeAside from '@/Components/F1Homecomponents/f3HomeAside.vue'
export default {
    name: 'MapBase',
    components:{
        OtherHeader,
        HomeAside,
        MapSection,
    },
    mounted(){
        let WhereAmI = this.$route.matched[0].name
        this.$store.dispatch('fetchWhereAmI', WhereAmI);
    }
}
</script>

<style scoped>

</style>