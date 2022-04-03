<template>
    <div>
        <OtherHeader/>
        <HomeAside/>
        <ChatSection/>
    </div>
</template>


<script>
import OtherHeader from '@/Components/BasicComponents/OtherHeader.vue'
import HomeAside from '@/Components/F1Homecomponents/f3HomeAside.vue'
import ChatSection from '@/Components/F3ChatComponents/f3Chat_Section.vue'

export default {
    name: 'ChatBase',
    components:{
        OtherHeader,
        HomeAside,
        ChatSection,
    },
    mounted(){
        let WhereAmI = this.$route.matched[0].name
        this.$store.dispatch('fetchWhereAmI', WhereAmI);
    }
}
</script>

<style scoped>

</style>