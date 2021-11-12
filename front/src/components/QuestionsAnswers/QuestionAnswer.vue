<template>
  <div class="qa-block">
    <div class="qa-question" @click="is_opened = !is_opened">
      <div class="q-txt">
        <slot name="head"></slot>
      </div>
      <div class="q-arrow">
        <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="iconData" />
        </svg>
      </div>
    </div>
    <transition name="slidedown">
      <div class="qa-answer" v-show="is_opened">
        <slot name="content"></slot>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "QuestionAnswer",
  data(){
    return{
      is_opened: false
    }
  },
  computed:{
    iconData(){
      return !this.is_opened ? 'M19 13l-7 7-7-7m14-8l-7 7-7-7' : 'M5 11l7-7 7 7M5 19l7-7 7 7'
    }
  },

}
</script>

<style scoped>
  .qa-block{
    width: 100%;
    margin-top: 20px;
  }
  /*.qa-question:hover{*/
  /*  color: black;*/
  /*  background-color: ghostwhite;*/
  /*}*/
  /*.qa-question:active{*/
  /*  color: white;*/
  /*  background-color: gray;*/
  /*}*/
  .qa-question{
    display: flex;
    border: 1px solid white;
    padding: 15px;
    align-items: center;
    cursor: pointer;
    transition: .2s;
  }
  .q-txt{
    flex: 1;
    padding-right: 15px;
  }
  .q-arrow{
    padding: 0 7px;
    /*border: 1px solid #ddd;*/
  }
  .qa-answer{
    padding: 10px;
    font-weight: 300;
  }
  .slidedown-enter-active,
  .slidedown-leave-active {
    transition: max-height .3s linear;
  }

  .slidedown-enter-to,
  .slidedown-leave-from {
    overflow: hidden;
    max-height: 400px;
  }

  .slidedown-enter-from,
  .slidedown-leave-to {
    overflow: hidden;
    max-height: 0;
  }
</style>