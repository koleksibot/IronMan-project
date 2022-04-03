<template>
    <div>
        <div class="Search_Container Hide_Search_Container" id="Search_Container">
            <SearchBase/>
        </div>
        <router-view/>
        <HomeFooter/>
    </div>
</template>

<script>
import SearchBase from '@/App/A6Search/a6SerchBase.vue'
import HomeFooter from '@/Components/F1Homecomponents/f5HomeFooter.vue'
export default {
    name: 'Base',
    components:{
        SearchBase,
        HomeFooter,
    },
}
</script>

<style>
.Search_Container{
    position: fixed;
    width: 100%;
    height: 100vh;
    /* background: orangered; */
    background: rgba(51, 51, 51, 0.282);
    z-index: 900;
}
.Hide_Search_Container{
    display: none;
}


.Hide_Scroll_button::-webkit-scrollbar{
    display: none;
}
@media only screen and (max-width: 480px){
    .Scroll_Button_Container::-webkit-scrollbar{
        display: none;
    }

    nav::-webkit-scrollbar{
        display: none;
    }
}
@media only screen and (min-width: 480px){
    .Scroll_Button_Container::-webkit-scrollbar{
        background: transparent;
        width: 10px;
    }
    .Scroll_Button_Container::-webkit-scrollbar-button{
        width: 5px;
    }
    .Scroll_Button_Container::-webkit-scrollbar-thumb{
        color: rgb(122, 252, 122);
        height: 100px;
    }
    .Scroll_Button_Container::-webkit-scrollbar-track{
        background: transparent;
    }
    .Scroll_Button_Container::-webkit-scrollbar-thumb{
        max-width: 250px;
        background: #4c9d63ce;

    }


    nav::-webkit-scrollbar{
        background: transparent;
        margin-top: 10px;
        height: 5px;
        position: absolute;
        transform: translateY(10px);
    }
    nav::-webkit-scrollbar-thumb{
        width: 200px;
        background-color: rgb(122, 252, 122);
    }

}
</style>
