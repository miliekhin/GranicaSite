<template>
  <div class="info_card">
    <div id="id_info_wrp" :class="onStart">

      <div id="id_info_head"
           v-if="current_step"
           :class="current_step>=7 ? 'center_head':''"
      >
        {{head[current_step]}}{{current_step < 7 ? ':':''}}
      </div>
      <div v-if="!current_step" id="id_add_data_block">
        <div id="id_add_data_head">
          Добавьте свои данные, если вы сейчас находитесь перед границей, и знаете количество машин до шлагбаума
        </div>
        <kp-button text="ДОБАВИТЬ ДАННЫЕ" @click="startAdder"/>
      </div>

      <info-cars :info_data="info_data" v-else-if="current_step===1"/>
      <radio-selector :info_data="info_data.kpp" v-else-if="current_step===2" :items="static_data.kpp_names" id_name="kpp" @radio_click="onRadioClick" />
      <radio-selector :info_data="info_data.way" v-else-if="current_step===3" :items="static_data.way" id_name="way" @radio_click="onRadioClick" />
      <radio-selector :info_data="info_data.car_type" v-else-if="current_step===4" :items="static_data.car_type" id_name="car_type" @radio_click="onRadioClick" />
      <info-comment :info_data="info_data" v-else-if="current_step===5"/>
      <info-final :info_data="info_data" :static_data="static_data" v-else-if="current_step===6"/>
      <after-send  v-else-if="current_step===7" :text="txt_after_send"/>
      <after-send  v-else-if="current_step===8" :text="txt_block_send"/>

      <div class="btn_panel" id="id_buttons" v-show="current_step">
        <kp-button text="&laquo; Назад" @click="onBack" v-if="current_step < 7 && current_step"/>
        <div id="cross_btn" title="Отмена">
          <kp-button
              :text="current_step < 7 ? '&Cross;' : 'OK'"
              @click="onCancel" v-if="current_step < 9 && current_step"
          />
        </div>
        <kp-button
            :text="current_step===6 ? 'Отправить' : 'Далее &raquo;'"
            @click="onNext"
            v-if="current_step < 7 && current_step"
        />
        <!--    <kp-button text="Отправить" @click="onSend" v-else-if="current_step===6"/>-->
      </div>

    </div>
  </div>
</template>

