<template>
  <div id="id-wrp" :class="classNarrow">
    <div id="id-cell"><strong>{{ txt }}</strong></div>
    <span id="id-under">({{ under }})</span>
  </div>
</template>

<script>
  export default {
    name: "Cell",
    props: ['txt', 'under', 'narrow'],
    computed:{
      classNarrow(){
        if( this.narrow ){
          return 'narrow'+this.narrow;
        }
        return 'narrow0'
      }
    },
  }
</script>

<style scoped>
  div{
    text-align: center;
  }
  #id-wrp{
    margin: 0 5px;
  }
  .narrow3{
    flex: 0 1 80px;
  }
  .narrow2{
    flex: 0 1 90px;
  }
  .narrow1{
    flex: 0 1 140px;
  }
  .narrow0{
    flex: 1;
  }
  #id-cell{
    display: flex;
    justify-content:center;
    align-items:flex-end;
    border-bottom: 1px solid black;
    height: 24px;
    padding: 0 10px;
    white-space: nowrap;
  }
  #id-under{
    display: block;
    font-size: 8pt;
    /*line-height: 1.2em;*/
  }
</style>