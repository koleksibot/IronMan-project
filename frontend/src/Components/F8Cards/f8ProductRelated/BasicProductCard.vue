<template>
        <div class="Product_Holder">
        <div class="Product_Card_Holder">

            <!-- Card 1 -->
            <div v-for="product in allProductsList" v-bind:key="product.id"  class="product_Card">

                <!-- Product Name Container -->
                <div class="Product_Name_Container">
                    {{product.prod_name}}
                </div>

                <!-- Product Image Container -->
                <div class="Product_Image_Container">
                    <img :src="product.prod_picture_url">

                    <!-- Product Offer Container -->
                    <div class="Product_Offer_Container">
                        Offer:{{product.prod_offer}}%
                    </div>
                </div>

                <!-- Product Description Container -->
                <div class="Product_Description_Container">
                    <span>{{product.prod_description}}</span>
                </div>

                <!-- Product Price -->
                <div class="Product_Price_Container">
                        Price: Rs.-{{product.prod_price}}/{{product.quantity}}-{{product.in_terms_of}}
                </div>

                <!-- Product Origin -->
                <div class="Product_Country_Of_Origin_Container">
                    Made In: {{ product.country_Of_Origin }}
                </div>

                <!-- Product Links Container -->
                <div class="Product_Links_Container">
                    <!-- <a href="#">Buy</a>
                    <a href="#">Detail</a> -->
                    <button class="button_OutLine_Zero">Cart</button>
                </div>
                
            </div>

        </div>

    </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex';
export default {
    name: 'BasicProductCard',
    methods: {
        ...mapActions(['fetchProductsList']),
    },
    computed: mapGetters(["allProductsList"]),
    created(){
        this.fetchProductsList();
    },
}
</script>

<style scoped>
.Product_Holder{
    width: 100%;
    display: grid;
    grid-template-columns: 1fr repeat(12, minmax(auto, 120px)) 1fr;
    padding: 10px 0;
    font-weight: 400;
    font-family: sans-serif;
    grid-gap: 10px;
    background: transparent;
}

.Product_Card_Holder{
    grid-column: 2/ span 12;
    display: grid;
    grid-template-columns: repeat(12, minmax(auto, 200px));
    grid-gap: 10px;
}

.product_Card{
    grid-column-end: span 2;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    cursor: pointer;
    transition: all 0.3s ease 0.3s;
    font-size: 13px;
    border-radius: 3px;
}
.product_Card:hover{
    box-shadow: 0px 0px 5px #2e45ca;
}
/* <!-- Product Name Container --> */
.Product_Name_Container{
    text-align: center;
    overflow: hidden;
    padding: 3px 0px;
    color: #04928b;
    /* color: #159AC4; */
    font-weight: 600;
}

/* <!-- Product Image Container --> */
.Product_Image_Container{
    grid-column-end: span 3;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    cursor: pointer;
    transition: all 0.3s ease 0.3s;
    font-size: 14px;
    height: 200px;
    overflow: hidden;
}
.Product_Image_Container img{
    width: 100%;
    height: 100%;
    object-fit: contain;
    z-index: 0;
}

/* <!-- Product Offer Container --> */
.Product_Offer_Container{
    position: relative;
    background-color: #0000007c;
    width: 5em;
    color: #fff;
    transform: translateY(-15px);
}


/* <!-- Product Description Container --> */
.Product_Description_Container{
    display: block;
    overflow: hidden;
    text-align: center;
    color: gray;
    font-size: 12px;
    max-height: 40px;
}

/* <!-- Product Price --> */
.Product_Price_Container{
    float: left;
    background-color: #bcfffc;
    font-weight: bold;
    padding: 3px;
    font-size: 12px;
}

/* <!-- Product Origin --> */
.Product_Country_Of_Origin_Container{
    text-align: center;
    color: #03095e;
    font-size: 12px;
}


/* <!-- Product Links Container --> */
.Product_Links_Container{
    display: flex;
    justify-content: space-evenly;
    padding: 5px 0px;
}
.Product_Links_Container button{
    text-decoration: none;
    padding: 2px 5px;
    border-radius: 10px;
    font-weight: bold;
    background-color: #c0fabb;
    color: #024d05;
    border: 1px solid #024d05;
    
}
.Product_Links_Container button:hover{
    background-color: #babaff;
    color: #000063;
    border: 1px solid #000063;
}

@media only screen and (max-width: 1000px){
    .Product_Holder{
        grid-template-columns: 1fr repeat(12, minmax(auto, 80px)) 1fr;
        grid-gap: 10px;
        padding: 10px 0;
    }

    .Product_Card_Holder{
        grid-column: 2/ span 12;
        grid-template-columns: repeat(12, minmax(auto, 80px));
        grid-gap: 5px;
    }

    .product_Card{
        grid-column-end: span 4;
    }
    /* <!-- Product Image Container --> */
    .Product_Image_Container{
        height: 140px;
    }
}

@media only screen and (max-width: 580px){
    .Product_Holder{
        width: 98%;
        grid-template-columns: 1fr repeat(10, minmax(auto, 60px)) 1fr;
        grid-gap: 0px;
        padding: 5px 1%;
    }

    .Product_Card_Holder{
        grid-column: 2/ span 10;
        grid-template-columns: repeat(10, minmax(auto, 60px));
        grid-gap: 8px;
    }

    .product_Card{
        grid-column-end: span 5;
    }
}

</style>