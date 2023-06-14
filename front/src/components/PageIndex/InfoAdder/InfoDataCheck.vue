<template>
  <div id="id_final_body">
    <div v-if="!isComplaint" class="item">Машин: <span>{{ cars }}</span></div>
    <div class="item">КПП: <span>{{ kpp }}</span></div>
    <div class="item">Направление: <span>{{ way }}</span></div>
    <div v-if="!isComplaint" class="item">Тип: <span>{{ type }}</span></div>
    <div
        class="item"
    >
      Комментарий:
      <span v-if="isComplaint">Жалоба</span>
      <span v-else>{{ finalObject.comment ? 'Добавлен' : 'Отсутствует' }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoDataCheck",
  props: {
    finalObject: { type: Object, default: () => ({}) },
    isComplaint: { type: Boolean, default: false },
  },
  computed: {
    cars() {
    const cars = this.finalObject.cars_num;
      if (cars > -1 && cars < this.FUZZY_CARS_COUNT_MARK) {
        return cars;
      }
      return Object.keys(this.RADIO_CARS_COUNT).find(key => this.RADIO_CARS_COUNT[key] === cars);
    },
    kpp() {
      return this.finalObject.kpp;
    },
    type() {
      return Object.keys(this.RADIO_CAR_TYPES).find(key => this.RADIO_CAR_TYPES[key] === this.finalObject.car_type);
    },
    way() {
      return Object.keys(this.RADIO_WAYS).find(key => this.RADIO_WAYS[key] === this.finalObject.way);
    },
  }
}
</script>

<style scoped>
  #id_final_body{
    display: flex;
    flex: 1;
    flex-direction: column;
    font-size: 18px;
    margin-left: 13px;
    justify-content: center;
  }
  .item{
    margin: 5px 0;
  }
  span{
    font-weight: 600;
    margin-left: 5px;
  }
</style>