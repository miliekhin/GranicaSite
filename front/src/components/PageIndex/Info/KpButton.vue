<template>
  <span
      :style="styleStr"
      @click="isHovering = false"
      @mouseover="isHovering = true"
      @mouseout="isHovering = false"
      v-html="text"
  >
  </span>
</template>

<script>
export default {
  name: "KpButton",
  props: ['text', 'styleStr'],
  data(){
    return{
    }
  },

}
</script>
<style scoped>
  span {
    text-align: center;
    max-width: 320px;
    border: 1px solid whitesmoke;
    padding: 8px 15px;
    cursor: pointer;
    transition: .2s;
    user-select: none;
    font-size: 18px;
    color: whitesmoke;
    display: inline-block;
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