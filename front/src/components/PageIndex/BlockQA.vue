<template>
  <div class="block_big" id="id_big_about">
    <div class="block_inner" id="id_about">

      <div id="id_about_head">
        <h6>ВОПРОС-ОТВЕТ</h6>
        <div class="under_h6">Ответы на частые вопросы</div>
      </div>
      <div id="block_qa">
        <how-to-use/>
        <from-where-data/>
        <where-get-info/>
      </div>
    </div>
  </div>
</template>

<script>
  import HowToUse from "../QuestionsAnswers/HowToUse.vue"
  import FromWhereData from "../QuestionsAnswers/FromWhereData.vue"
  import WhereGetInfo from "../QuestionsAnswers/WhereGetInfo.vue"
  export default {
    name: "BlockQA",
    components: {FromWhereData, HowToUse, WhereGetInfo},
    data(){
      return{
      }
    },

  }
</script>

<style scoped>
  h6{
    font-size: 2.5em;
    margin-top: 20px;
    margin-bottom: 0;
    font-weight: 200;
    color: #ff7da1;
  }
  .under_h6{
    font-weight: 200;
    font-size: 1.2em;
    margin-top: 15px;
    margin-bottom: 15px;
    color: #eee;
  }
  #id_about{
    display: flex;
    flex-wrap: wrap;
  }
  #id_about_head{
    flex: 1;
  }
  #id_big_about{
    background-color: #002a33;
    color: white;
    padding: 50px 0;
  }
  #block_qa{
    display: flex;
    flex: 0 1 720px;
    /*justify-content: space-around;*/
    line-height: 1.5em;
    flex-wrap: wrap;
  }
  a {
    background: linear-gradient(to bottom, #ff9800 0%, #ff9800 100%) repeat-x 0 100%;
    background-size: 3px 3px;
    color: white;
    text-decoration: none;
    font-size: 1.2em;
    align-self: center;
  }

  a:hover {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg id='squiggle-link' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:ev='http://www.w3.org/2001/xml-events' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift .3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-20px);}}%3C/style%3E%3Cpath fill='none' stroke='%23ff9800' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
    background-position: 0 100%;
    background-size: auto 6px;
    background-repeat: repeat-x;
    text-decoration: none;
  }

  @media only screen and (max-width: 420px) {
    #id_about_head {
      text-align: center;
      padding: 0 20px;
    }
  }
</style>