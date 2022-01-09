<template>
  <div id="id-home-page">
    <error-panel/>
    <block-info :current_day="current_day"/>
    <block-advertising/>
    <block-comments :current_day="current_day"/>
    <block-declaration/>
    <block-telegramma/>
    <block-q-a/>
    <block-donates/>
    <block-feedback/>
    <block-footer/>
  </div>
</template>

<script>
import ErrorPanel from "./ErrorPanel.vue"
import BlockQA from "./PageIndex/BlockQA.vue"
import BlockComments from "./PageIndex/BlockComments.vue"
import BlockTelegramma from "./PageIndex/BlockTelegramma.vue"
import BlockDonates from "./PageIndex/BlockDonates.vue"
import BlockFeedback from "./PageIndex/BlockFeedback.vue"
import BlockFooter from "./PageIndex/BlockFooter.vue"
import BlockAdvertising from "./PageIndex/BlockAdvertising.vue";
import BlockDeclaration from "./PageIndex/BlockDeclaration.vue";
import BlockInfo from "./PageIndex/Info/BlockInfo.vue";
export default {
  components:{
    BlockInfo, BlockDeclaration, BlockAdvertising,
    BlockQA, BlockFooter, BlockFeedback, BlockDonates, BlockTelegramma, BlockComments,
    ErrorPanel
  },
  data(){
    return{
      next_day_timer: 0,
      current_day: 0, // для перерисовки дат после наступления нового дня
      isModalOpened: false,
      bodyWidth: 0,
    }
  },
  beforeUnmount() {
    clearInterval(this.next_day_timer)
  },
  mounted() {
    this.setNextDayTimer();
    this.emitter.on('modalOpenClose', e => {
      this.isModalOpened = !this.isModalOpened;
      if(this.isModalOpened){
        this.bodyWidth = document.body.clientWidth;
        document.body.style.overflow = 'hidden';
        document.body.style.width = this.bodyWidth + 'px';
      }else{
        document.body.style.overflow = 'auto';
        document.body.style.width = 'auto';
      }
    });
  },
  methods:{
    setNextDayTimer(){
      let actualTime = new Date(Date.now())
      let endOfDay = new Date(actualTime.getFullYear(), actualTime.getMonth(), actualTime.getDate() + 1, 0, 0, 0)
      let timeRemaining = endOfDay.getTime() - actualTime.getTime()
      this.next_day_timer = setTimeout(this.updateDates, timeRemaining)
    },
    updateDates(){
      // console.log('New day: ', new Date(Date.now()))
      this.current_day = new Date().getDate()
      // this.current_day = Math.floor(Math.random() * 12)
      clearInterval(this.next_day_timer)
      this.setNextDayTimer()
    },
  },

}
</script>

<style>
#app {}
#id-home-page {
  font-family: Montserrat, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
body{
  margin: 0;
    /*overflow: hidden;*/
}

.block_big{
  display: flex;
  justify-content: center;
}
.block_inner{
  flex: 0 1 1200px;
  height: 100%;
  /*border: 1px solid white;*/
}

@media only screen and (max-width: 1024px) and (min-width: 420px){
  .block_inner{
    padding: 0 20px;
  }
}

</style>
