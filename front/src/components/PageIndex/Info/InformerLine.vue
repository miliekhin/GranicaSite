<template>
  <div class="line">
    <div class="left-block">
      <div class="cell_actual"><span class="date-str">{{ added.date }}</span> {{added.time}}</div>
      <div class="cell_way" v-html="to"/>
    </div>
    <div class="car_count">
      {{cars_info.cars_num}}
    </div>
  </div>

  <informer-grafik :grafik_info="line_info.info[car_type_index]"/>
</template>

<script>
import InformerGrafik from "./InformerGrafik.vue"
import {util} from "../../../tools.js"
export default {
  name: "InformerLine",
  components: {InformerGrafik},
  props: {
    carType: { type: String, default: '' },
    line_info: { type: Object, default: () => ({}) }
  },
  data(){
    return{
    }
  },
  methods:{
  },
  computed:{
    to(){
      return this.line_info.from_ldnr ?
          'ДНР <span class="icon-right-bold"></span> РФ' :
          'РФ <span class="icon-right-bold"></span> ДНР';
    },
    car_type_index(){
      if (this.carType === 'cars')
        return 0
      if (this.carType === 'trucks')
        return 1
    },
    cars_info(){
      let ret = {}
      let grafik_arr_data_len
      grafik_arr_data_len = this.line_info.info[this.car_type_index].length-1
      ret = this.line_info.info[this.car_type_index][grafik_arr_data_len]
      return ret
    },
    added(){
      // console.log('INFO: ', this.cars_info.added)
      return util.textDateTime(this.cars_info.added)
    },
  },
}
</script>

<style scoped>
  .line{
    display: flex;
    margin-top: 20px;
  }
  .left-block{
    flex: 1;
  }
  .car_count{
    font-size: 2.3em;
    text-align: center;
    /*font-family: Courier, monospace;*/
    font-weight: 800;
    /*line-height: 1em;*/
    width: 99px;
  }
  .cell_way{
    font-weight: 600;
    font-size: 1.1em;
    padding-top: 10px;
  }
  .cell_actual{
    /*text-align: right;*/
    font-size: .8em;
  }
  .date-str{
    color: #ff8f65;
  }
</style>