<template>
    <header id="baseHeader">
        <div class="Align_HederContent Logo">ataOta</div>
        <div class="Align_HederContent">
            <button v-on:click="ShowSearchButton">
                <img src="@/assets/BaseIcons/SearchGreen.svg">
            </button>
        </div>
        <div class="Align_HederContent">
            <button>
                <img src="@/assets/BaseIcons/FilterGreen.svg">
            </button>
        </div>
        <div class="Align_HederContent">
            <button>
                <img src="@/assets/BaseIcons/Notifications.svg">
            </button>
        </div>
        <div class="Align_HederContent">
            <button v-on:click="displayBaseAside" id="HideWindow_Menu">
                <img src="@/assets/BaseIcons/WindowMenuGreen.svg">
            </button>
        </div>
    </header>
</template>


<script>
export default {
    name: 'HomeHeader',
    methods:{
        displayBaseAside(){
            let asideContainer = document.getElementById('Home_aside');
            asideContainer.classList.remove('Hide_HomeAside');
        },
        ShowSearchButton(){
            let search_button = document.getElementById('Search_Container')
            search_button.classList.remove('Hide_Search_Container')
        }
    }
}
</script>


<style scoped>
header{
    width: 100%;
    height: 40px;
    position: fixed;
    background: #ffffff;
    display: grid;
    grid-template-columns: 1fr 40px 40px 40px 40px;
    z-index: 800;
}
.Logo{
    color: #04928b;
    font-weight: bold;
}
.Align_HederContent{
    display: flex;
    align-items: center;
    border-radius: 50px;
}
.Align_HederContent:first-child{
    margin-left: 5px;
}

.Align_HederContent button{
    padding: 7px;
    border-radius: 50%;
    background: #eceded;
    justify-content: center;
    display: flex;
    align-items: center;
    border: none;
}
.Align_HederContent button:hover{
    background: #d2f7ff;
}
.Align_HederContent button:focus{
    outline: 0;
}
.Align_HederContent button img{
    height: 20px;
    width: 20px;
}


@media only screen and (min-width:600px){
    header{
        width: 75%;
    }
    #HideWindow_Menu{
        display: none;
    }
}
@media only screen and (min-width:750px){
    header{
        width: 80%;
    }
}
@media only screen and (min-width:1000px){
    header{
        width: 84%;
    }
}
@media only screen and (min-width:1200px){
    header{
        width: 86%;
    }
}
</style>
