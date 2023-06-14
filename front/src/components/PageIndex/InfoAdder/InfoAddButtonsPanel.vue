<template>
  <div id="buttons-line">
    <div id="buttons-box">
      <kp-button
          v-if="textBack"
          style="margin-right: 15px"
          :text="textBack"
          @click="onBack"
      />
      <kp-button
          v-if="textCancel"
          :title="textCancel.includes('Cross') ? 'Отмена' : ''"
          :style-str="textCancel.includes('Cross') ? 'color: #ff8f66' : ''"
          :text="textCancel"
          @click="onCancel"
      />
      <kp-button
          v-if="textNext"
          style="margin-left: 15px"
          :style-str="textNext === 'Отправить' ? 'color: #ff8f66' : ''"
          :text="textNext"
          @click="onNext"
      />
    </div>
  </div>
</template>

<script>
import KpButton from "../Info/KpButton.vue";

export default{
  name: "InfoAddButtonsPanel",
  components: {KpButton},
  props: {
    textBack: { type: String, default: '' },
    textCancel: { type: String, default: '' },
    textNext: { type: String, default: '' },
  },
  methods: {
    onNext() {
      this.$emit('nextAdder');
    },
    onCancel() {
      this.$emit('cancelAdder');
    },
    onBack() {
      this.$emit('backAdder');
    }
  }
}
</script>

<style scoped>
  #buttons-line {
    display: flex;
    justify-content: flex-end;
  }
  #buttons-box {
    display: flex;
    flex: 1;
    justify-content: flex-end;
  }
</style>