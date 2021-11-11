<template>
<!--  <fieldset>-->
<!--    <legend>{{head}}:</legend>-->
    <div id="id_rb_group">
      <div v-for="(item, i) in items" :key="id_name+i" class="item">
        <input
            type="radio"
            :id="id_name+i"
            :name="id_name"
            :value="i"
            :checked="info_data === i"
            @click="$emit('radio_click', {val: i, name: id_name})"
        >
        <label :for="id_name+i">{{item}}</label>
      </div>
<!--      <div class="item">-->
<!--        <input type="radio" id="id_kpp2" name="kpp" value="2">-->
<!--        <label for="id_kpp2">Мариновка</label>-->
<!--      </div>-->
<!--      <div class="item">-->
<!--        <input type="radio" id="id_kpp3" name="kpp" value="3">-->
<!--        <label for="id_kpp3">Новоазовск</label>-->
<!--      </div>-->
    </div>
</template>

<script>
export default {
  name: "InfoKpp",
  props: ['items', 'id_name', 'info_data', ],
  data(){
    return{
      initial_check: 0,
    }
  },


}
</script>

<style scoped>

  legend{
    margin: 10px 0;
  }
  .item{
    margin: 9px 0;
  }

  #id_rb_group {
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    font-size: .85em;

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