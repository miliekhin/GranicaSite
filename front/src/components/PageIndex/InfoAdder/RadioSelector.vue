<template>
  <div id="id_rb_group">
    <div
        v-for="(item, i) in items"
        :key="idName+i"
        class="radio-item"
    >
      <input
          type="radio"
          :id="idName+i"
          :name="idName"
          :checked="selekkta === i"
          @click="$emit('radio_click', item)"
      >
      <label :for="idName+i">{{item}}</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "RadioSelector",
  props: {
    idName: { type: String, default: 'idname' },
    items: { type: Array, default: () => [] },
    selekkta: { type: Number, default: 0 },
  },
  data(){
    return {
    }
  },


}
</script>

<style scoped>
  .radio-item{
    margin: 5px 0;
  }
  legend{
    margin: 10px 0;
  }

  #id_rb_group {
    display: flex;
    flex-direction: column;
    font-size: 18px;
  }

  label {
    /*margin-right: 15px;*/
    /*line-height: 32px;*/
    cursor: pointer;
    position: relative;
    bottom: 4px;
  }

  input {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;

    border-radius: 50%;
    width: 20px;
    height: 20px;

    border: 3px solid white;
    transition: 0.2s all linear;
    outline: none;
    margin-right: 12px;

    position: relative;
    /*top: 4px;*/
    cursor: pointer;
  }

  input:checked {
    border: 5px solid orangered;
  }
  input:checked:after {
    content: '';
    display: block;
    position: absolute;
    top: -8px;
    bottom: -8px;
    left: -8px;
    right: -8px;
    border-radius: 50%;
    border: 2px solid whitesmoke;
  }

</style>