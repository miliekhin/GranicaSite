<template>
  <div class="block_big" id="id_big_decl">
    <div class="block_inner" id="id_decl">
      <div id="id_decl_head">
        <h6>ТАМОЖЕННАЯ ДЕКЛАРАЦИЯ</h6>
        <div class="under_h6">
          Заполните и распечатайте пассажирскую таможенную декларацию заранее,
          чтобы сэкономить время при прохождении границы
        </div>
      </div>

      <div id="block_decl">

        <modal-wnd
          v-if="showModal"
          @close-modal="closeModalWnd"
          :modalData="modalData"
        >
          <template #modalBody>
            <div v-if="modalData.eventName === 'declarationForm'">
              <input-text-field
                v-for="(itm, i) in inputsData"
                :key="i"
                :topText="itm.topText"
                :bottomText="itm.bottomText"
                :localStorageKey="itm.localStorageKey"
                :type="itm.type"
                @key-enter="closeModalWnd(modalData.eventName)"
              />
            </div>
            <p v-if="modalData.eventName === 'deleteDeclData'">
              Все данные введенные в форму таможенной декларации будут удалены!
            </p>
            <div v-if="modalData.eventName === 'notifyBeforePrint'">
              <p class="hint-item">
                <span class="icon-check-2"></span>
                Рекомендуется еще раз внимательно проверить данные перед распечаткой деклараций
              </p>
              <p class="hint-item">
                <span class="icon-check-2"></span>
                Декларацию необходимо распечатать с обоих сторон листа, в двух экземплярах
              </p>
              <p class="hint-item">
                <span class="icon-check-2"></span>
                После распечатки декларации, пожалуйста не забудьте поставить число и подпись на обоих экземплярах
              </p>
            </div>
          </template>
        </modal-wnd>

        <!--vue-mobile-detection library-->
        <img v-if="$isMobile()" class="img_decl" src="../Declaration/assets/declaration.png" alt="Бланк декларации" draggable="false">
        <router-link v-else id="img_lnk" :to="{ name: 'declaration', params:{ inputs } }">
          <img class="img_decl" src="../Declaration/assets/declaration.png" alt="Бланк декларации" draggable="false">
        </router-link>
        <div id="id_decl_menu">
          <div class="btn" @click="showModalWnd('declarationForm')">ЗАПОЛНИТЬ</div>
          <div class="btn" @click="showModalWnd('notifyBeforePrint')">РАСПЕЧАТАТЬ</div>
          <div class="processing" v-if="pdfRendering">Подготовка документа...</div>
          <div class="btn" v-else @click="saveDecl()">СКАЧАТЬ</div>
          <div class="btn" v-if="isDeclarationSomeData" @click="showModalWnd('deleteDeclData')">УДАЛИТЬ ДАННЫЕ</div>
        </div>
        <div id="id_decl_hint">
          <span class="icon-asterisk"></span> Данные декларации будут храниться только в этом браузере и на этом компьютере
        </div>
        <div id="mobile-view">
          Заполнение и распечатка декларации недоступны на мобильном устройстве
        </div>
      </div>

    </div>
  </div>
  <declaration-pdf :inputs="inputs"/>
</template>

<script>
import html2pdf from "html2pdf.js";
import ModalWnd from "../ModalWnd.vue";
import InputTextField from "../Declaration/InputTextField.vue";
import DeclarationPdf from "../Declaration/DeclarationPdf.vue";
import {util} from "../../tools.js"

