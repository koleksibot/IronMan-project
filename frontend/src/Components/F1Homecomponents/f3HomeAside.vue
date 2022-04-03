<template>
    <aside class="Hide_HomeAside" id="Home_aside">
        <div class="Hider_HomeAside" v-on:click="hideBaseAside"></div>
        <div class="Menu_HomeAside">
            <HomeAsideMenu/>
        </div>
    </aside>
</template>


<script>
import HomeAsideMenu from './f3HomeAsideMenu/f3HomeAsideMenu.vue'

export default {
    name: 'HomeAside',
    components:{
        HomeAsideMenu
    },
    methods:{
        hideBaseAside(){
            let asideContainer = document.getElementById('Home_aside');
            asideContainer.classList.add('Hide_HomeAside');
        }
    }
}
</script>


<style scoped>
aside{
    width: 100%;
    height: 100vh;
    position: fixed;
    background: transparent;
    display: flex;
    z-index: 1000;
}
.Hider_HomeAside{
    width: 40%;
    height: 100%;
    background: transparent;
}
.Menu_HomeAside{
    width: 60%;
    height: 100%;
    background: #fffffff2;
    overflow: auto;
    box-shadow: -2px 0px 2px #bbb;
}
@media only screen and (max-width:600px){
    .Hide_HomeAside{
        display: none;
    }
}
@media only screen and (min-width:600px){
    aside{
        width: 25%;
        margin-left: 75%;
    }
    .Hider_HomeAside{
        display: none;
    }
    .Menu_HomeAside{
        width: 100%;
    }
}
@media only screen and (min-width:750px){
    aside{
        width: 20%;
        margin-left: 80%;
        z-index: 800;
    }
}
@media only screen and (min-width:1000px){
    aside{
        width: 16%;
        margin-left: 84%;
    }
}
@media only screen and (min-width:1200px){
    aside{
        width: 14%;
        margin-left: 86%;
    }
}

</style>