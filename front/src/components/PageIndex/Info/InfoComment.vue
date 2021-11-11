<template>
<!--  <legend>Ваш комментарий:</legend>-->
  <textarea
      :maxlength="maxl"
      rows="6"
      v-model="info_data.comment"
      placeholder="Напишите здесь комментарий или нажмите Далее чтобы пропустить этот шаг"
  />
  <div id="id_symb_lost">Осталось символов: {{maxl - info_data.comment.length}}</div>
</template>

<script>
export default {
  name: "InfoComment",
  props: ['info_data', ],
    data(){
      return {
       maxl: 256
      }
    },

}
</script>

<style scoped>
  textarea{
    font-size: 1.1em;
    resize: none;
  }

  #id_symb_lost{
    text-align: right;
    font-size: .65em;
  }
</style>