export default {
  name: "BlockDeclaration",
  components: {ModalWnd, InputTextField, DeclarationPdf},
  data(){
    return{
      pdfEmptyRendering: false,
      pdfRendering: false,
      isDeclarationSomeData: false,
      showModal: false,
      modalData:{
        headText: '',
        cancelBttnText: '',
        okBttnText: '',
        eventName: '',
      },
      inputsData: [
        {
          topText: "Фамилия",
          bottomText: "Фамилия декларанта",
          localStorageKey: "surname",
        },
        {
          topText: "Имя",
          bottomText: "Имя декларанта",
          localStorageKey: "name"
        },
        {
          topText: "Отчество",
          bottomText: "Отчество декларанта",
          localStorageKey: "patronymic"
        },
        {
          topText: "Документ удостоверяющий личность",
          bottomText: "Введите через запятую: наименование документа, страна выдачи, " +
              "серия номер, дата выдачи.Пример: Паспорт, Украина, ВВ 234567, 01.02.1999",
          localStorageKey: "identityDocument"
        },
        {
          topText: "Адрес постоянного места жительства (регистрации)",
          bottomText: "Пример: Украина, Донецкая область, г. Донецк, ул. Артёма 12 кв. 11",
          localStorageKey: "homeAddress"
        },
        {
          topText: "Адрес временного проживания (пребывания) в государстве – члене ЕАЭС",
          bottomText: "Пример: Россия, Ростовская область, г. Таганрог, ул. Ленина 22",
          localStorageKey: "tempAddress"
        },
        // {
        //   <!--            topText: "Страна отправления"-->
        //   <!--            bottomText: "Введите Украина, если выезжаете из ДНР"-->
        //   <!--            localStorageKey: "fromCountry"-->
        // },
        {
          topText: "Страна назначения",
          bottomText: "Введите страну назначения, например: Россия",
          localStorageKey: "toCountry"
        },
        {
          topText: "Количество лиц не достигших 16-летнего возраста",
          bottomText: "Введите в цифрах количество лиц пересекающих границу которые не достигли 16-летнего возраста",
          type: "number",
          localStorageKey: "underageCount"
        },
        {
          topText: "Марка и модель автомобиля",
          bottomText: "Пример: Toyota Corolla",
          localStorageKey: "carModel"
        },
        {
          topText: "Регистрационный номер автомобиля, страна регистрации",
          bottomText: "Пример: В012АЕ DPR, Украина",
          localStorageKey: "carID"
        },
        {
          topText: "VIN номер автомобиля",
          bottomText: "Номер указан в тех. паспорте автомобиля. Пример: MTAJNY65Т44255422",
          localStorageKey: "carVIN"
        },
        {
          topText: "Объем двигателя",
          bottomText: "Введите объем двигателя как в тех. паспорте автомобиля, например: 2259",
          type: "number",
          localStorageKey: "engineVolume"
        },
        {
          topText: "Дата или год выпуска автомобиля",
          bottomText: "Введите год или дату выпуска автомобиля как указано в тех. паспорте, например: 2005",
          localStorageKey: "carYear"
        },
        {
          topText: "Рыночная стоимость автомобиля",
          bottomText: "Введите примерную рыночную стоимость автомобиля на текущее время в рублях РФ, например: 500000",
          type: "number",
          localStorageKey: "carCost"
        },
      ],
    }
  },
  mounted() {
    this.isDeclarationSomeData = util.isDeclarationFilled(this.inputsData)
  },
  computed:{
    inputs(){
      return JSON.stringify(this.inputsData);
    }
  },
  methods:{
    showModalWnd(modalName){
      this.modalData.eventName = modalName;
      if (modalName === 'deleteDeclData'){
        this.modalData.headText = 'ПРЕДУПРЕЖДЕНИЕ';
        this.modalData.cancelBttnText = 'ОТМЕНА';
        this.modalData.okBttnText = 'ПРОДОЛЖИТЬ';
      }
      if (modalName === 'notifyBeforePrint'){
        this.modalData.headText = 'НАПОМИНАНИЕ';
        this.modalData.cancelBttnText = 'ОТМЕНА';
        this.modalData.okBttnText = 'ПРОДОЛЖИТЬ';
      }
      if (modalName === 'declarationForm'){
        this.modalData.headText = 'ДАННЫЕ ТАМОЖЕННОЙ ДЕКЛАРАЦИИ';
        this.modalData.cancelBttnText = 'ЗАКРЫТЬ';
        this.modalData.okBttnText = 'СОХРАНИТЬ';
      }
      this.showModal = true;
      this.emitter.emit('modalOpenClose');
    },
    closeModalWnd(eventName){
      console.log('closeModalWnd', eventName)
      switch (eventName) {
        case 'declarationForm':
          this.isDeclarationSomeData = util.isDeclarationFilled(this.inputsData)
          break;
        case 'notifyBeforePrint':
          this.$router.push({ name: 'declaration_print', params: {'needPrint': 'true', 'inputs': this.inputs} });
          break;
        case 'deleteDeclData':
          this.deleteDeclarationData();
          break;
        default:
          break;
      }
      this.showModal = false;
      this.emitter.emit('modalOpenClose');
    },
    deleteDeclarationData(){
      for(let itm of this.inputsData){
        localStorage.removeItem(itm.localStorageKey)
      }
      this.isDeclarationSomeData = util.isDeclarationFilled(this.inputsData)
    },
    async saveDecl(){
      let el = document.getElementById('id_declaration_pdf_body');
      let clonedElement = el.cloneNode(true);
      clonedElement.style.display = 'block';

      let opt = {
        margin: 0,
        filename: "declaration.pdf",
        image: {
          type: "jpeg",
          quality: 0.98
        },
        html2canvas: {
          dpi: 192,
          letterRendering: true,
          useCORS: true,
        },
        jsPDF: {
          unit: "in",
          format: "letter",
          orientation: "portrait"
        },
        pagebreak: {
          mode: 'avoid-all', after: '.page'
        },
      };
      this.pdfRendering = true;
      await html2pdf().set(opt).from(clonedElement).save();
      this.pdfRendering = false;
      clonedElement.remove();
    },
  },

}
</script>

