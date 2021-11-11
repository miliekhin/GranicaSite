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
              <input type="radio" id="id_cars" name="type" value="cars" checked v-model="car_type">
              <label for="id_cars">ЛЕГКОВЫЕ</label>
            </div>
            <div class="item">
              <input type="radio" id="id_trucks" name="type" value="trucks" v-model="car_type">
              <label for="id_trucks">ГРУЗОВЫЕ</label>
            </div>
          </div>
          <div id="car_image_wrp">
            <transition name="slide-fade" mode="out-in">
              <img class="img_avto" width="175" src="../../../assets/car.png" alt="легковые" v-if="car_type === 'cars'">
              <img class="img_avto" src="../../../assets/truck1.png" alt="грузовые" v-else>
            </transition>
          </div>
        </div>

        <informer-wrapper :car_type="car_type" :is_inited="is_inited" :kpps="kppss" :current_day="current_day"/>
        <info-adder :is_inited="is_inited" :kpps="kppss"/>
      </div>
      <div class="id_tip">&#10034; Абсолютная достоверность данных не гарантируется</div>
      <div class="id_tip">&#10034; Страницу можно не обновлять - вся информация обновляется автоматически</div>
    </div>
  </div>
  <pop-tip/>
</template>

<script>
import PopTip from "./PopTip.vue";
import InfoAdder from "./InfoAdder.vue";
import KpButton from "./KpButton.vue";
import InformerWrapper from "./InformerWrapper.vue";

export default {
  name: "BlockInfo",
  props: ['current_day'],
  components:{
    InformerWrapper, InfoAdder, KpButton, PopTip,},
  data(){
    return{
      is_inited: false,
      car_type: 'cars',
      fetch_timer: 0,
      kppss:[],
    }
  },
  created() {
    this.zeroKpps()
  },
  mounted() {
    clearInterval(this.fetch_timer)
    this.fetchData()
    this.fetch_timer = setInterval(this.fetchData, this.GET_INFO_PERIOD)
  },
  beforeUnmount() {
    clearInterval(this.fetch_timer)
  },
  methods: {
    zeroKpps(){
      let kpp_id = 0
      let kpp_name_id = 0
      let kpp_obj = {}

      function fake_info(car_type){
        let arr_stolb = []
        for (let a = 0; a < 8; a++){
          let added = new Date(new Date().setDate(new Date().getDate()-a))
          // let o = {cars_num: Math.floor(Math.random() * 101), car_type, added}
          let o = {cars_num: 0, car_type, added}
          arr_stolb.push(o)
        }
        return arr_stolb.reverse()
      }

      for (let i = 0; i < this.KPP_NAMES.length; i++)
      {
        let arr_grafiks = []
        kpp_id++
        arr_grafiks.push(fake_info(0))
        arr_grafiks.push(fake_info(1))
        kpp_obj = {
          id: kpp_id * 10000,
          name: this.KPP_NAMES[kpp_name_id],
          from_ldnr: true,
          info: arr_grafiks
        }
        this.kppss.push(kpp_obj)

        kpp_id++
        arr_grafiks = []
        arr_grafiks.push(fake_info(0))
        arr_grafiks.push(fake_info(1))
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
    runFetchLoop(){
      // if(this.DEBUG_MODE)
      //   return true

      this.fetch_timer = setInterval(this.fetchData, this.GET_INFO_PERIOD)
      // console.log(this.fetch_timer)
    },
    async fetchData() {
      try {
        let response = await fetch(this.URL + 'kpp/') // завершается с заголовками ответа
        let result = await response.json() // читать тело ответа в формате JSON
        // console.log( result )
        this.init(result) // разкомитить
        // this.is_inited = true // удалить
        if( !this.fetch_timer )
          this.runFetchLoop()

      } catch (err) {
        // console.error('fetchData error:', err);
        clearInterval(this.fetch_timer)
        // console.log(this.fetch_timer)
        this.fetch_timer = 0
        setTimeout(this.fetchData, 4321)
      }
    },
    init(result) {
      this.kppss.forEach((local_kpp) => {
        let res_kpp = result.find(rkpp => {
          return rkpp.name.toUpperCase() === local_kpp.name.toUpperCase() && rkpp.from_ldnr === local_kpp.from_ldnr
        })
        // console.log(res_kpp)

        if( res_kpp ){
          local_kpp.id = res_kpp.id
          // console.log(local_kpp)
          res_kpp.info.forEach((res_grafik_arr, i )=> {
            // console.log(res_grafik_arr, i)
            // console.log(res_grafik_arr[0])
            if(res_grafik_arr){
              res_grafik_arr.reverse()
              res_grafik_arr.forEach((res_grafik, j) => {
                if( res_grafik ){
                  // console.log(res_grafik)
                  local_kpp.info[i][j].car_type = res_grafik.car_type
                  local_kpp.info[i][j].cars_num = res_grafik.cars_num
                  local_kpp.info[i][j].added = res_grafik.added
                  // local_kpp.info[i].reverse()
                }
              })
            }
          })
        }
      })
      // console.log(this.kppss)
      this.is_inited = true
    },

  }

}
</script>

<style scoped>
  .id_tip{
    font-size: .7em;
    font-weight: 300;
    margin-bottom: 10px;
    margin-left: 5px;
    color: #ccc;
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
  /*@media only screen and (max-width: 767px) {*/
  /*  #id_head{*/
  /*     background-image: url(smaller-image.jpg);*/
  /*  }*/
  /*}*/

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
  }
  .img_avto{
    filter: invert(100%);
    -webkit-filter: invert(100%);
    align-self: flex-end;
    margin-right: 10px;
  }
  #car_image_wrp{
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
}
@media only screen and (max-width: 320px) {
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

  #car_selector {
      justify-content: space-around;
  }
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

/*.slide-fade-leave-active {*/
/*  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);*/
/*}*/

.slide-fade-enter-from {
  transform: translateX(100px);
  opacity: 0;
}

</style>