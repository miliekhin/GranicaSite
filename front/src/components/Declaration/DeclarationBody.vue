<template>
  <div class="book">
    <div class="page">
      <div class="subpage">
        <div id="id-head"><strong>ПАССАЖИРСКАЯ ТАМОЖЕННАЯ ДЕКЛАРАЦИЯ</strong></div>
        <div id="id-p2">
          Заполняется физическим лицом, достигшим 16-летнего возраста.<br>
          В случае утвердительного ответа в соответствующем поле проставляется знак
          "<span class="icon-check-2"></span>" или "<span class="icon-times"></span>".<br>
          Экземпляр оформленной пассажирской таможенной декларации сохраняется на весь период временного
          пребывания на таможенной территории ЕАЭС (за ее пределами) и предъявляется таможенному органу при
          выезде (возвращении).
        </div>
        <div>
          <strong>1. Сведения о декларанте:</strong>
          <div class="multi-cell">
            <cell :txt="fields.surname" under="фамилия"/>
            <cell :txt="fields.name" under="имя"/>
            <cell :txt="fields.patronymic" under="отчество"/>
          </div>
          <cell :txt="fields.identityDocument" under="документ, удостоверяющий личность (наименование, страна выдачи, серия, номер, дата выдачи)"/>
          <cell :txt="fields.homeAddress" under="адрес постоянного места жительства (регистрации) (заполняется при ввозе (в том числе временном) транспортного
            средства, ввозе или вывозе наличных денежных средств и (или) денежных инструментов, транзите"/>
          <cell :txt="fields.tempAddress" under="адрес временного проживания (пребывания) в государстве – члене ЕАЭС (заполняется иностранным лицом при ввозе (в том числе
            временном) транспортного средства, ввозе или вывозе наличных денежных средств и (или) денежных инструментов, транзите"/>
          <div class="multi-cell">
            <cell :txt="fields.fromCountry" under="страна отправления"/>
            <cell :txt="fields.toCountry" under="страна назначения"/>
          </div>
          <div id="id-p3">
            Со мной следуют лица, не достигшие 16-летнего возраста, в количестве
            <span style="display: inline-block; text-align:center; border-bottom: 1px solid black; width: 30px"><strong>{{fields.underageCount}}</strong></span> чел.<br>
            Мной, следующими со мной лицами, не достигшими 16-летнего возраста, либо в мой адрес (от меня)
            перемещаются следующие товары и транспортные средства:
          </div>
          <div class="p4"><strong>2. Сведения о способе перемещения товаров и транспортных средств:</strong></div>
          <div class="multi-cell">
            <cell-check style="width: 900px" :is-checked="fields.cargo" txt="2.1. Сопровождаемый багаж, включая ручную кладь"/>
            <cell-check txt="2.2. Несопровождаемый багаж (багаж, следующий отдельно от въезжающего/выезжающего лица)
              (при въезде лица заполняется для учета норм ввоза товаров без уплаты платежей)"/>
            <cell-check style="width: 700px" txt="2.3. Доставляемые в адрес (пересылаемые) товары без въезда/выезда лица"/>
          </div>
          <div class="p4"><strong>3. Сведения о товарах:</strong></div>
          <div class="multi-cell">
            <cell-check txt="Ввоз (свободное обращение)"/>
            <cell-check style="flex: 0 1 70px;" txt="Вывоз"/>
            <cell-check txt="Временный вывоз"/>
            <cell-check txt="Транзит (для товаров, ввозимых со льготой)"/>
          </div>
          <cell-check style="margin-top: 10px;" txt="3.1. Наличные денежные средства и (или) дорожные чеки свыше 10 000 $ в эквиваленте (на 1 лицо), векселя, чеки (банковские чеки), ценные бумаги <*>"/>
          <cell-check txt="3.2. Товары, ввозимые с освобождением от уплаты таможенных пошлин, налогов (ввоз со льготой)"/>
          <cell-check txt="3.3. Товары, стоимость, вес и (или) количество которых превышают нормы ввоза без уплаты таможенных пошлин, налогов"/>
          <cell-check txt="3.4. Культурные ценности"/>
          <cell-check txt="3.5. Гражданское и служебное оружие, его основные (составные) части, патроны к нему"/>
          <cell-check txt="3.6. Наркотические средства, психотропные вещества, их прекурсоры в виде лекарственных средств"/>
          <cell-check txt="3.7. Животные, растения"/>
          <cell-check txt="3.8. Коллекционные материалы по минералогии, палеонтологии, кости ископаемых животных"/>
          <cell-check txt="3.9. Образцы биологических материалов человека"/>
          <cell-check txt="3.10. Другие товары, в отношении которых подлежат соблюдению запреты и ограничения и требуется представление подтверждающих документов и (или) сведений"/>

        </div>
      </div>
    </div>
    <div class="page">
      <div class="subpage">
        <div class="p4">
          <strong>4. Дополнительные сведения о товарах, в том числе указанных в графах 3.2 - 3.10:</strong>
        </div>
        <table>
          <tr>
            <td width="29">N<br>п/п</td>
            <td>Наименование товара и его описание (идентификационный номер и другие отличительные признаки), наименования, даты и номера
              документа, подтверждающего соблюдение условий ввоза с освобождением от уплаты таможенных пошлин, налогов,
              и (или) документа, подтверждающего соблюдение ограничений, а также наименования органов, выдавших такие документы
            </td>
            <td>Вес (с учетом фактически перемещаемой первичной упаковки) (кг)/количество (л, шт.)</td>
            <td>Стоимость (в валюте государства - члена ЕАЭС, евро или долларах США)</td>
          </tr>
          <tr v-for="i in 12" :key="i">
            <td/><td/><td/><td/>
          </tr>
        </table>
        <div class="p4"><strong>5. Сведения о транспортных средствах:</strong></div>
        <div class="multi-cell">
          <cell-check txt="Ввоз (свободное обращение)"/>
          <cell-check :is-checked="fields.tempImport" txt="Временный ввоз"/>
          <cell-check nogrow='1' txt="Вывоз"/>
          <cell-check txt="Временный вывоз"/>
          <cell-check nogrow='1' style="margin-right: 0" txt="Транзит"/>
        </div>
        <cell-check style="margin: 8px 0" txt="Транспортные средства, ввозимые с освобождением от уплаты таможенных
          пошлин, налогов (ввоз со льготой)"/>
        <div class="multi-cell">
          <cell-check :is-checked="fields.vehicle" txt="Авто- и мототранспортное средство"/>
          <cell-check nogrow='1' txt="Прицеп"/>
        </div>
        <div class="multi-cell">
          <cell :txt="fields.carModel" under="марка, модель"/>
          <cell :txt="fields.carID" under="регистрационный номер, страна регистрации"/>
          <cell :txt="fields.carVIN" under="идентификационный номер"/>
          <cell :txt="fields.engineVolume" under="рабочий объем двигателя (см3)" narrow="2"/>
        </div>
        <div class="multi-cell">
          <cell :txt="fields.carVIN" under="номер кузова"/>
          <cell txt="" under="номер шасси"/>
          <cell :txt="fields.carYear" under="дата изготовления" narrow="2"/>
          <cell :txt="spacedCost(fields.carCost)" under="стоимость" narrow="1"/>
        </div>
        <div class="multi-cell">
          <div class="mc-txt">Водное судно</div>
          <cell txt="" under="вид"/>
          <cell txt="" under="регистрационный номер, страна регистрации"/>
          <cell txt="" under="стоимость"/>
          <cell txt="" under="масса (кг)" narrow="2"/>
          <cell txt="" under="длина корпуса (м)" narrow="2"/>
        </div>
        <div class="multi-cell">
          <div class="mc-txt">Воздушное судно</div>
          <cell txt="" under="вид"/>
          <cell txt="" under="регистрационный номер, страна регистрации"/>
          <cell txt="" under="стоимость"/>
          <cell txt="" under="масса пустого снаряженного аппарата (кг)"/>
        </div>
        <div style="margin-bottom: -9px">Часть транспортного средства, замененная в государстве, не являющемся членом ЕАЭС,</div>
        <div class="multi-cell">
          <div class="mc-txt">и подлежащая учету (регистрации)</div>
          <cell txt="" under="наименование, номер"/>
        </div>
        <div style="margin-top: 5px">
          Мне известно, что сообщение в пассажирской таможенной декларации недостоверных сведений влечет
          за собой ответственность в соответствии с законодательством государства - члена ЕАЭС.
        </div>
        <div class="multi-cell">
          <cell txt="" under="дата" narrow="1"/>
          <cell txt="" under="подпись" narrow="2"/>
          <cell txt="" under="Ф.И.О. лица, действующего от имени и по поручению декларанта, реквизиты документа"/>
        </div>
        <hr>
        <div style="font-size: .8em">Для служебных отметок:</div>
        <div style="display: flex; margin-bottom: 20px;">
          <div style="width: 80px; height: 80px; border: 1px solid black; margin-left: 20px; margin-top: 10px;">
            <div style="margin-top: 90px; text-align: center; font-size: .7em">М.П.</div></div>
          <div style="flex: 1; margin-left: 20px">
            <div class="p5" v-for="i in 6" :key="i"/>
          </div>
        </div>
        <div style="font-size: .7em">&lt;*> Необходимо заполнить приложение к пассажирской таможенной декларации.</div>

      </div>
    </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";
