<template>
        <div class="Profile_Picture_holderimg">
            <router-link :to="{'name': 'OthersProfile', params: {id: this.id}}">
                <img :src="img_url" alt="ProPic">
            </router-link>
        </div>
</template>


<script>
export default {
    name: 'ListProfilePicture',
    props:{
        id:Number,
        img_url:String,
    },
}
</script>


<style scoped>
.Profile_Picture_holder{
    height: 40px;
    width: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.Profile_Picture_holder img{
    height: 30px;
    width: 30px;
    border-radius: 50%;
    background: #ddd;
    overflow: hidden;
    border: 1px solid red;
    object-fit: cover;
}
</style>