<template>
  <div class="block_big" id="id_head">
    <div class="block_inner">
      <div id="block_head">
        <div id="block_slogan">
          <div id="slogan">КППшка</div>
          <img src="../../../assets/kpp3.png" width="170" alt="logo" id="id_kpp_logo_big">
          <h1 id="slogan_text"><span>Очередь на границе</span> <span>ДНР - РФ</span></h1>
          <h2>Узнавайте и добавляйте информацию о количестве автомобилей в очередях</h2>
        </div>

        <div id="car_selector">
          <div id="id_buttons_block">
            <div class="item">
              <input type="radio" id="id_cars" name="type" value="cars" checked v-model="carType">
              <label for="id_cars">ЛЕГКОВЫЕ</label>
            </div>
            <div class="item">
              <input type="radio" id="id_trucks" name="type" value="trucks" v-model="carType">
              <label for="id_trucks">ГРУЗОВЫЕ</label>
            </div>
          </div>
          <div id="car_image_wrp">
            <transition name="slide-fade" mode="out-in">
              <img class="img_avto" width="175" src="../../../assets/car.png" alt="легковые" v-if="carType === 'cars'">
              <img class="img_avto" src="../../../assets/truck1.png" alt="грузовые" v-else>
            </transition>
          </div>
        </div>

        <informer-wrapper
          :car-type="carType"
          :is-inited="isInited"
          :kpps="kppss"
          :current-day="currentDay"
        />
      </div>
      <div class="id_tip"><span class="icon-asterisk"></span> Внимание! Точность данных не гарантируется</div>
      <div class="id_tip"><span class="icon-asterisk"></span> Информация на графиках обновляется автоматически</div>
    </div>
  </div>
  <pop-tip/>
</template>

<script>
import PopTip from "./PopTip.vue";
import InfoAdder from "../InfoAdder/InfoAdder.vue";
import KpButton from "./KpButton.vue";
import InformerWrapper from "./InformerWrapper.vue";

export default {
  name: "BlockInfo",
  props: {
    currentDay: { type: Number, default: 0 },
    kppss: { type: Array, default: () => [] },
    isInited: { type: Boolean, default: false },
  },
  components: {
    InformerWrapper,
    InfoAdder,
    KpButton,
    PopTip,
  },
  data() {
    return{
      carType: 'cars',
      columnsInGrafik: 12,
    };
  },
  created() {
    this.zeroKpps();
  },
  methods: {
    zeroKpps(){
      let kpp_id = 0
      let kpp_name_id = 0
      let kpp_obj = {}

      function fake_info(car_type, columns){
        let arr_stolb = []
        for (let a = 0; a < columns; a++){
          let added = new Date(new Date().setDate(new Date().getDate()-a))
          // let o = {cars_num: Math.floor(Math.random() * 101), car_type, added}
          let o = { cars_num: 0, car_type, added };
          arr_stolb.push(o);
        }
        return arr_stolb.reverse();
      }

      for (let i = 0; i < this.KPP_NAMES.length; i++)
      {
        let arr_grafiks = []
        kpp_id++
        arr_grafiks.push(fake_info(0, this.columnsInGrafik))
        arr_grafiks.push(fake_info(1, this.columnsInGrafik))
        kpp_obj = {
          id: kpp_id * 10000,
          name: this.KPP_NAMES[kpp_name_id],
          from_ldnr: true,
          info: arr_grafiks
        }
        this.kppss.push(kpp_obj)

        kpp_id++
        arr_grafiks = []
        arr_grafiks.push(fake_info(0, this.columnsInGrafik))
        arr_grafiks.push(fake_info(1, this.columnsInGrafik))
        kpp_obj = {
          id: kpp_id * 10000,
          name: this.KPP_NAMES[kpp_name_id],
          from_ldnr: false,
          info: arr_grafiks
        }
        this.kppss.push(kpp_obj)
        kpp_name_id++
      }
      // console.log(this.kppss)
    },

  },
}
</script>

