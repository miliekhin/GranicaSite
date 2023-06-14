<template>
  <div id="sent-ok" v-if="isSent">
      Спасибо за информацию!
      <br>
    <span v-if="isComplaint">
      После проверки ваша жалоба будет опубликована на сайте.
    </span>
    <span v-else>
      Вы сделали доброе дело.
      <br><br>
      После проверки ваши данные будут опубликованы на сайте.
    </span>
  </div>
  <div id="sending" v-if="isSending">
    Идёт отправка данных...
    <spinner />
  </div>
</template>

<script>
import Spinner from "../Info/Spinner.vue";

export default {
  name: "InfoSender",
  components: {
    Spinner,
  },
  props: {
    isComplaint: { type: Boolean, default: false },
    finalObject: { type: Object, default: () => ({}) },
    kpps: { type: Array, default: () => [] },
  },
  emits: [
    'send-finished',
    'send-error',
  ],
  data() {
    return {
      isSent: false,
      isSending: true,
    }
  },
  methods: {
    isDataValid() {
      const cars = this.finalObject.cars_num;
      if ( cars >= this.MAX_CARS_LIMIT && cars < this.FUZZY_CARS_COUNT_MARK) {
        return false
      }
      return true
    },
    getCookie(cname) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${cname}=`);
      if (parts.length === 2) {
        return parts.pop().split(';').shift();
      }
      return '';
    },
    startSending() {
      setTimeout(() => {
        this.sendData();
      }, 1234);
    },
    async sendData() {
      if(!this.isDataValid()) {
        this.isSent = true;
        this.isSending = false;
        this.$emit('send-finished');
        return;
      }
      const kpp = this.getKppObj();
      if (this.finalObject.cars_num >= this.FUZZY_CARS_COUNT_MARK) {
        this.setNewComment();
      } else {
        this.setCarsCountInfo(kpp);
      }

      // if(this.DEBUG_MODE) {
      //   this.isSent = true;
      //   this.isSending = false;
      //   this.$emit('send-finished');
      //   return;
      // }

      const data = {
        kpp: kpp.id,
        // from_ldnr: Boolean(!this.info_data.way),
        cars_num: this.finalObject.cars_num,
        car_type: this.finalObject.car_type,
        comment: this.finalObject.comment.trim()
      }
      // console.log('send: ', JSON.stringify(data))

      const url = `${this.URL}kpp/`;
      try {
        // const response = await fetch(url, {
        await fetch(url, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken'),
          }
        })
        // const json = await response.json();
        // console.log('Response:', JSON.stringify(json), response.status)
        localStorage.setItem('sent', Date());
        this.isSent = true;
        this.isSending = false;
        this.$emit('send-finished');
      }
      catch (error) {
        console.error('Send info error:', error)
        this.$emit('send-error');
        this.emitter.emit('fetch_error', error)
      }
    },
    getKppObj() {
      let kpp = this.kpps.find(kpp =>
        kpp.name.toUpperCase() === this.finalObject.kpp.toUpperCase()
        && kpp.from_ldnr === Boolean(!this.finalObject.way)
      );
      if (kpp === undefined) {
        this.emitter.emit('fetch_error', 'КПП не найден');
      }
      // kpp = info_data_obj.way ? kpp.to_ldnr : kpp.to_rf
      return kpp;
    },
    setCarsCountInfo(kpp) {
      // Количество машин сразу добавляется на табло
      // console.log(info_data_obj, kpp)
      kpp.info[this.finalObject.car_type].shift();
      let obj = {
        cars_num: this.finalObject.cars_num,
        car_type: this.finalObject.car_type,
        added: new Date().toISOString(),
      };
      kpp.info[this.finalObject.car_type].push(obj);
    },
    setNewComment() {
      this.emitter.emit('add-comment', this.finalObject);
    },
  },
}
</script>

<style scoped>
  div{
    text-align: center;
    font-size: 18px;
    line-height: 1.5em;
  }
  #sent-ok{
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
  }
  #sending{
    display: flex;
    flex: 1;
    flex-direction: column;
    justify-content: center;
  }
</style>