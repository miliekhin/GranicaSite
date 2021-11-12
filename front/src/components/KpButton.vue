<template>
  <span :class="{isHovering}"
        @click="isHovering=false"
        @mouseover="isHovering = true"
        @mouseout="isHovering = false"
  >{{ text }}</span>
</template>

<script>
export default {
  name: "KpButton",
  props: ['text'],
  data(){
    return{
      // text: 'text'
      isHovering: false
    }
  },

}
</script>
<style scoped>
  span{
    /*display: block;*/
    text-align: center;
    max-width: 320px;
    border: 1px solid white;
    padding: 8px 15px;
    cursor: pointer;
    transition: .2s;
    user-select: none;
    font-size: .85em;
  }
  span:hover{
    color: black;
    background-color: ghostwhite;
  }
  span:active{
    color: white;
    background-color: gray;
  }

</style>