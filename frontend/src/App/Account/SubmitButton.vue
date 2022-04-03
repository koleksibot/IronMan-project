<template>
        <div class="Submit_ButtonHolder">
            <button type="submit">{{ buttonText }}
                <img src="@/assets/AccountIcons/Icon material-send.svg">
            </button>
        </div>
</template>

<script>
export default {
    name: 'SubmitButton',
    props:{
        buttonText:String
    }
}
</script>


<style scoped>
.Submit_ButtonHolder{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.Submit_ButtonHolder button{
    height: 40px;
    padding: 0px;
    width: 150px;
    border-radius: 40px;
    border: 2px solid #00fffb;
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 16px;
    color: #0A671A;
    font-variant: small-caps;
}
.Submit_ButtonHolder button:focus{
    outline: 0;
}
.Submit_ButtonHolder button img{
    height: 30px;
    width: 30px;
    padding: 5px;
}
</style>