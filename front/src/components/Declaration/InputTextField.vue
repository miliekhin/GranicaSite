<template>
  <div id="id_body">
    <div id="id_top_text">{{topText}}</div>
    <input
        maxlength="256"
        @keydown.enter.prevent="$emit('keyEnter')"
        :type="type ? type : 'text'"
        v-model="fieldValue"
    />
    <div id="id_bottom_text">{{bottomText}}</div>
  </div>
</template>

<script>
export default {
  name: "InputTextField",
  props: ['topText', 'bottomText', 'defaultValue', 'type', 'localStorageKey'],
  data(){
    return{
      fieldValue: '',
    }
  },
  watch:{
    fieldValue(){
      localStorage.setItem(this.localStorageKey, this.fieldValue);
    }
  },
  mounted() {
    let val = localStorage.getItem(this.localStorageKey);
    if ( val === null ){
      val = '';
    }
    this.fieldValue = val;
  }
}
</script>

<style scoped>
  #id_body{
    margin-bottom: 20px;
  }
  input{
    width: 100%;
    box-sizing: border-box;
    font-family: Montserrat, sans-serif;
    font-size: 1em;
    margin: 4px 0;
  }
  #id_top_text{
    font-size: .9em;
    color: white;
    line-height: 1.25em;
  }
  #id_bottom_text{
    font-size: .8em;
    color: #d4d4d4;
    line-height: 1.25em;
  }
</style>