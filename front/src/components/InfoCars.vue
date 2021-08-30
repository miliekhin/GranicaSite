<template>
<!--  <legend>Укажите количество машин:</legend>-->
  <div id="id_cars_count">
    <div class="btn" @click="minus(10)">-10</div>
    <div class="btn" @click="minus(1)">-1</div>
    <div id="id_digits">{{info_data.cars}}</div>
    <div class="btn" @click="plus(1)">+1</div>
    <div class="btn" @click="plus(10)">+10</div>
  </div>
</template>

<script>
export default {
  name: "InfoCars",
  props: ['info_data', ],
  data(){
    return{
      cars: 16,
    }
  },
  methods:{
    plus(v){
      this.info_data.cars +=v
      if(this.info_data.cars > this.MAX_CARS) this.info_data.cars = this.MAX_CARS
    },
    minus(v){
      this.info_data.cars -=v
      if(this.info_data.cars<0) this.info_data.cars = 0
    },
  },

}
</script>

<style scoped>
  /*legend{*/
  /*  margin: 10px 0;*/
  /*}*/
  #id_cars_count{
    display: flex;
    justify-content: space-between;
  }
  .btn{
    padding: 10px 0;
    width: 47px;
    height: 27px;
    border: solid 1px white;
    text-align: center;
    cursor: pointer;
    user-select: none;
    transition: .3s;
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
    /*padding: 10px 0;*/
    width: 90px;
    /*margin: 0 10px;*/
    /*line-height: 0;*/
    text-align: center;
    font-weight: 800;
    font-size: 2em;
  }
</style>