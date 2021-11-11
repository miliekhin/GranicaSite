<template>
  <div id="id-wrp">
    <div id="id-txt" :class="grow">{{txt}}</div>
    <div id="id-check">{{isChecked ? '&#9745;' : '&#9744;'}}</div>
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
  #id-check{
    font-size: 18pt;
    margin-left: 4px;
    line-height: 18pt;
  }
</style>