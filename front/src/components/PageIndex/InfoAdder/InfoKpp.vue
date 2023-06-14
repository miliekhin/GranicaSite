<template>
  <div class="radio-box">
    <radio-selector
        :items="KPP_NAMES"
        id_name="kpp"
        @radio_click="onRadioClick"
    />
  </div>
</template>
<script>
import RadioSelector from "./RadioSelector.vue";
export default {
  name: "InfoKpp",
  components: {
    RadioSelector,
  },
  props: {
    finalObject: { type: Object, default: () => ({}) },
  },
  data() {
    return {
      selection: this.KPP_NAMES[0],
    };
  },
  methods: {
    onRadioClick(kppName) {
      this.selection = kppName;
    },
    getResult() {
      return this.selection;
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