<template>
  <div id="id_cars_count">
    <div id="btns-box">
      <div class="btn" @click="minus(10)">-10</div>
      <div class="btn" @click="minus(1)">-1</div>
      <div id="id_digits">{{cars}}</div>
      <div class="btn" @click="plus(1)">+1</div>
      <div class="btn" @click="plus(10)">+10</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoCarsNumber",
  props: {
    finalObject: { type: Object, default: () => ({}) },
  },
  data() {
    return{
      cars: 16,
    }
  },
  methods: {
    plus(v) {
      this.cars += v
      if(this.cars > this.MAX_CARS_COUNTER) {
        this.cars = this.MAX_CARS_COUNTER;
      }
    },
    minus(v) {
      this.cars -= v
      if(this.cars < 0) {
        this.cars = 0;
      }
    },
    getResult() {
      return this.cars;
    },
  },

}
</script>

<style scoped>
  #id_cars_count{
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: center;
  }
  #btns-box{
    display: flex;
    flex: 0 1 320px;
    justify-content: space-between;
  }
  .btn{
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 47px;
    height: 49px;
    border: solid 1px whitesmoke;
    cursor: pointer;
    user-select: none;
    transition: .3s;
    font-size: 21px;
  }
   .btn:hover{
    color: black;
    background-color: ghostwhite;
  }
   .btn:active{
    color: white;
    background-color: gray;
  }

  #id_digits{
    width: 90px;
    text-align: center;
    font-weight: 800;
    font-size: 42px;
  }
</style>