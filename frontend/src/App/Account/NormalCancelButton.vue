<template>
        <button class="Cancel_Button">
            {{ ButtonText }}
        </button>
</template>

<script>
export default {
    name: 'NormalCancelButton',
    props:{
        ButtonText:String
    }
}
</script>


<style scoped>
.Cancel_Button{
    min-height: 40px;
    margin-top: 10px;
    min-width: 140px;
    max-width: 300px;
    padding: 0px 5px;
    border-radius: 40px;
    background: #fde7e7;
    color: #ff4400;
    display: flex;
    align-items: center;
    justify-content: center;
    font-variant: small-caps;
    border: 2px solid #ff4400;
    font-size: 16px;
    font-weight: bolder;
    text-decoration: none;
}
.Cancel_Button:focus{
    outline: 0;
}
</style>