<template>
  <question-answer>
    <template v-slot:head>
      Откуда берутся данные?
    </template>
    <template v-slot:content>
      <p>Все данные берутся из открытых источников, а также могут быть добавлены самими посетителями сайта.</p>
      <p>
        Абсолютная достоверность данных не гарантируется.
      </p>

    </template>
  </question-answer>
</template>

<script>
  import QuestionAnswer from "./QuestionAnswer.vue"
  export default {
    name: "FromWhereData",
    components: {QuestionAnswer}
  }
</script>

<style scoped>
  table td{
    padding: 0 10px;
  }
  .phone{
    font-weight: 400;
  }
  p:not(:first-child){
    margin-top: 36px;
  }
</style>