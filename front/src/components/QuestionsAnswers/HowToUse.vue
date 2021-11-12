<template>
  <question-answer>
    <template v-slot:head>
      Как пользоваться?
    </template>
    <template v-slot:content>
      <img alt="Изображение" src="./assets/help_info.png" draggable="false">
      <p>1. Вверху слева отображается время получения последних данных о количестве автомобилей в очереди.
        То есть, в 06:57 было получено значение 19.</p>
      <p>2. Справа отображается последнее полученное значение количества автомобилей перед шлагбаумом - 19.</p>
      <p>3. Столбцы показывают количество автомобилей перед шлагбаумом в разное время.
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
</style>