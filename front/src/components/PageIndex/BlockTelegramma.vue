<template>
  <div class="block_big" id="id_big_teleg">
    <div class="block_inner" id="id_teleg">

      <div id="id_teleg_head">
        <h6>TELEGRAM</h6>
        <div class="under_h6">Заходите в нашу группу Telegram, делитесь новостями с границы, и задавайте вопросы</div>
      </div>
      <div id="block_teleg_logo">
        <div id="img_wrp" @click="openTelegram">
          <img alt="Telegram канал" src="./assets/telegrama.png" width="240" height="240" draggable="false">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlockTelegramma",
  methods:{
    openTelegram(){
      window.open('https://t.me/kppshka', '_blank')
    }
  }
}
</script>

<style scoped>
h6{
  font-size: 2.5em;
  margin-top: 20px;
  margin-bottom: 0;
  font-weight: 200;
  color: #34afe3;
}
.under_h6{
  font-weight: 200;
  font-size: 1.2em;
  margin-top: 15px;
  margin-bottom: 15px;
}
#id_teleg{
  display: flex;
  flex-wrap: wrap;
}
#id_teleg_head{
  flex: 1;
}
#id_big_teleg{
  background-color: #e5f6ff;
  /*background-color: papayawhip;*/
  padding: 50px 0;
}
#img_wrp{
  border: 1px solid grey;
  border-radius: 120px;
  cursor: pointer;
  transition: .3s;
  width: 240px;
  height: 240px;
  /*-webkit-touch-callout: none; !* iOS Safari *!*/
  /*-webkit-user-select: none; !* Safari *!*/
  /*-moz-user-select: none; !* Firefox *!*/
  /*-ms-user-select: none; !* Internet Explorer/Edge *!*/
  /*user-select: none;*/
}
#img_wrp:hover{
  cursor: pointer;
  /*margin-top: -10px;*/
  -webkit-box-shadow: 0px 0px 8px 5px rgba(0,0,0,0.25);
  box-shadow: 0px 0px 8px 5px rgba(0,0,0,0.25);
  border: 3px white solid;
}
#block_teleg_logo{
  padding: 40px 0;
  display: flex;
  justify-content: space-around;
  flex: 0 1 720px;
  height: 240px;
}
@media only screen and (max-width: 420px) {
  #id_teleg_head {
    text-align: center;
    padding: 0 20px;
  }
  /*#img_wrp{*/
      /*pointer-events: none;*/
      /*user-select: none;*/
  /*}*/

  /*#img_wrp:active{*/
  /*  -webkit-box-shadow: 0px 0px 8px 5px rgba(0,0,0,0.25);*/
  /*  box-shadow: 0px 0px 8px 5px rgba(0,0,0,0.25);*/
  /*  border: 3px white solid;*/
  /*}*/
}

</style>