<script>
import AfterSend from "./AfterSend.vue"
import InfoFinal from "./InfoFinal.vue"
import InfoCars from "./InfoCars.vue"
import RadioSelector from "./RadioSelector.vue"
import InfoComment from "./InfoComment.vue"
import KpButton from "./KpButton.vue"
export default {
  name: "InfoAdder",
  components:{InfoComment, InfoCars, RadioSelector, KpButton, InfoFinal, AfterSend},
  props: ['is_inited', "kpps"],
  data(){
    return{
      static_data: {
        kpp_names: this.KPP_NAMES,
        way: ['В сторону РФ', 'В сторону ДНР',],
        car_type: ['Легковые', 'Грузовые',],
      },
      txt_after_send: 'Вы сделали доброе дело<br><br> Ваша информация будет учтена при следующем обновлении данных',
      txt_block_send: '',
      head: [
        '',
        'Количество машин',
        'Укажите КПП',
        'Укажите направление',
        'Укажите тип транспорта',
        'Ваш комментарий',
        'Проверьте данные',
        'СПАСИБО!',
        'Пожалуйста подождите...',
      ],
      current_step: 0,
      onStart: 'onStart',
      info_data: {
        cars: 16,
        kpp: 0,
        way: 0,
        car_type: 0,
        comment: '',
      },
    }
  },
  methods:{
    getCookie(cname) {
      let name = cname + "=";
      let decodedCookie = decodeURIComponent(document.cookie);
      let ca = decodedCookie.split(';');
      for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    },
    startAdder(){
      if(!this.is_inited){
        this.emitter.emit('fetch_error', 'Сайт ещё не готов к работе.')
        return
      }
      let sent_time = localStorage.getItem('sent')
      if(sent_time)
        if(!this.checkSendPeriod(sent_time))
          return

      this.current_step++
      this.onStart = 'afterStart'
    },
    checkSendPeriod(sent_time){
      if(this.DEBUG_MODE)
        return true

      let sent = new Date(sent_time)
      let now = new Date()
      let unblocked_after_ms = this.SEND_INFO_PERIOD_LIMIT - (now - sent)
      // console.log(unblocked_after_ms)
      if( unblocked_after_ms > 0){
        let mins = Math.floor(unblocked_after_ms / 1000 / 60) + 1
        let msg = '<br>Вы снова сможете отправить данные примерно через<br>'
        let tmin = ' минут'
        if (mins < 5)
          tmin = ' минуты'
        if (mins === 1)
          tmin = ' минуту'
        this.txt_block_send = msg + mins + tmin
        this.current_step = 8
        this.onStart = 'afterStart'
        return false
      }
      return true
    },
    onBack(){
      this.current_step--
      if( !this.current_step ){
        this.onStart = 'onStart'
      }
    },
    onCancel(){
      this.current_step = 0
      this.onStart = 'onStart'
    },
    onNext(){
      this.current_step++
      if( this.current_step === 7){
        // if(this.isDataValid())
          this.sendInfo()
      }
    },
    onRadioClick(obj){
      this.info_data[obj.name] = obj.val
    },
    isDataValid(){
      if (this.info_data.cars === this.MAX_CARS)
        return false
      if (this.info_data.cars >= 256)
        return false

      return true
    },
    async sendInfo(){
      const url = this.URL + 'kpp/'
      let kpp = this.getKppObj( this.info_data )
      this.setCarsCountInfo(this.info_data, kpp)
      // return
      if( !this.isDataValid() )
        return

      const data = {
        kpp: kpp.id,
        // from_ldnr: Boolean(!this.info_data.way),
        cars_num: this.info_data.cars,
        car_type: this.info_data.car_type,
        comment: this.info_data.comment.trim()
      }
      // console.log('send: ', JSON.stringify(data))

      try {
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken'),
          }
        })
        const json = await response.json();
        console.log('Response:', JSON.stringify(json), response.status)
        localStorage.setItem('sent', Date());
      }
      catch (error) {
        console.error('Send info error:', error)
        this.emitter.emit('fetch_error', error)
      }
      this.info_data.comment = ''
      // this.onCancel()
    },
    getKppObj(info_data_obj){
      let kpp = this.kpps.find(kpp => kpp.name.toUpperCase() === this.KPP_NAMES[info_data_obj.kpp].toUpperCase() && kpp.from_ldnr === Boolean(!info_data_obj.way))
      if (kpp === undefined) {
        this.emitter.emit('fetch_error', 'КПП не найден')
      }
      // kpp = info_data_obj.way ? kpp.to_ldnr : kpp.to_rf
      return kpp
    },
    setCarsCountInfo(info_data_obj, kpp){
      // Количество машин сразу добавляется на табло
      console.log(info_data_obj, kpp)
      kpp.info[info_data_obj.car_type].shift()
      let obj = {
        cars_num: info_data_obj.cars,
        car_type: info_data_obj.car_type,
        added: new Date().toISOString()
      }
      kpp.info[info_data_obj.car_type].push(obj)
    },
  },
  // mounted() {
  //   console.log('csrf: ' + this.getCookie('csrftoken'))
  // }

}
</script>

<style scoped>
  .info_card{
    padding: 15px;
    border: #404040 solid 1px;
    /*width: 320px;*/
    /*max-width: 420px;*/
    /*flex: 0 1 380px;*/
    max-width: 380px;
    box-sizing: border-box;
    background-color: rgba(31, 56, 69, .7);
    /*background-color: rgba(31, 56, 69, .32);*/
    /*backdrop-filter: blur(8px);*/
    margin: 20px auto;
  }
  @media only screen and (max-width: 1024px) {
    .info_card{
      margin-bottom: 20px;
      margin-top: 0;
    }
  }
  #id_add_data_head{
    font-size: .8em;
    /*font-weight: 300;*/
    text-align: center;
    color: #ddd;
  }
  #id_add_data_block{
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-around;
    height: 200px;
  }
  #id_info_wrp{
    /*border: 1px solid white;*/
    display: flex;
    max-width: 320px;
    flex-direction: column;
    /*justify-content: space-between;*/
    /*margin-top: 40px;*/
    margin: auto;
    height: 250px;
  }
  .onStart{
    justify-content: space-around;
  }
  .afterStart{
    justify-content: space-between;
  }
  .btn_panel{
    display: flex;
  }
  #id_buttons{
    justify-content: space-between;
  }
  #cross_btn{
    display: flex;
    justify-content: space-around;
    flex: 1;
  }
  #id_butt_send{
    justify-content: space-around;
  }
  .center_head{
    text-align: center;
  }

</style>