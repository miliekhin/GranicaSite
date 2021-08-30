<template>
<!--  <transition name="fade">-->
    <div v-show="show_pop" class="popover" ref="pop">{{txt}}</div>
<!--  </transition>-->
</template>

<script>
import {util} from "../tools.js"
export default {
  name: "PopTip",
  data(){
    return{
      show_pop: false,
      txt: '88.88.8888 88:88'
    }
  },
  methods:{

  },
  mounted() {
    this.emitter.on('show_pop', pos => {
      let dt = util.textDateTime(pos.dt)
      this.txt = `${dt.date} ${dt.time}`
      let popl = pos.l
      let popr = pos.l+150
      this.$refs.pop.style.top = (pos.t-60)+'px'
      let dw = document.documentElement.clientWidth
      if (popr > dw){
        // console.log(popr, popl,  dw)
        let v = popl - (popr - dw) - 5
        this.$refs.pop.style.left = v+'px'
      } else {
        this.$refs.pop.style.left = popl+'px'
      }
      this.show_pop = true
    });
    this.emitter.on('hide_pop', err => {
      this.show_pop = false;
    });
  }
}
</script>

<style scoped>
  .popover{
    border: 1px solid grey;
    background: rgba(0, 0, 0, 0.84);
    color: white;
    position: absolute;
    top: 100px;
    left: 115px;
    width: 150px;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    box-sizing: border-box;
  }
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}
</style>