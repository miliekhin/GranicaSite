<template>
  <div id="adder-frame">
    <header>{{headText}}</header>
    <div id="form-body">
      <KeepAlive>
        <component
          :is="currentBodyComponent"
          ref="bodyForm"
          :is-complaint="isComplaint"
          :final-object="finalObject"
          :kpps="kpps"
          @send-finished="onInfoSendFinished"
          @send-error="onInfoSendError"
        />
      </KeepAlive>
    </div>
    <info-add-buttons-panel
      :text-back="textBack"
      :text-cancel="textCancel"
      :text-next="textNext"
      @cancelAdder="cancelAdding"
      @nextAdder="onNext"
      @backAdder="onBack"
    />
  </div>
</template>
<script>
import InfoWait from "./InfoWait.vue";
import InfoSiteNotReady from "./InfoSiteNotReady.vue";
import InfoAddButtonsPanel from "./InfoAddButtonsPanel.vue";
import InfoCarsFuzzy from "./InfoCarsFuzzy.vue";
import InfoCarsNumber from "./InfoCarsNumber.vue";
import InfoKpp from "./InfoKpp.vue";
import InfoWay from "./InfoWay.vue";
import InfoCarType from "./InfoCarType.vue";
import InfoComment from "./InfoComment.vue";
import InfoDataCheck from "./InfoDataCheck.vue";
import InfoSender from "./InfoSender.vue";
export default{
  name: "InfoAdderWrapper",
  components: {
    InfoWait,
    InfoSiteNotReady,
    InfoAddButtonsPanel,
    InfoCarsNumber,
    InfoCarsFuzzy,
    InfoKpp,
    InfoWay,
    InfoCarType,
    InfoComment,
    InfoDataCheck,
    InfoSender,
  },
  props: {
    blockType: { type: String, default: '' },
    kpps: { type: Array, default: () => [] },
    isInited: { type: Boolean, default: false },
  },
  emits: ['cancelAdder'],
  data() {
    return {
      bodyFormsOpts: {
        cars: [
          {
            headText: 'Пожалуйста подождите...',
            bodyComponent: 'InfoWait',
          },
          {
            headText: 'Пожалуйста подождите...',
            bodyComponent: 'InfoSiteNotReady',
          },
          {
            headText: 'Сколько машин перед шлагбаумом?',
            bodyComponent: 'InfoCarsFuzzy',
          },
          {
            headText: 'Укажите число машин:',
            bodyComponent: 'InfoCarsNumber',
          },
          {
            headText: 'Укажите КПП:',
            bodyComponent: 'InfoKpp',
          },
          {
            headText: 'Укажите направление:',
            bodyComponent: 'InfoWay',
          },
          {
            headText: 'Укажите тип транспорта:',
            bodyComponent: 'InfoCarType',
          },
          {
            headText: 'Ваш комментарий:',
            bodyComponent: 'InfoComment',
          },
          {
            headText: 'Проверьте ваши данные:',
            bodyComponent: 'InfoDataCheck',
          },
          {
            headText: '',
            bodyComponent: 'InfoSender',
          },

        ],
        complaint: [
          {
            headText: 'Пожалуйста подождите...',
            bodyComponent: 'InfoWait',
          },
          {
            headText: 'Пожалуйста подождите...',
            bodyComponent: 'InfoSiteNotReady',
          },
          {
            headText: 'Опишите суть проблемы:',
            bodyComponent: 'InfoComment',
          },
          {
            headText: 'Укажите КПП:',
            bodyComponent: 'InfoKpp',
          },
          {
            headText: 'Укажите направление:',
            bodyComponent: 'InfoWay',
          },
          {
            headText: 'Проверьте ваши данные:',
            bodyComponent: 'InfoDataCheck',
          },
          {
            headText: '',
            bodyComponent: 'InfoSender',
          },
        ],
      },
      finalObject: {
        cars_num: 0,
        kpp: 0,
        way: 0,
        car_type: 0,
        comment: '',
      },
      currentBodyComponent: 'InfoCarsFuzzy',
      textBack: '&laquo; Назад',
      textCancel: '&Cross;',
      textNext: 'Далее &raquo;',
      resultFuzzySelect: -1,
    };
  },
  created() {
    if (!this.isReadyToAddInfo() || !this.isInited) {
      this.currentBodyComponent = !this.isInited ? 'InfoSiteNotReady': 'InfoWait';
      this.textNext = '';
      this.textBack = '';
      this.textCancel = 'OK';
    } else if(this.isComplaint) {
      this.currentBodyComponent = 'InfoComment';
    }
  },
  computed: {
    headText() {
      return this.bodyFormsOpts[this.blockType]
          .find((itm) => itm.bodyComponent === this.currentBodyComponent).headText;
    },
    isComplaint() {
      return this.blockType === 'complaint';
    }
  },
  methods: {
    isReadyToAddInfo() {
      if(this.DEBUG_MODE)
        return true

      const sentTime = localStorage.getItem('sent')
      const sent = new Date(sentTime)
      const now = new Date()
      const unblockedAfterMs = this.SEND_INFO_PERIOD_LIMIT - (now - sent)
      if( unblockedAfterMs > 0) {
        return false
      }
      return true
    },
    cancelAdding() {
      this.finalObject.cars_num = 0;
      this.finalObject.kpp = 0;
      this.finalObject.way = 0;
      this.finalObject.car_type = 0;
      this.finalObject.comment = '';
      this.$emit('cancelAdder');
    },
    onNext() {
      switch (this.currentBodyComponent) {
        case 'InfoCarsFuzzy':
          this.resultFuzzySelect = this.$refs.bodyForm.getResult();
          this.finalObject.cars_num = this.resultFuzzySelect;
          this.currentBodyComponent = this.resultFuzzySelect === -1 ? 'InfoCarsNumber' : 'InfoKpp';
          break;
        case 'InfoCarsNumber':
          this.finalObject.cars_num = this.$refs.bodyForm.getResult();
          this.currentBodyComponent = 'InfoKpp';
          break;
        case 'InfoKpp':
          this.finalObject.kpp = this.$refs.bodyForm.getResult();
          this.currentBodyComponent = 'InfoWay';
          break;
        case 'InfoWay':
          this.finalObject.way = this.$refs.bodyForm.getResult();
          if (this.isComplaint) {
            this.textNext = 'Отправить';
            this.currentBodyComponent = 'InfoDataCheck';
          } else {
            this.currentBodyComponent = 'InfoCarType';
          }
          break;
        case 'InfoCarType':
          this.finalObject.car_type = this.$refs.bodyForm.getResult();
          this.currentBodyComponent = 'InfoComment';
          break;
        case 'InfoComment':
          this.finalObject.comment = this.$refs.bodyForm.getResult();
          if (this.isComplaint) {
            if(this.$refs.bodyForm.isValid()) {
              this.currentBodyComponent = 'InfoKpp';
            }
          } else {
            this.textNext = 'Отправить';
            this.currentBodyComponent = 'InfoDataCheck';
          }
          break;
        case 'InfoDataCheck':
          if (this.isComplaint) {
            this.finalObject.cars_num = this.COMPLAINT_MARK;
          }
          this.textNext = '';
          this.textBack = '';
          this.textCancel = '';
          this.currentBodyComponent = 'InfoSender';
          this.$nextTick(() => {
            this.$refs.bodyForm.startSending();
          });
          break;
        default:
          break;
      }

    },
    onBack() {
      switch (this.currentBodyComponent) {
        case 'InfoCarsFuzzy':
          this.cancelAdding();
          break;
        case 'InfoCarsNumber':
          this.currentBodyComponent = 'InfoCarsFuzzy';
          break;
        case 'InfoKpp':
          if (this.isComplaint) {
            this.currentBodyComponent = 'InfoComment';
          } else {
            this.currentBodyComponent = this.resultFuzzySelect === -1 ? 'InfoCarsNumber' : 'InfoCarsFuzzy';
          }
          break;
        case 'InfoWay':
          this.currentBodyComponent = 'InfoKpp';
          break;
        case 'InfoCarType':
          this.currentBodyComponent = 'InfoWay';
          break;
        case 'InfoComment':
          if (this.isComplaint) {
            this.cancelAdding();
          } else {
            this.currentBodyComponent = 'InfoCarType';
          }
          break;
        case 'InfoDataCheck':
          this.textNext = 'Далее &raquo;';
          if (this.isComplaint) {
            this.currentBodyComponent = 'InfoWay';
          } else {
            this.currentBodyComponent = 'InfoComment';
          }
          break;
        case 'InfoSender':
          this.textBack = '&laquo; Назад';
          this.textCancel = '&Cross;';
          this.textNext = 'Далее &raquo;';
          this.currentBodyComponent = 'InfoDataCheck';
          break;
        default:
          break;
      }
    },
    onInfoSendFinished() {
      this.textCancel = 'Отлично!';
    },
    onInfoSendError() {
      this.onBack();
    },
  },
};
</script>

<style scoped>
  #adder-frame{
    padding: 10px;
    display: flex;
    flex: 0 1 500px;
    flex-direction: column;
    color: white;
    background-color: #21415f;
  }
  header{
    height: auto;
  }
  #form-body{
    display: flex;
    flex-direction: column;
    flex: 1;
  }
</style>