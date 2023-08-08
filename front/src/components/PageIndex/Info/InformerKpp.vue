<template>
  <div class="block_data_kpp">
    <h5>{{kppName.toUpperCase()}}</h5>
    <div v-if="isInited">
      <informer-line :line_info="kpp_to_rf" :car-type="carType"/>
      <informer-line :line_info="kpp_to_ldnr" :car-type="carType"/>
    </div>
    <spinner v-else/>
  </div>
</template>

<script>
import InformerLine from "./InformerLine.vue"
import Spinner from "./Spinner.vue"
export default {
  name: "InformerKpp",
  components: {
    InformerLine,
    Spinner,
  },
  props: {
    kppName: { type: String, default: '' },
    carType: { type: String, default: '' },
    currentDay: { type: Number, default: 0 },
    kpps: { type: Array, default: () => [] },
    isInited: { type: Boolean, default: false },
  },
  data(){
    return{
    }
  },
  computed: {
    kpp_to_rf(){
      return this.kpps.find(kpp => kpp.name.toUpperCase() === this.kppName.toUpperCase() && kpp.from_ldnr)
    },
    kpp_to_ldnr(){
      return this.kpps.find(kpp => kpp.name.toUpperCase() === this.kppName.toUpperCase() && !kpp.from_ldnr)
    },
  },

}
</script>

<style scoped>
  h5{
    margin: 0 !important;
    font-size: 35px;
    font-weight: 500;
  }
  .block_data_kpp{
    /*padding: 15px 5px 15px 15px;*/
    padding: 10px 15px;
    border: #404040 solid 1px;
    flex: 0 1 585px;
    box-sizing: border-box;
    background-color: rgba(31, 56, 69, .5);
    /*background-color: rgba(31, 56, 69, .32);*/
    /*backdrop-filter: blur(8px);*/
    margin-bottom: 30px;
  }
  @media only screen and (max-width: 1190px) and (min-width: 1024px){
    .block_data_kpp{
      flex: 0 1 545px;
      margin-bottom: 15px;
    }
  }
</style>