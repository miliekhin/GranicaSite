<template>
  <div id="id_list" ref="comms_list" :class="!comments.length ? 'list_loading' : ''">
    <spinner is_grey="true" v-if="!comments.length"/>
    <div v-else class="comment" v-for="(c, i) in comments" :ref="'c'+i" :key="current_day + i">
      <div class="comm_header">{{c.header}}</div>
      <div class="comm_txt">{{c.comment}}</div>
      <div class="comm_time">{{time(c.added)}}</div>
    </div>
  </div>
</template>

<script>
import Spinner from "./Info/Spinner.vue"
import {util} from "../../tools.js"
export default {
  name: "Comments",
  components: {Spinner},
  props: ['current_day'],
  data(){
    return{
      comments:[
        // {
        //   comment: 'Давно выяснено, что читаемый текст мешает сосредоточиться.',
        //   added: '2021-05-26 23:48:52.393497',
        // },
      ],
      is_bottom: true,
      comment_index: 0,
      comments_timer: 0,
      fetch_timer: 0,
    }
  },
  methods:{
    runFetchLoop(){
      // if(this.DEBUG_MODE)
      //   return true

      this.fetch_timer = setInterval(this.getComments, this.GET_COMMENTS_PERIOD)
    },
    time(in_time_str){
      let options = { year: '2-digit', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };
      let added = new Date(in_time_str)
      let days_diff = util.dateDiffInDays( added, new Date() )
      let date_str = added.toLocaleString('ru-RU', options)
      let date = date_str.substr(0, 8)
      let time = date_str.substr(-5)
      date_str.replace(',', '')
      let ret_str = ''
      if(!days_diff)
        ret_str = time
      if(days_diff === 1)
        ret_str = 'Вчера' + ' ' + time
      if(days_diff > 1)
        ret_str = date + ' ' + time

      return ret_str
    },
    async getComments(){
      let uri = 'comments/'
      if( this.comments.length )
        uri += '?after_date=' + this.comments[this.comments.length-1].added
      try {
        let response = await fetch(this.URL + uri) // завершается с заголовками ответа
        let result = await response.json() // читать тело ответа в формате JSON
        if (Array.isArray(result) && result.length) {
          result = result.reverse()
          this.comments.push(...result)
          // console.log(result)
        }
        if( !this.fetch_timer )
          this.runFetchLoop()
      } catch (err) {
        console.log('Comments fetch error: ', err)
        clearInterval(this.fetch_timer)
        this.fetch_timer = 0
        setTimeout(this.getComments, 4321)
      }

    },

  },
  beforeUnmount() {
    clearInterval(this.fetch_timer)
  },
  mounted() {
    clearInterval(this.fetch_timer)
    // this.getFish()
    // this.comments_timer = setInterval(this.getFish, 2000)
    setTimeout(this.getComments, 1234)
    // this.comments_timer = setInterval(this.getComments, 2000)
  },
  updated() {
    // console.log(Math.round(this.$refs.comms_list.scrollTop))
    // console.log(this.$refs.comms_list.scrollHeight)
    // console.log(this.$refs.comms_list.offsetHeight)

    if( this.is_bottom ){
      let el = this.$refs['c' + (this.comments.length - 1).toString()]
      this.$refs.comms_list.scrollTo({top: el.offsetTop, behavior: 'smooth'})
    }
  }
}
</script>

<style scoped>
  #id_list{
    height: 560px;
    flex: 0 1 720px;
    /*max-width: 720px;*/
    overflow-y : auto;
    /*flex-wrap: wrap;*/
    background-color: ghostwhite;
    padding: 0 10px;
    padding-bottom: 20px;
    /*border: 1px solid darkgrey;*/
  }
  .list_loading{
    display: flex;
    justify-content: space-around;
    flex-direction: column;
  }
  .comment{
    margin-top: 15px;
    border: 1px solid #d8d8d8;
    border-radius: 10px;
    padding: 9px 13px;
    background: #eeedff;
  }
  .comm_time{
    text-align: right;
    font-size: .8em;
    margin-top: 3px;
    color: #5f5f5f;
  }
  .comm_header{
    font-size: .8em;
    margin-bottom: 10px;
    color: #5f5f5f;
  }
</style>