<template>
  <div id="id-wrp">
    <div id="id-txt" :class="grow">{{txt}}</div>
    <div id="id-check-empty">
      <span v-if="isChecked" class="icon-check-2"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: "CellCheck",
  props: ['txt', 'isChecked', 'nogrow'],
  computed:{
    grow(){
      if( !this.nogrow ) return 'grow'
      return 'nogrow';
    }
  }
}
</script>

<style scoped>
  #id-wrp{
    display: flex;
    /*flex: 1;*/
    margin-right: 22px;
    /*line-height: 1em;*/
    padding-bottom: 5px;
  }
  .nogrow{
    flex: 0;
    margin-right: 10px;
    margin-left: 30px;
  }
  .grow{
    flex: 1;
  }
  #id-txt{
    margin-right: 7px;
  }
  #id-check-empty{
    margin-top: 4px;
    width: 16px;
    height: 16px;
    border: 1px solid black;
  }
</style>