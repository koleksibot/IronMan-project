<template>

<div id="AboutUs_Holder">
    <header class="AboutUs_Header">
        <div class="Align_HederContent Logo">ataOta</div>
        <div class="Align_HederContent">
            <a @click="$router.go(-1)">
            <button>
                <img src="@/assets/BaseIcons/Back.svg">
            </button>
            </a>
        </div>
    </header>
    
    <div class="AboutUs_Description_Header">
        About ataOta
    </div>

    <div class="AboutUs_Description">
        <em>"Advance Technology Adoption and Organization of Technical Assistant"</em> as known as <em>"ataOta"</em>
        is an internet commerce marketspace where everyone can use the internet to provide an
        opportunity to create market at home, and serve customers in digital ways.
        Internet Commerce is the use of the Internet for all phases of creating and completing
        business transactions. <em>Established in October-2020.</em> It is designed by
        globally organized local community model which allows the disaster proof business
        operation to overcome all situations with safe and secure system. With help of Ataota you
        can discover your business through online and make a stable market to overcome all kinds of fallout.
    </div>


    <div class="AboutUs_Mission"><br>
        <div class="Mission_Heading">MISSION</div>
        <div class="Mission_Description">
            <ul>
                <li>
                    All Types of Legal Products and Services, Bring In Your Hand With Proper Location.
                </li><br>
                <li>Get Together and Serve Each Other.</li><br>
                <li>Add Value In Your and Our Life Simultaneously.</li><br>
            </ul>
        </div>
    </div>

    <div class="AboutUs_Mission">
        <div class="Mission_Heading">VISION</div>
        <div class="Mission_Description">We’re excited to help you on your journey!</div>
    </div>



    <div class="AboutUs_Empolyee_Details_Holder">
        <div  v-for="about in allAboutUs" v-bind:key="about.id" class="AboutUs_Empolyee_Details_Holder_InnerContainer">
            <div class="Employee_Image_Holder">
                <img :src="about.image_url" alt="/">
            </div>
            <div class="Basic_Details_Of_Employee">
                <span class="Employee_Name">{{ about.name }}</span><br/>
                <span class="Employee_Role">{{ about.role }}</span><br/>
                    {{ about.details }}
            </div>
        </div>
    </div>



    <div class="AboutUs_Footer">
        <div class="AboutUs_contactUs">
            <span class="Fotter_Heading">CONTACT US</span><br/>
            Call Us: *Soon We Add Our Official No.*<br/>
            support@ataota.in<br/>
            Tarakeswar pin- 712410<br/>
            Whatsapp, instagram,facebook,linkdn<br/>
        </div>
        <div class="AboutUs_customer_service">
            <span class="Fotter_Heading">CUSTOMER SERVICE</span><br/>
            Call Us: *Soon We Add Our Official No.*<br/>
            support@ataota.in<br/>
            Panskura pin- 721152<br/>
            Whatsapp, instagram,facebook,linkdn<br/>
        </div>
    </div>
</div>

</template>


<script>
import { mapGetters, mapActions} from 'vuex';


export default {
    name: 'AboutUs',
    methods: {
        ...mapActions(['fetchAboutUs']),
    },
    computed: mapGetters(["allAboutUs"]),
    created(){
        this.fetchAboutUs();
    }

}
</script>


<style scoped>
.Header_Search_Box form{
    display: none;
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
#AboutUs_Holder{
    max-width: 100%;
    height: 100vh;
    overflow: auto;
    font-family: sans-serif;
    background-size: cover;
    overflow: auto;
    background-position: center;
}

.AboutUs_Header{
    height: 40px;
    width: 100%;
    position: fixed;
    background: #fff;
    box-shadow: 0px 2px 2px #27c997;
    display: grid;
    grid-template-columns: 1fr 40px;
}
.Logo{
    color: #04928b;
    font-weight: bold;
    padding-left: 5px;
}
.Align_HederContent{
    display: flex;
    align-items: center;
}
.back{
    font-size: 16px;
    text-decoration: none;
    color: #ff5d06;
}


.AboutUs_Description_Header{
    margin-top: 50px;
    width: 100%;
    justify-self: start;
    font-size: 24px;
    font-weight: bold;
    color: #1F8DCC;
    background-color: #fff;
}

.AboutUs_Description{
    display: inline-block;
    text-align: justify;
    padding: 5px;
    font-size: 14px;
    color: #67657d;
}
.AboutUs_Description em{
    font-weight: bold;
    font-style: normal;
}


.AboutUs_Mission{
    width: 100%;
    display: block;
    margin-top: 20px;
}
.Mission_Heading{
    width: 100%;
    text-align: center;
    padding-top: 5px;
    font-weight: bold;
    font-size: 18px;
    color: #1F8DCC;
}
.Mission_Description{
    width: 100%;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
    color: #0a0071;
}



.AboutUs_Empolyee_Details_Holder{
    width: 100%;
    height: auto;
    margin-top: 10px;
    padding-bottom: 10px;
}
.AboutUs_Empolyee_Details_Holder_InnerContainer{
    width: 80%;
    margin-left: 10%;
    margin-top: 5px;
    padding-top: 20px;
}
.Employee_Image_Holder{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    box-shadow: 0px 0px 3px #749591;
    box-sizing: border-box;
    overflow: hidden;
    margin-left: 40%;
}
.Employee_Image_Holder img{
    height: 100%;
    width: 100%;
    object-fit: cover;
}
.Basic_Details_Of_Employee{
    min-height: 100px;
    box-shadow: 0px 0px 3px #749591;
    margin-top: 5px;
    border-radius: 5px;
    display: block;
    padding: 2px 5px;
    color: #000000;
    font-size: 14px;
}
.Employee_Name{
    font-size: 16px;
    font-weight: bold;
    color: #02630C;
}
.Employee_Role{
    font-size: 16px;
    font-weight: bold;
}



.AboutUs_Footer{
    width: 100%;
    display: flex;
    justify-content: space-between;
    background-color: transparent;
    height: auto;
    margin-top: 10px;
    font-size: 14px;
    position: relative;
}
.AboutUs_contactUs{
    padding: 5px;
    color: #fff;
    width: 50%;
    border-right: 1px solid #fff;
    background-color: #272525ee;
    box-shadow: 0px -2px 5px #aaa;
    text-align: left;
}
.AboutUs_customer_service{
    padding: 5px;
    color: #fff;
    width: 50%;
    box-shadow: 0px -2px 5px #aaa;
    border-left: 1px solid #fff;
    background-color: #272525ee;
    text-align: right;
}
.Fotter_Heading{
    font-size: 16px;
    font-weight: bold;
}

@media only screen and (min-width: 750px){
    .AboutUs_Description{
        display: inline-block;
        text-align: justify;
        padding: 5px 10%;
        font-size: 14px;
    }
    .AboutUs_Empolyee_Details_Holder_InnerContainer{
        display: flex;
        justify-content: center;
        margin-top: 5px;
    }


    .Employee_Image_Holder{
        margin-left: 0%;
    }
    .Basic_Details_Of_Employee{
        width: 80%;
        min-height: 80px;
        margin-left: 10px;
        margin-top: 0px;
        text-align: left;
    }

    .AboutUs_Footer{
        width: 100%;
        display: flex;
        justify-content: space-between;
        height: auto;
        margin-top: 10px;
    }
    .AboutUs_contactUs{
        padding: 5px;
        color: #fff;
        width: 40%;
        margin-left: 10%;
        text-align: left;
    }
    .AboutUs_customer_service{
        padding: 5px;
        color: #fff;
        width: 40%;
        margin-right: 10%;
        text-align: right;
    }
}

</style>