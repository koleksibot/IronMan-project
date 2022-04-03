<template>
        <div class="NormalForms_ButtonHolder">
            <button>
                {{ buttonText }}
            </button>
        </div>
</template>

<script>
export default {
    name: 'NormalFormsButton',
    props:{
        buttonText:String
    }
}
</script>


<style scoped>
.NormalForms_ButtonHolder{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.NormalForms_ButtonHolder button{
    margin-top: 10px;
    height: 40px;
    padding: 0px;
    min-width: 150px;
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
.NormalForms_ButtonHolder button:focus{
    outline: 0;
}
</style>