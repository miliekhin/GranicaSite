<template>
  <question-answer>
    <template v-slot:head>
      Как пользоваться?
    </template>
    <template v-slot:content>
      <img alt="Изображение" src="./assets/help_info.png" draggable="false">
      <p><span class="hint-num">1</span> Вверху слева отображается время получения последних данных о количестве автомобилей в очереди.
        То есть, в 06:57 было получено значение 19.</p>
      <p><span class="hint-num">2</span> Справа отображается последнее полученное значение количества автомобилей перед шлагбаумом - 19.</p>
      <p><span class="hint-num">3</span> Столбцы показывают количество автомобилей перед шлагбаумом в разное время.
        Чтобы увидеть время получения данных, нажмите на столбец.
        Данные полученные сегодня отображаются под желтыми столбцами. Вчера - под зелеными.
        Позавчера и старше - под синими.
      </p>
      <p>
        Все данные на странице обновляются автоматически.
      </p>
    </template>
  </question-answer>
</template>

<script>
  import QuestionAnswer from "./QuestionAnswer.vue"
  export default {
    name: "HowToUse",
    components: {QuestionAnswer}
  }
</script>

<style scoped>
  img{
    display: block;
    margin: 10px auto;
  }
  .hint-num{
    float: left;
    line-height: 27px;
    margin-right: 10px;
    text-align: center;
    display: inline-block;
    border: 6px solid #fe00fe;
    color: #fe00fe;
    font-weight: bold;
    height: 27px;
    width: 27px;
    border-radius: 50%;
  }
</style>