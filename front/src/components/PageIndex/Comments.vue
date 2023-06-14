<template>
  <div id="id_list" ref="comms_list" :class="!comments.length ? 'list_loading' : ''">
    <spinner is_grey="true" v-if="!comments.length"/>
    <div v-else class="comment" v-for="(c, i) in commentoz" :ref="'c'+i" :key="currentDay + i">
      <div class="comm_header">
        <span
            v-if="c.isComplaint"
            class="complaint-word"
        >
          {{complaintText}}
        </span>
        {{ c.header }}
      </div>
      <div class="comm_txt">{{ c.comment }}</div>
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
  props: {
    currentDay: { type: Number, default: 0 },
  },
  data(){
    return{
      comments: [],
      is_bottom: true,
      comment_index: 0,
      comments_timer: 0,
      fetch_timer: 0,
      complaintText: 'Жалоба! ',
    }
  },
  computed: {
    commentoz() {
      return this.comments.map((cmnt) => {
        if (cmnt.header.includes(this.complaintText)) {
          cmnt.isComplaint = true;
          cmnt.header = cmnt.header.replace(this.complaintText, '');
        }
        return cmnt;
      });
    },
  },
  methods: {
    runFetchLoop(){
      if (this.DEBUG_MODE) {
        return true
      }

      this.fetch_timer = setInterval(this.fetchComments, this.GET_COMMENTS_PERIOD)
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
        ret_str = 'Сегодня ' + time
      if(days_diff === 1)
        ret_str = 'Вчера ' + time
      if(days_diff > 1)
        ret_str = date + ' ' + time

      return ret_str
    },
    async fetchComments() {
      let uri = 'comments/'
      if( this.comments.length ) {
        uri += '?after_date=' + this.comments[this.comments.length - 1].added;
      }
      try {
        let response = await fetch(this.URL + uri) // завершается с заголовками ответа
        let result = await response.json();
        if (Array.isArray(result) && result.length) {
          result = result.reverse()
          this.comments = this.comments.filter((itm) => !itm.isAddedByScript)
          this.comments.push(...result)
          // console.log(result)
        }
        if(!this.fetch_timer) {
          this.runFetchLoop();
        }
      } catch (err) {
        console.log('Comments fetch error: ', err)
        clearInterval(this.fetch_timer)
        this.fetch_timer = 0
        if (this.DEBUG_MODE) {
          return;
        }
        setTimeout(this.fetchComments, 4321)
      }

    },
    addComment(finalObj) {
      const isComplaint = finalObj.cars_num === this.COMPLAINT_MARK;
      let cmnt = finalObj.comment;
      let carsCount = Object.keys(this.RADIO_CARS_COUNT).find(key => this.RADIO_CARS_COUNT[key] === finalObj.cars_num);
      let carType = ` ${Object.keys(this.RADIO_CAR_TYPES).find(key => this.RADIO_CAR_TYPES[key] === finalObj.car_type)}`;
      let way = Object.keys(this.RADIO_WAYS).find(key => this.RADIO_WAYS[key] === finalObj.way);
      if (isComplaint) {
        carType = '';
      } else if (cmnt) {
        carType = ` ${carType}: ${carsCount}`;
      } else {
        carType += '.';
      }
      let hdr = `${isComplaint ? 'Жалоба! ': ''}${finalObj.kpp}. ${way}.${carType}`
      if (!cmnt) {
        cmnt = `${carsCount}`;
      }
      const cmntObj = {
        header: hdr,
        comment: cmnt,
        added: new Date().toISOString(),
        isAddedByScript: true,
      };
      this.comments.push(cmntObj)
    },
  },
  beforeUnmount() {
    clearInterval(this.fetch_timer);
    this.emitter.off('add-comment');
  },
  mounted() {
    clearInterval(this.fetch_timer)
    // this.getFish()
    // this.comments_timer = setInterval(this.getFish, 2000)
    setTimeout(this.fetchComments, 1234)
    // this.comments_timer = setInterval(this.fetchComments, 2000)
    this.emitter.on('add-comment', this.addComment);
  },
  updated() {
    if( this.is_bottom ) {
      let el = this.$refs['c' + (this.comments.length - 1).toString()][0];
      this.$refs.comms_list.scrollTo({top: el.offsetTop, behavior: 'smooth'});
    }
  }
}
</script>

<style scoped>
  #id_list{
    height: 560px;
    flex: 0 1 720px;
    overflow-y : auto;
    background-color: ghostwhite;
    padding: 0 10px 20px 10px;
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
  .complaint-word{
    color: #ff8f66;
  }
</style>