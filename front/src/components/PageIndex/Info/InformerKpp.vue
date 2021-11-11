<template>
  <div class="block_data_kpp">
    <h5>{{kpp_name.toUpperCase()}}</h5>
    <div v-if="is_inited">
      <informer-line :line_info="kpp_to_rf" :car_type="car_type"/>
      <informer-line :line_info="kpp_to_ldnr" :car_type="car_type"/>
<!--      <informer-line :line_info="kpp_info.to_rf" :way="'to_rf'" :car_type="car_type"/>-->
<!--      <informer-line :line_info="kpp_info.to_ldnr" :way="'to_ldnr'" :car_type="car_type"/>-->
    </div>
    <spinner v-else/>
  </div>
</template>

<script>
import InformerLine from "./InformerLine.vue"
import Spinner from "./Spinner.vue"
export default {
  name: "InformerKpp",
  components:{InformerLine, Spinner},
  // props: ['kpp_info', 'car_type', 'is_inited'],
  props: ['kpps', 'kpp_name', 'car_type', 'is_inited'],
  data(){
    return{
    }
  },
  // mounted() {
  //   console.log(this.car_type)
  //   console.log(this.carInfo())
  // },
  computed: {
    kpp_to_rf(){
      // let r = this.kpps.find(kpp => kpp.name.toUpperCase() === this.kpp_name.toUpperCase() && kpp.from_ldnr)
      // console.log(r)
      // return r
      return this.kpps.find(kpp => kpp.name.toUpperCase() === this.kpp_name.toUpperCase() && kpp.from_ldnr)
    },
    kpp_to_ldnr(){
      return this.kpps.find(kpp => kpp.name.toUpperCase() === this.kpp_name.toUpperCase() && !kpp.from_ldnr)
    },
  },

}
</script>

<style scoped>
  h5{
    margin: 0 !important;
    font-size: 1.8em !important;
    font-weight: 500;
  }
  .block_data_kpp{
    /*padding: 15px 5px 15px 15px;*/
    padding: 15px;
    border: #404040 solid 1px;
    /*width: 320px;*/
    /*max-width: 420px;*/
    flex: 0 1 380px;
    box-sizing: border-box;
    background-color: rgba(31, 56, 69, .5);
    /*background-color: rgba(31, 56, 69, .32);*/
    /*backdrop-filter: blur(8px);*/
    /*margin-bottom: 20px;*/
  }
  @media only screen and (max-width: 1024px) {
    .block_data_kpp{
      margin-bottom: 20px;
    }
}
</style>