<template>
  <div class="radio-box">
    <radio-selector
        :items="Object.keys(RADIO_CAR_TYPES)"
        id_name="way"
        @radio_click="onRadioClick"
    />
  </div>
</template>
<script>
import RadioSelector from "./RadioSelector.vue";
export default {
  name: "InfoCarType",
  components: {
    RadioSelector,
  },
  props: {
    finalObject: { type: Object, default: () => ({}) },
  },
  data() {
    return {
      selection: Object.keys(this.RADIO_CAR_TYPES)[0],
    };
  },
  methods: {
    onRadioClick(key) {
      this.selection = key;
    },
    getResult() {
      return this.RADIO_CAR_TYPES[this.selection];
    }
  },
}
</script>

<style scoped>
  .radio-box{
    display: flex;
    flex: 1;
    padding-left: 15px;
    padding-top: 15px;
    padding-bottom: 15px;
    align-items: center;
  }

</style>