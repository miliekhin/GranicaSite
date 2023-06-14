<template>
  <div id="block_data_wrapper">
    <informer-kpp
        v-for="(name, i) in KPP_NAMES"
        :kpp-name="name"
        :kpps="kpps"
        :car-type="carType"
        :is-inited="isInited"
        :key="currentDay + i"
    />
  </div>
</template>

<script>
import InformerKpp from "./InformerKpp.vue"
import InfoAdder from "../InfoAdder/InfoAdder.vue";

export default {
  components: {
    InformerKpp,
    InfoAdder,
  },
  name: "InformerWrapper",
  props: {
    carType: { type: String, default: '' },
    currentDay: { type: Number, default: 0 },
    kpps: { type: Array, default: () => [] },
    isInited: { type: Boolean, default: false },
  },
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

  /*
  @media only screen and (min-width: 1024px) {
    #block_data_wrapper div:nth-child(1) {
      order: 0;
    }
    #block_data_wrapper div:nth-child(2) {
      order: 1;
    }
    #block_data_wrapper div:nth-child(3) {
      order: 3;
    }
    #block_data_wrapper div:nth-child(4) {
      order: 3;
    }
    #block_data_wrapper div:nth-child(5) {
      order: 2;
    }
    #block_data_wrapper div:nth-child(6) {
      order: 5;
    }
  }
  */

  @media only screen and (max-width: 1024px) {
    #block_data_wrapper {
      justify-content: space-around;
    }
  }
</style>