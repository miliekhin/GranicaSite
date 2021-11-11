<template>
  <div id="id_final_body">
    <div class="item">Машин: <span>{{ info_data.cars }}</span></div>
    <div class="item">КПП: <span>{{ static_data.kpp_names[info_data.kpp] }}</span></div>
    <div class="item">Направление: <span>{{ static_data.way[info_data.way] }}</span></div>
    <div class="item">Тип: <span>{{ static_data.car_type[info_data.car_type] }}</span></div>
    <div class="item">Комментарий: <span>{{ info_data.comment ? 'Добавлен' : 'Отсутствует' }}</span></div>
  </div>
</template>

<script>
export default {
  name: "InfoFinal",
  props: ['info_data', 'static_data', ],

}
</script>

<style scoped>
  #id_final_body{
    font-size: .85em;
    margin-left: 13px;
  }
  .item{
    margin-bottom: 8px;
  }
  span{
    font-weight: 600;
    margin-left: 5px;
  }
</style>