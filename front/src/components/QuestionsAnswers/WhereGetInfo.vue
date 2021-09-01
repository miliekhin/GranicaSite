<template>
  <question-answer>
    <template v-slot:head>
      Где получить информацию о пересечении границы?
    </template>
    <template v-slot:content>
        <p>По вопросам пересечения границы на КПП ДНР в сторону России:</p>
      <table>
        <tr><td>Успенка</td><td><span class="phone">071 301-74-05</span></td></tr>
        <tr><td>Мариновка</td><td><span class="phone">071 310-08-10</span></td></tr>
        <tr><td>Новоазовск</td><td><span class="phone">071 310-08-11</span></td></tr>
      </table>

      <p>Для консультаций по вопросам пересечении КПП ДНР.
        Отдел оперативных дежурных департамента таможенного дела ДНР:
      </p>
      <span class="phone">062 301-54-17</span>

      <p>
        Для обращений и жалоб в случае неправомерных действий со стороны военнослужащих таможенной службы ДНР:
      </p>
      <span class="phone">071 307-67-55</span>

    </template>
  </question-answer>
</template>

<script>
  import QuestionAnswer from "./QuestionAnswer.vue"
  export default {
    name: "WhereGetInfo",
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