<template>
<div v-html="text"></div>
</template>

<script>
export default {
  name: "AfterSend",
  props: ['text', ],
}
</script>

<style scoped>
  div{
    margin-bottom: 40px;
    text-align: center;
    line-height: 1.5em;
  }
</style>