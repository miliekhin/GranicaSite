<template>
<!--  <transition name="slides">-->
  <div id="err_wrp" v-show="err_msg">
    <div id="err">
      <div id="err_txt">
        Ой. Возникла непредвиденная ошибка: <br><br>
        {{err_msg}}
        <br><br>
        Попробуйте обновить страницу и повторить действие снова.
      </div>
      <div id="close" @click="err_msg=''">&Cross;</div>
    </div>
  </div>
<!--  </transition>-->
</template>

<script>
export default {
  name: "ErrorPanel",
  data(){
    return{
      err: true,
      err_msg: '',
    }
  },
  mounted() {
    this.emitter.on('fetch_error', err => {
      this.err_msg = err;
    });
  },
}
</script>

<style scoped>

/*.slides-enter-active {*/
/*  transition: top 0.3s ease-out;*/
/*}*/
/*.slides-leave-active {*/
/*  transition: top 0.8s cubic-bezier(1, 0.5, 0.8, 1);*/
/*}*/
/*.slides-enter-from,*/
/*.slides-leave-to {*/
/*  top: -100%;*/
/*}*/
  #err_wrp{
    position: fixed;
    top: 20px;
    display: flex;
    justify-content: space-around;
    width: 100%;
    font-size: .9em;
    z-index: 777;
  }
  #err{
    width: 320px;
    background-color: #ff8f65;
    padding: 15px;
    box-sizing: border-box;
    display: flex;
    align-items: start;
    -webkit-box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
    box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
  }
  #err_txt{
    padding-right: 15px;
  }
  #close{
    border: 2px black solid;
    text-align: center;
    padding: 14px 6px 17px 7px;
    line-height: 0;
    cursor: pointer;
    font-size: 2em;
    transition: .2s;
    background-color: orangered;
    user-select: none;
  }
  #close:hover{
    background: antiquewhite;
  }

</style>