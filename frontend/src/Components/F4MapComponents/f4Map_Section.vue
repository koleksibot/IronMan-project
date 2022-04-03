<template>
    <section>
        <h3>It is our Map </h3> 
        <h4>Now in Development</h4>
    </section>
</template>

<script>
export default {
    name: 'MapSection'
}
</script>

<style scoped>
section{
    position: relative;
    height: 100vh;
    background: #e8e8e8;
    position: fixed;
    padding-top: 40px;
    padding-bottom: 40px;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 100vh;
}

@media only screen and (max-width:600px){
    section{
        width: 100%;
    }
}

@media only screen and (min-width:600px){
    section{
        width: 75%;
    }
}
@media only screen and (min-width:750px){
    section{
        width: 80%;
        position: relative;
        height: 100vh;
        position: fixed;
        background: transparent;
        padding-top: 45px;
        padding-bottom: 45px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 100vh;
    }
}
</style>