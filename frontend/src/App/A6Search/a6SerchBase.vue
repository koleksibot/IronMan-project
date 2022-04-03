<template>
    <div class="SerchPage_BaseContainer">
        <div class="SerchBox_container">
            <div class="Search_BackButton_Holder">
                <button v-on:click="HideSearchButton" class="stleSerch_SectionButton button_OutLine_Zero">
                    <img src="@/assets/BaseIcons/Back.svg">
                </button>
            </div>
            <div class="Search_Box_Input_Container">
                <input type="search" class="Input_OutLine_Zero" placeholder="Search Here">
            </div>
            <div class="Search_ActionButton_Holder"> 
                <button class="stleSerch_SectionButton button_OutLine_Zero">
                    <img src="@/assets/BaseIcons/SearchGreen.svg">
                </button>
            </div>
        </div>

        <div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SearchBase',
    methods:{
        HideSearchButton(){
            let search_button = document.getElementById('Search_Container')
            search_button.classList.add('Hide_Search_Container')
        }
    }
}
</script>


<style scoped>
.SerchPage_BaseContainer{
    height: auto;
    background: #fff;
    min-height: 40px;
    z-index: 1000;
}
.SerchBox_container{
    display: grid;
    grid-template-columns: 40px 1fr 40px;
    height: 40px;
    align-items: center;
}
.Search_Box_Input_Container{
    width: 100%;
}

.Search_Box_Input_Container input{
    width: 100%;
    height: 35px;
    border: none;
    border-bottom: 2px solid #04928b;
    font-size: 14px;
}
.Search_Box_Input_Container input:hover{
    transition: 0.3s;
    border-bottom: 2px solid blue;
}
.stleSerch_SectionButton{
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: transparent;
    justify-content: center;
    display: flex;
    align-items: center;
    border: none;

}


@media only screen and (min-width:600px){
    .SerchPage_BaseContainer{
        float: right;
        width: 75%;
        margin-right: 25%;
        background: transparent;
        font-size: 16px;
    }
    .SerchBox_container{
        width: 90%;
        margin-left: 10%;
    }
    .Search_Box_Input_Container input{
        width: 100%;
        height: 35px;
        border-radius: 35px;
        padding: 0px 40px;
        border: none;
        box-shadow: inset 0px 0px 3px #04928b;
    }
    .Search_Box_Input_Container input:hover{
        border-bottom: none;
        box-shadow: inset 0px 0px 3px #023d3a;
    }
    .Search_BackButton_Holder{
        transform: translateX(40px);
    }
    .Search_ActionButton_Holder{
        transform: translateX(-40px);
    }
}
@media only screen and (min-width: 720px){
    .SerchPage_BaseContainer{
        width: 80%;
        margin-right: 20%;
    }
}
@media only screen and (min-width:1000px){
    .SerchPage_BaseContainer{
        width: 84%;
        margin-right: 16%;
    }
}
@media only screen and (min-width:1200px){
    .SerchPage_BaseContainer{
        width: 86%;
        margin-right: 14%;
    }
}

</style>