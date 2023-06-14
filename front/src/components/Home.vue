<template>
  <div id="id-home-page">
    <error-panel/>
    <block-info :current-day="currentDay" :kppss="kppss" :is-inited="isInited" />
    <block-advertising/>
    <block-info-adder :kpps="kppss" :is-inited="isInited"/>
    <block-comments :current-day="currentDay"/>
    <block-telegramma/>
    <block-q-a/>
    <block-donates/>
    <block-feedback/>
    <block-footer/>
  </div>
</template>

<script>
import ErrorPanel from "./ErrorPanel.vue"
import BlockQA from "./PageIndex/BlockQA.vue"
import BlockComments from "./PageIndex/BlockComments.vue"
import BlockTelegramma from "./PageIndex/BlockTelegramma.vue"
import BlockDonates from "./PageIndex/BlockDonates.vue"
import BlockFeedback from "./PageIndex/BlockFeedback.vue"
import BlockFooter from "./PageIndex/BlockFooter.vue"
import BlockAdvertising from "./PageIndex/BlockAdvertising.vue";
import BlockInfo from "./PageIndex/Info/BlockInfo.vue";
import BlockInfoAdder from "./PageIndex/InfoAdder/BlockInfoAdder.vue";
export default {
  components:{
    BlockInfoAdder,
    BlockInfo,
    BlockAdvertising,
    BlockQA,
    BlockFooter,
    BlockFeedback,
    BlockDonates,
    BlockTelegramma,
    BlockComments,
    ErrorPanel,
  },
  data(){
    return{
      nextDayTimer: 0,
      currentDay: 0, // для перерисовки дат после наступления нового дня
      isModalOpened: false,
      bodyWidth: 0,
      fetchTimer: 0,
      kppss: [],
      isInited: false,
    }
  },
  beforeUnmount() {
    clearInterval(this.nextDayTimer);
    clearInterval(this.fetchTimer);
  },
  mounted() {
    this.setNextDayTimer();
    this.emitter.on('modalOpenClose', e => {
      this.isModalOpened = !this.isModalOpened;
      if(this.isModalOpened){
        this.bodyWidth = document.body.clientWidth;
        document.body.style.overflow = 'hidden';
        document.body.style.width = this.bodyWidth + 'px';
      }else{
        document.body.style.overflow = 'auto';
        document.body.style.width = 'auto';
      }
    });
    
    clearInterval(this.fetchTimer);
    this.fetchData();
    this.fetchTimer = setInterval(this.fetchData, this.GET_INFO_PERIOD);
  },
  methods:{
    setNextDayTimer() {
      let actualTime = new Date(Date.now())
      let endOfDay = new Date(actualTime.getFullYear(), actualTime.getMonth(), actualTime.getDate() + 1, 0, 0, 0)
      let timeRemaining = endOfDay.getTime() - actualTime.getTime()
      this.nextDayTimer = setTimeout(this.updateDates, timeRemaining)
    },
    updateDates() {
      // console.log('New day: ', new Date(Date.now()))
      this.currentDay = new Date().getDate();
      clearInterval(this.nextDayTimer);
      this.setNextDayTimer();
    },
    runFetchLoop() {
      this.fetchTimer = setInterval(this.fetchData, this.GET_INFO_PERIOD);
      // console.log(this.fetchTimer)
    },
    async fetchData() {
      try {
        let response = await fetch(this.URL + 'kpp/'); // завершается с заголовками ответа
        let result = await response.json(); // читать тело ответа в формате JSON
        // console.log( result )
        this.init(result); // разкомитить
        // this.isInited = true // удалить
        if( !this.fetchTimer ) {
          this.runFetchLoop();
        }

      } catch (err) {
        // console.error('fetchData error:', err);
        clearInterval(this.fetchTimer);
        // console.log(this.fetchTimer)
        this.fetchTimer = 0;
        if(this.DEBUG_MODE) {
          return;
        }
        setTimeout(this.fetchData, 4321);
      }
    },
    init(result) {
      this.kppss.forEach((local_kpp) => {
        let res_kpp = result.find(rkpp => {
          return rkpp.name.toUpperCase() === local_kpp.name.toUpperCase() && rkpp.from_ldnr === local_kpp.from_ldnr
        })
        // console.log(res_kpp)

        if( res_kpp ) {
          local_kpp.id = res_kpp.id;
          // console.log('local_kpp', local_kpp)

          let dataCars = res_kpp.data_cars;
          if( dataCars ){
            dataCars.reverse()
            dataCars.forEach((res_grafik, j) => {
              if( res_grafik ){
                  local_kpp.info[0][j].car_type = res_grafik.car_type;
                  local_kpp.info[0][j].cars_num = res_grafik.cars_num;
                  local_kpp.info[0][j].added = res_grafik.added;
                }
              })
          }

          let dataTrucks = res_kpp.data_trucks;
          if( dataTrucks ) {
            dataTrucks.reverse()
              dataTrucks.forEach((res_grafik, j) => {
                if( res_grafik ){
                  local_kpp.info[1][j].car_type = res_grafik.car_type;
                  local_kpp.info[1][j].cars_num = res_grafik.cars_num;
                  local_kpp.info[1][j].added = res_grafik.added;
                }
              })
          }

        }
      })
      this.isInited = true
    },    
  },

}
</script>

<style>
  #app {}
  #id-home-page {
    font-family: Montserrat, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  body{
    margin: 0;
      /*overflow: hidden;*/
  }

  .block_big{
    display: flex;
    justify-content: center;
  }
  .block_inner{
    flex: 0 1 1200px;
    height: 100%;
    /*border: 1px solid white;*/
  }

  @media only screen and (max-width: 1024px) and (min-width: 420px){
    .block_inner{
      padding: 0 20px;
    }
  }

</style>