<style scoped>
  .id_tip{
    font-size: .7em;
    font-weight: 300;
    margin-bottom: 10px;
    margin-left: 5px;
    color: #eee;
  }
  #id_head{
    color: white;
    font-size: 1.3em;
    /*height: 1080px;*/
    background: url('../../../assets/head_back.jpg')no-repeat center center;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }
  #id_kpp_logo_big{
    padding-bottom: 7px;
    margin-right: 11px;
    margin-left: -162px;
  }
  #block_slogan{
    display: flex;
    flex-wrap: wrap;
    /*margin-bottom: 40px;*/
    margin-top: 20px;
    align-items: flex-end;
  }
  h1{
    color: #fffc9c;
    margin: 0;
    font-size: 1em;
  }
  h2{
    margin: 4px 0 0;
    /*margin-top: 10px;*/
    font-size: .8em;
    font-weight: 400;
    /*color: #ff8a8a;*/
  }
  #slogan_text{
    font-weight: 600;
    padding-bottom: 6px;
    display: flex;
    flex-wrap: wrap;
  }
  #slogan_text span{
    margin-right: 5px;
  }
  #slogan{
    font-size: 64px;
    font-weight: 800;
    color: white;
    margin-right: 20px;
    line-height: 64px;
  }
  #car_selector{
    margin-bottom: 20px;
    display: flex;
    align-items: flex-end;
    min-height: 117px;
    flex-wrap: wrap;
  }
  #id_buttons_block{
    display: flex;
    justify-content: space-between;
    flex: 0 1 380px;
    padding: 0 5px;
  }
  .img_avto{
    filter: invert(100%);
    -webkit-filter: invert(100%);
    align-self: flex-end;
    margin-right: 10px;
    user-select: none;
    -webkit-user-drag: none;
  }
  #car_image_wrp{
    user-select: none;
    overflow: hidden;
    height: 117px;
    display: flex;
    flex-grow: 1;
    justify-content: flex-end;
  }
@media only screen and (max-width: 320px) {
  #slogan {
    margin-right: 0;
    font-size: 55px;
  }
  #id_kpp_logo_big {
    margin-left: -124px !important;
  }
  #slogan_text span:last-of-type{
    margin-left: 200px;
  }
}
@media only screen and (max-width: 420px) {
  #block_slogan{
    margin-bottom: 20px;
    margin-left: 10px;
  }
  #slogan{
    margin-right: 0;
  }
  #id_kpp_logo_big{
    margin-left: -144px;
  }

/*  #car_selector {
      justify-content: space-around;
  }*/
}


  label {
    /*margin-right: 15px;*/
    /*line-height: 32px;*/
    cursor: pointer;
    position: relative;
    bottom: 3px;
  }

  input {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;

    border-radius: 50%;
    width: 20px;
    height: 20px;

    border: 3px solid yellow;
    transition: 0.2s all linear;
    outline: none;
    margin-right: 6px;

    position: relative;
    /*top: 4px;*/
    cursor: pointer;
  }

  input:checked {
    border: 5px solid orangered;
  }
  input:checked:after {
    content: '';
    display: block;
    position: absolute;
    top: -8px;
    bottom: -8px;
    left: -8px;
    right: -8px;
    border-radius: 50%;
    border: 2px solid whitesmoke;
  }

.slide-fade-enter-active {
  transition: all .5s ease-out;
}

.slide-fade-enter-from {
  transform: translateX(100px);
  opacity: 0;
}
  @media only screen and (max-width: 1190px) {
    #block_head{
      display: flex;
      flex-wrap: wrap;
    }
    #car_selector{
      flex: 1 1 700px;
    }
    #id_buttons_block{
      flex: 0 0 330px;
    }
  }
  @media only screen and (max-width: 1024px) {
    #car_selector{
      flex: 0 1 670px;
      align-self: center;
    }
    #block_head{
      justify-content: space-around;
    }
  }
</style>