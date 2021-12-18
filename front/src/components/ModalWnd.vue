<template>
  <div id="id_modal_wrapper">
    <form>
      <header>
        <div id="id_htext">{{modalData.headText}}</div>
        <div class="icon-cancel-squared" id="id_close" title="Закрыть" @click="$emit('closeModal')"></div>
      </header>
      <hr>
      <div id="id_form_body">
        <slot name="modalBody">Body of modal wnd</slot>
      </div>
      <footer>
        <kp-button class="bttn" :text="modalData.cancelBttnText" @click.prevent="$emit('closeModal', 'eventCloseModal')"/>
        <kp-button class="bttn" :text="modalData.okBttnText" @click.prevent="submit"/>
      </footer>
    </form>
  </div>
</template>

<script>
import KpButton from "./KpButton.vue";

export default {
  name: "ModalWnd",
  components: {KpButton, },
  props: ['modalData', ],

  mounted() {
    document.addEventListener("keydown", this.onEscape);
  },
  beforeUnmount() {
    document.removeEventListener("keydown", this.onEscape);
  },
  methods:{
    onEscape(e){
        if (e.key === 'Escape') {
            this.$emit('closeModal', 'eventCloseModal');
        }
    },
    submit(){
      this.$emit('closeModal', this.modalData.eventName);
    },
  },

}
</script>

<style scoped>
  hr{
    width: 100%;
    border: 1px solid #00000000;
    border-bottom: 1px solid #fff3a0;
    margin-bottom: 20px;
  }
  header{
    display: flex;
    flex-shrink: 0;
    height: 60px;
    justify-content: space-between;
    align-items: center;
  }
  #id_htext{
    color: #fff3a0;
    font-weight: 300;
    /*font-size: 1em;*/
  }
  #id_close:hover{
    color: red;
  }
  #id_close{
    padding: 0 0 0 25px;
    margin-top: -21px;
    margin-right: -3px;
    font-size: 1.5em;
    color: indianred;
    cursor: pointer;
  }
  #id_modal_wrapper{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.7); /* Black w/ opacity */
    overflow: auto;
    z-index: 776;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  form{
    margin: 20px 0;
    max-height: 90%;
    display: flex;
    flex-direction: column;
    flex: 0 1 540px;
    background: #00435c;
    color: white;
    padding: 10px 20px 25px;
    box-sizing: border-box;
    overflow: hidden;
    /*animation-name: animatetop;*/
    /*animation-duration: 0.4s*/
  }
  footer{
    margin-top: 25px;
    text-align: right;
  }
  .bttn{
    margin-left: 15px;
  }
  #id_form_body{
    position: relative;
    max-height: 100%;
    overflow: auto;
  }
  /*@keyframes animatetop {*/
  /*  from {transform: scale(.5); opacity: 0}*/
  /*  to {transform: scale(1); opacity: 1}*/
  /*}*/
::-webkit-scrollbar {
    width: 30px;
}

/*::-webkit-scrollbar-track {*/
/*    !*box-shadow: inset 0 0 10px 10px green;*!*/
/*    border-left: solid 10px transparent;*/
/*}*/

::-webkit-scrollbar-thumb {
  border-left: 20px solid transparent;
  background-clip: padding-box;
  /*border-radius: 9999px;*/
  background-color: #AAAAAA;
}
</style>