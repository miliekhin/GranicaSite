<template>
  <div class="block_big" id="id_big_adder">
    <div class="block_inner" id="id_adder">

      <div id="id_adder_head">
        <h6>ДОБАВЬТЕ ДАННЫЕ</h6>
        <div class="under_h6">Добавьте ваши данные о количестве машин перед КПП или напишите жалобу</div>
      </div>
      <div id="block_adder_form_block">
        <div id="adder-buttons"
            v-if="!currentBlockType"
        >
          <kp-button
              text="ДОБАВИТЬ ДАННЫЕ"
              @click="currentBlockType = 'cars'"
          />
          <kp-button
              text="НАПИСАТЬ ЖАЛОБУ"
              @click="currentBlockType = 'complaint'"
          />
        </div>
        <info-adder-wrapper
            v-else
            :block-type="currentBlockType"
            :kpps="kpps"
            :is-inited="isInited"
            @cancelAdder="currentBlockType = ''"
        />
      </div>
    </div>
  </div>
</template>

<script>
import KpButton from "../Info/KpButton.vue";
import InfoAdderWrapper from "./InfoAdderWrapper.vue";

export default {
  name: "BlockInfoAdder",
  components: {
    InfoAdderWrapper,
    KpButton,
  },
  props: {
    kpps: { type: Array, default: () => [] },
    isInited: { type: Boolean, default: false },
  },
  data() {
    return {
      currentBlockType: '',
    }
  },
  methods: {

  }
}
</script>

<style scoped>
h6{
  font-size: 2.5em;
  margin-top: 20px;
  margin-bottom: 0;
  font-weight: 200;
  color: #34afe3;
}
.under_h6{
  font-weight: 200;
  font-size: 1.2em;
  margin-top: 15px;
  margin-bottom: 15px;
  color: #afd8ff;
}
#id_adder{
  display: flex;
  flex-wrap: wrap;
}
#id_big_adder{
  background-color: #193651;
  padding: 50px 0;
}
#adder-buttons{
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: space-around;
  height: 300px;
  width: 300px;
}
#block_adder_form_block{
  display: flex;
  flex: 0 1 720px;
  height: 300px;
  justify-content: space-around;
}
#id_adder_head{
  flex: 1;
}
@media only screen and (max-width: 420px) {
  #id_adder_head {
    text-align: center;
    padding: 0 20px;
  }
}
@media only screen and (max-width: 1024px) {
  #id_adder {
    justify-content: space-around;
  }
}

</style>