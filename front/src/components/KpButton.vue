<template>
  <button :class="{isHovering}"
        @click="isHovering=false"
        @mouseover="isHovering = true"
        @mouseout="isHovering = false"
          ref="bttn"
  >{{ text }}</button>
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
  methods:{
    click(){
      this.$refs.bttn.click();
    }
  }
}
</script>
<style scoped>
  button{
    /*display: block;*/
    text-align: center;
    max-width: 320px;
    border: 1px solid white;
    padding: 8px 15px;
    cursor: pointer;
    transition: .2s;
    user-select: none;
    font-size: .85em;
    background-color: transparent;
    color: inherit;
  }
  button:hover{
    color: black;
    background-color: ghostwhite;
  }
  button:active{
    color: white;
    background-color: gray;
  }

</style>