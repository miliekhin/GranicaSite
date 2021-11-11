<template>
<div class="stolbs-line">
  <div v-for="(stolb, i) in grafik_info" :key="stolb+i"
       class="stolb-wrp"
       @mouseover="show_tip($event, i)"
       @mouseleave="hide_tip"
       :ref="'stolbec'+i"
  >
    <div class="stolb-val-wrp" :class="date_color(i, true)">
      <div class="stolb-val" :class="date_color(i)" :style="stolb_height(i)"/>
    </div>
    <div class="stolb-num">
      {{grafik_info[i].cars_num}}
    </div>
  </div>
</div>
</template>

<script>
import {util} from "../../../tools.js"
export default {
  name: "InformerGrafik",
  props: ['grafik_info', ],
  data(){
    return{
    }
  },
  methods: {
    stolb_height(i) {
      let max = Math.max(...this.grafik_info.map(v=>v.cars_num))
      let k = 42 / max
      let v = k * this.grafik_info[i].cars_num
      return `height: ${v}px`
    },
    hide_tip(event){
      this.emitter.emit('hide_pop')
    },
    show_tip(event, i){
      let el = this.$refs['stolbec'+i]
      // let el = event.target
      // if( event.target.className === 'stolb-val' || event.target.className === 'stolb-num' )
      //   el = event.target.parentNode

      let l = el.getBoundingClientRect().left + window.scrollX
      let t = el.getBoundingClientRect().top + window.scrollY
      this.emitter.emit('show_pop', {t, l, dt: this.grafik_info[i].added} )
    },
    date_color(i, wrp=false){
      let days = util.dateDiffInDays( new Date(this.grafik_info[i].added), new Date())
      let class_name = undefined
      switch (days) {
        case 0:
          class_name = 'day-color-today'
          break
        case 1:
          class_name = 'day-color-yesterday'
          break
        default:
          class_name = 'day-color-old'
          break
      }
      if (wrp) class_name += '-wrp'
      return class_name
    }

  },
  created() {
  },

}
</script>

<style>
  .stolbs-line{
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
  }
  .stolb-wrp{
    width: 30px;
  }
  .stolb-val{
    width: 100%;
  }
  .day-color-today{
    background: rgba(255, 251, 0, 0.9);
  }
  .day-color-yesterday{
    background: rgba(129, 176, 78, 0.79);
  }
  .day-color-old{
    background: rgba(106, 180, 237, 0.38);
  }
  .day-color-today-wrp{
    background: rgba(255, 251, 0, 0.1);
  }
  .day-color-yesterday-wrp{
    background: rgba(129, 176, 78, 0.1);
  }
  .day-color-old-wrp{
    background: rgba(106, 180, 237, 0.1);
  }
  .stolb-val-wrp:hover{
    border: 1px solid #aaa;
  }
  .stolb-val-wrp{
    display: flex;
    align-items: flex-end;
    height: 42px;
    border: 1px solid transparent;
    transition: .2s;
  }
  .stolb-num{
    font-weight: 200;
    font-size: .8em;
    width: 100%;
    text-align: center;
  }
</style>