import CellCheck from "./CellCheck.vue";
import {util} from "../../tools.js"

export default {
  name: "DeclarationBody",
  components: {CellCheck, Cell},
  props: ['needPrint', 'inputs'],
  data(){
    return {
      fields: {},
    }
  },
  mounted() {
    const arr = JSON.parse(this.inputs);
    if( util.isDeclarationFilled(arr) )
    {
      this.fillDeclaration( arr );
    }
    this.$nextTick(() => {
      if( this.needPrint ){
        window.print();
      }
    })
  },
  methods:{
    fillDeclaration( arr ){
      this.fields.fromCountry = 'Украина';
      this.fields.cargo = true;
      this.fields.tempImport = true;
      this.fields.vehicle = true;
      for ( let a of arr){
        this.fields[a.localStorageKey] = localStorage.getItem(a.localStorageKey);
      }
      this.fields.underageCount = this.fields.underageCount || 0;
    },
    spacedCost(digit){
      let cost = util.formatDigitSpaceSeparated(digit);
      if( cost ){
        cost += ' руб.';
      }
      return cost;
    },

  },
}
</script>

<style scoped>
  * {
    box-sizing: border-box;
    -moz-box-sizing: border-box;
  }
  .p5{
    border-bottom: 1px solid black;
    height: 17px;
  }
  .mc-txt{
    padding-top: 10px;
  }
  table, th, td {
    border-collapse: collapse;
    table-layout: fixed;
    border: 1px solid black;
  }
  td{
    vertical-align: top;
    height: 19px;
    padding: 3px;
  }
  table{
    border-collapse: collapse;
    font-size: .8em;
  }
  td{
    text-align: center;
  }
  .multi-cell{
    display: flex;
    justify-items: center;
  }
  #id-head{
    margin-bottom: 5px;
    text-align: center;
  }
  #id-p2{
    border: 1px solid black;
    padding: 5px;
    margin-bottom: 7px;
    /*line-height: 1em;*/
  }
  #id-p3{
    margin-top: 7px;
  }
  .p4{
    margin-top: 10px;
    margin-bottom: 6px;
  }
  hr{
    border: 1px solid transparent;
    border-bottom: 1px solid black;
    box-sizing: border-box;
    margin: 15px 0;
  }

</style>