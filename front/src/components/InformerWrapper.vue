<template>
      <div id="block_data_wrapper">
<!--        <informer-kpp v-for="k in kpps" :kpp_info="k" :car_type="car_type" :is_inited="is_inited"/>-->
        <informer-kpp v-for="(name, i) in KPP_NAMES"
                      :kpp_name="name"
                      :kpps="kpps"
                      :car_type="car_type"
                      :is_inited="is_inited"
                      :key="current_day + i"
        />
      </div>
</template>

<script>
import InformerKpp from "./InformerKpp.vue"
export default {
  components:{InformerKpp, },
  name: "InformerWrapper",
  props: ['car_type', 'is_inited', 'kpps', 'current_day'],
  data(){
    return{

    }
  },
}
</script>

<style scoped>
  #block_data_wrapper{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  @media only screen and (max-width: 1024px) {
    #block_data_wrapper {
      justify-content: space-around;
    }
  }
</style>