<style scoped>
  .hint-item{
    display: flex;
    align-items: center;
  }
  .icon-check-2{
    color: limegreen;
    font-size: 1.7em;
    margin-right: 20px;
  }
  h6{
    font-size: 2.5em;
    margin-top: 20px;
    margin-bottom: 0;
    font-weight: 200;
    color: #fff3a0;
  }
  .under_h6{
    font-weight: 200;
    font-size: 1.2em;
    margin-top: 15px;
    margin-bottom: 15px;
    color: #eee;
  }
  #id_decl{
    display: flex;
  }
  #id_decl_head{
    flex: 1;
  }
  #id_big_decl{
    background-color: #00435c;
    padding: 50px 0;
  }
  #block_decl{
    display: flex;
    flex-wrap: wrap;
    flex: 0 1 720px;
    line-height: 1.5em;
    color: white;
  }
  .img_decl:hover{
    transform: scale(1.1);
  }
  .img_decl{
    margin-left: 50px;
    margin-right: 40px;
    cursor: pointer;
    transition: .3s;
  }
  #id_decl_menu{
    width: 235px;
    /*font-size: 1.1em;*/
  }
  .btn:hover{
    border-bottom: 1px dashed white;
  }
  .btn{
    display: inline-block;
    box-sizing: border-box;
    cursor: pointer;
    margin-bottom: 19px;
    margin-right: 38px;
    text-decoration: none;
    color: inherit;
    border-bottom: 1px solid #00000000;
  }
  .processing{
    box-sizing: border-box;
    margin-bottom: 19px;
    text-decoration: none;
    color: darkgray;
    border-bottom: 1px solid #00000000;
  }
  #id_decl_hint{
    color: #ccc;
    font-size: .85em;
    font-weight: 300;
    margin: 20px 20px 0;
  }
  #mobile-view{
    display: none;
    margin: 20px;
    text-align: center;
  }

  @media only screen and (max-width: 1024px) {
    #mobile-view{
      display: block;
    }
    #id_decl_menu, #id_decl_hint{
      display: none;
    }
    #block_decl{
      justify-content: center;
    }
  }
  @media only screen and (max-width: 768px) {
    #id_decl{
      flex-wrap: wrap;
    }
    .under_h6{
      margin-bottom: 66px;
    }
  }
  @media only screen and (max-width: 320px) {
    h6{
      font-size: 2.2em;
    }
  }
  @media only screen and (max-width: 420px) {
    .under_h6{
      margin-bottom: 15px;
    }
    #id_decl_head {
      text-align: center;
      padding: 0 20px;
    }
    #block_decl{
      margin-top: 40px;
    }
    #id_decl_menu{
      margin-left: 60px;
    }
    #img_lnk{
      width: 100%;
      text-align: center;
    }
    img{
      width: 75%;
      margin-bottom: 35px;
    }
    .btn, .processing{
      margin-bottom: 31px;
    }
  }

</style>
