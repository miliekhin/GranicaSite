<template>
  <div>
    <declaration-body :needPrint="needPrint" :inputs="inputs"/>
  </div>
</template>

<script>
import DeclarationBody from "./DeclarationBody.vue";
export default {
  name: "DeclarationPrint",
  components: {DeclarationBody},
  props: ['needPrint', 'inputs'],
}
</script>

<style scoped>
  /*body {*/
  /*  width: 100%;*/
  /*  height: 100%;*/
  /*  margin: 0;*/
  /*  padding: 0;*/
  /*  background-color: #FAFAFA;*/
  /*}*/
  div:deep(.book){
    font: 11pt "Times New Roman";
  }
  div:deep(.page) {
    width: 210mm;
    min-height: 297mm;
    padding: 10mm 10mm 10mm 25mm;
    margin: 10mm auto;
    border: 1px #D3D3D3 solid;
    border-radius: 5px;
    background: white;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  }
  div:deep(.subpage) {
    /*padding: 1cm;*/
    /*border: 1px grey solid;*/
    height: 256mm;
    /*outline: 2cm white solid;*/
  }
  @page {
    size: A4;
    margin: 0;
  }
  @media print {
    /*html, body {*/
    /*  width: 210mm;*/
    /*  height: 297mm;*/
    /*}*/
    div:deep(.page) {
      margin: 0;
      border: initial;
      border-radius: initial;
      width: initial;
      min-height: initial;
      box-shadow: initial;
      background: initial;
      page-break-after: always;
    }
  }
</style>