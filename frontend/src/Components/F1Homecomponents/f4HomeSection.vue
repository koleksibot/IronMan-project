<template>
    <section>
        <BasicProductCard/>
    </section>
</template>


<script>
import BasicProductCard from '@/Components/F8Cards/f8ProductRelated/BasicProductCard.vue';

export default {
    name: 'HomeSection',
    components:{
        BasicProductCard,
    }
}
</script>




<style scoped>
section{
    position: relative;
    min-height: auto;
    background: transparent;
    padding-top: 80px;
    padding-bottom: 45px;
    background: #e8e8e8;

}
@media only screen and (min-width:600px){
    section{
        width: 75%;
    }

}
@media only screen and (min-width:750px){
    section{
        width: 80%;
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